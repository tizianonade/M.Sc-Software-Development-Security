import subprocess
from mqtt_functions import send_cert_request

SUCCESS = 0

def create_folder_certificate():
    #Create certificate folder if it doesn't exist
    p_check_folder = subprocess.run("ls /home/gateway/ | grep certificate", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_folder.returncode == SUCCESS):
        p_create_folder = subprocess.run("mkdir -p /home/gateway/certificate/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_folder.returncode == SUCCESS:
            print("Gateway: Certificate folder created!")

def create_key_pairs():
    #Create RSA key pair
    p_check_key = subprocess.run("ls /home/gateway/certificate/ | grep gateway_key.pem", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_key = subprocess.run("openssl genrsa -out \"/home/gateway/certificate/gateway_key.pem\" 2048", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_key.returncode == SUCCESS:
            print("Gateway: RSA key pair created!")

def create_cert_request():  
    p_check_key = subprocess.run("ls /home/gateway/certificate/ | grep gateway.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_cert_req = subprocess.run("openssl req -new -key \"/home/gateway/certificate/gateway_key.pem\" -out \"/home/gateway/certificate/gateway.csr\" -subj \"/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=gateway\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_cert_req.returncode == SUCCESS:
            print("Gateway: Certificate request created!\n")

def get_cert_request():  
    p_check_cert_req = subprocess.run("cat /home/gateway/certificate/gateway.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_check_cert_req.returncode == SUCCESS:
        pass
    return p_check_cert_req.stdout[:-1]

def request_certificate(client):
    create_folder_certificate()
    create_key_pairs()
    create_cert_request()
    cert_req = get_cert_request()
    send_cert_request(client, "cert_req", "gateway", "192.168.0.2", "/home/pki/cert_requests",cert_req)
    print("Gateway: Certificate request sent to 192.168.0.4!")

def save_certificate(received):
    with open('/home/gateway/certificate/gateway.crt','w') as fd :
        fd.write(received['data'])
        fd.close()
        print("Gateway: Certificate received from {}!\n".format(received['ip']))




