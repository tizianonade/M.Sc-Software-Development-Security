import subprocess
from mqtt_functions import *

SUCCESS = 0

# ************************** PKI certificate *********************************

def create_folder_certificate():
    #Create certificate folder if it doesn't exist
    p_check_folder = subprocess.run("ls /home/pki/ | grep certificate", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_folder.returncode == SUCCESS):
        p_create_folder = subprocess.run("mkdir -p /home/pki/certificate/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_folder.returncode == SUCCESS:
            print("PKI: Certificate folder created!")

def create_folder_requests():
    #Create request folder if it doesn't exist
    p_check_folder = subprocess.run("ls /home/pki/ | grep cert_requests", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_folder.returncode == SUCCESS):
        p_create_folder = subprocess.run("mkdir -p /home/pki/cert_requests/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_folder.returncode == SUCCESS:
            print("PKI: Request certificate folder created!")

def create_key_pairs():
    #Create RSA key pair
    p_check_key = subprocess.run("ls /home/pki/certificate/ | grep pki_key.pem", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_key = subprocess.run("openssl genrsa -out \"/home/pki/certificate/pki_key.pem\" 2048", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_key.returncode == SUCCESS:
            print("PKI: RSA key pair created!")

def create_root_certificate():  
    p_check_key = subprocess.run("ls /home/pki/certificate/ | grep pki.crt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_cert_req = subprocess.run("openssl req -x509 -days 365 -key \"/home/pki/certificate/pki_key.pem\" -out \"/home/pki/certificate/pki.crt\" -subj \"/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=pki\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_cert_req.returncode == SUCCESS:
            print("PKI: Root certificate created!\n")

def build_pki():
    create_folder_certificate()
    create_folder_requests()
    create_key_pairs()
    create_root_certificate()


# ************************** Response certificate *********************************
  
def create_certificate(received):
    #Save file
    print("PKI: Certificate request received from {}!".format(received['ip']))
    p_check_request = subprocess.run("ls /home/pki/cert_requests/ | grep {}.csr".format(received['name']), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_request.returncode == SUCCESS):
        with open('/home/pki/cert_requests/gateway.csr','w') as fd :
            fd.write(received['data'])
            fd.close()

        #Create certificate
        p_create_cert = subprocess.run("openssl x509 -req -in  \"/home/pki/cert_requests/gateway.csr\" -CA \"/home/pki/certificate/pki.crt\" -CAkey \"/home/pki/certificate/pki_key.pem\" -CAcreateserial -out \"/home/pki/certificate/gateway.crt\" -days 365", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_cert.returncode == SUCCESS:
            print("PKI: Certificate created for {}!".format(received['ip']))
        else:
            print("PKI: Error creating certificate")

def read_certificate(name):
    p_read_cert = subprocess.run("cat /home/pki/certificate/{}".format(name), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_read_cert.returncode == SUCCESS:
        data = p_read_cert.stdout
    return data[:-1]
   
def response_certificate(received):
    #Create certificate    
    create_certificate(received)

    #Connect to broker
    client = connect_to_broker("pki","192.168.0.2")

    #Send certificate
    data = read_certificate(str(received['name'])+".crt")
    send_cert_response(client,"cert_resp","pki","192.168.0.4", "/home/gateway/certificate",data)
    print("PKI: Certificate sent to {}!\n".format(received['ip']))