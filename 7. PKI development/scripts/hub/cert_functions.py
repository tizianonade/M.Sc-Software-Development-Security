import subprocess
from mqtt_functions import send_cert_request

SUCCESS = 0

def create_folder_certificate():
    #Create certificate folder if it doesn't exist
    p_check_folder = subprocess.run("ls /home/hub/ | grep certificate", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_folder.returncode == SUCCESS):
        p_create_folder = subprocess.run("mkdir -p /home/hub/certificate/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_folder.returncode == SUCCESS:
            print("Hub: Certificate folder created!")

def create_key_pairs():
    #Create RSA key pair
    p_check_key = subprocess.run("ls /home/hub/certificate/ | grep hub_key.pem", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_key = subprocess.run("openssl genrsa -out \"/home/hub/certificate/hub_key.pem\" 2048", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_key.returncode == SUCCESS:
            print("Hub: RSA key pair created!")

def create_cert_request():  
    p_check_key = subprocess.run("ls /home/hub/certificate/ | grep hub.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_cert_req = subprocess.run("openssl req -new -key \"/home/hub/certificate/hub_key.pem\" -out \"/home/hub/certificate/hub.csr\" -subj \"/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=gateway\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_cert_req.returncode == SUCCESS:
            print("Hub: Certificate request created!\n")

def get_cert_request():  
    p_check_cert_req = subprocess.run("cat /home/hub/certificate/hub.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_check_cert_req.returncode == SUCCESS:
        pass
    return p_check_cert_req.stdout[:-1]

def request_certificate(client):
    create_folder_certificate()
    create_key_pairs()
    create_cert_request()
    cert_req = get_cert_request()
    send_cert_request(client, "cert_req", "hub", "192.168.0.3", "/home/pki/cert_requests",cert_req)
    print("Hub: Certificate request sent to 192.168.0.4!")

def save_certificate(received):
    with open('/home/hub/certificate/hub.crt','w') as fd :
        fd.write(received['data'])
        fd.close()
        print("Hub: Certificate received from {}!\n".format(received['ip']))




