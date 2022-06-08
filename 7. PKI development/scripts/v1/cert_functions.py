import subprocess
from mqtt_functions import send_cert_request, send_msg_request

SUCCESS = 0

# ************************** PART: managing certificate requests *********************************

def create_folder_certificate():
    #Create certificate folder if it doesn't exist
    p_check_folder = subprocess.run("ls /home/v1/ | grep certificate", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_folder.returncode == SUCCESS):
        p_create_folder = subprocess.run("mkdir -p /home/v1/certificate/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_folder.returncode == SUCCESS:
            print("Vehicle 1: Certificate folder created!")

def create_key_pairs():
    #Create RSA key pair
    p_check_key = subprocess.run("ls /home/v1/certificate/ | grep v1_key.pem", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_key = subprocess.run("openssl genrsa -out \"/home/v1/certificate/v1_key.pem\" 2048", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_key.returncode == SUCCESS:
            print("Vehicle 1: RSA key pair created!")

    p_check_key_pub = subprocess.run("ls /home/v1/certificate/ | grep \"v1_pub_key.pem\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key_pub.returncode == SUCCESS):
        p_create_key_pub = subprocess.run("openssl rsa -in \"/home/v1/certificate/v1_key.pem\" -pubout -out \"/home/v1/certificate/v1_pub_key.pem\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_key_pub.returncode == SUCCESS:
            print("Vehicle 1: RSA public key created!")

def create_cert_request():
    p_check_key = subprocess.run("ls /home/v1/certificate/ | grep v1.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_cert_req = subprocess.run("openssl req -new -key \"/home/v1/certificate/v1_key.pem\" -out \"/home/v1/certificate/v1.csr\" -subj \"/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=gateway\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_cert_req.returncode == SUCCESS:
            print("Vehicle 1: Certificate request created!\n")

def get_cert_request():
    p_check_cert_req = subprocess.run("cat /home/v1/certificate/v1.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_check_cert_req.returncode == SUCCESS:
        pass
    return p_check_cert_req.stdout[:-1]

def request_certificate(client):
    create_folder_certificate()
    create_key_pairs()
    create_cert_request()
    cert_req = get_cert_request()
    send_cert_request(client, "cert_req", "v1", "192.168.0.2", "/cert_requests",cert_req)
    print("Vehicle 1: Certificate request sent to CA (192.168.0.4)!\n")

# ************************** PART: managing certificate received *********************************

def save_certificate_pki(received):
    with open('/home/v1/certificate/pki.crt','w') as fd :
        fd.write(received['pki_cert'])
        fd.close()
        print("Vehicle 1: PKI Certificate received from CA ({})!".format(received['ip']))

def save_certificate_user(received):
    with open('/home/v1/certificate/v1.crt','w') as fd :
        fd.write(received['user_cert'])
        fd.close()
        print("Vehicle 1: V1 Certificate received from CA ({})!\n".format(received['ip']))

def save_pki_pub_key(received):
    with open('/home/v1/certificate/pki_pub_key.pem','w') as fd:
        fd.write(received['pki_pub_key'])
        fd.close()
        print("Vehicle 1: PKI public key received from CA ({})!".format(received['ip']))

def save_data(received):
    save_certificate_pki(received)
    save_pki_pub_key(received)
    save_certificate_user(received)

# ************************** PART: managing send message to other vehicles *********************************

def read_cert():
    data = ""
    with open('/home/v1/certificate/v1.crt','r') as fd :
        data = fd.read()
        fd.close()

    return data

def read_pub_key():
    data = ""
    with open('/home/v1/certificate/v1_pub_key.pem', 'r') as fd:
        data = fd.read()
        fd.close()

    return data[:-1]

def send_msg(client):
    cert = read_cert()
    pub_key = read_pub_key()
    msg = {"stationId":"v1", "stationType":5,"name":"vehicle1", "causeEvent":4, "lon":17.025, "lat":5.215}
    send_msg_request(client, "msg_req", "v1", "192.168.0.3", "192.168.0.2", "/msg_requests", cert, pub_key, msg)
    print("Vehicle 1: DENM message sent to Gateway (192.168.0.4)!")