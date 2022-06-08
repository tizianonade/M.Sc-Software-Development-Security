import subprocess
import cryptography
from mqtt_functions import send_cert_request, send_msg_request
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509

SUCCESS = 0

# ************************** PART: managing certificate requests *********************************

def create_folder_certificate():
    #Create certificate folder if it doesn't exist
    p_check_folder = subprocess.run("ls /home/v2/ | grep certificate", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_folder.returncode == SUCCESS):
        p_create_folder = subprocess.run("mkdir -p /home/v2/certificate/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_folder.returncode == SUCCESS:
            print("Vehicle 2: Certificate folder created!")

def create_key_pairs():
    #Create RSA key pair
    p_check_key = subprocess.run("ls /home/v2/certificate/ | grep v2_key.pem", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_key = subprocess.run("openssl genrsa -out \"/home/v2/certificate/v2_key.pem\" 2048", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_key.returncode == SUCCESS:
            print("Vehicle 2: RSA key pair created!")

    p_check_key_pub = subprocess.run("ls /home/v2/certificate/ | grep \"v2_pub_key.pem\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key_pub.returncode == SUCCESS):
        p_create_key_pub = subprocess.run("openssl rsa -in \"/home/v2/certificate/v2_key.pem\" -pubout -out \"/home/v2/certificate/v2_pub_key.pem\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_key_pub.returncode == SUCCESS:
            print("Vehicle 2: RSA public key created!")

def create_cert_request():
    p_check_key = subprocess.run("ls /home/v2/certificate/ | grep v2.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not(p_check_key.returncode == SUCCESS):
        p_create_cert_req = subprocess.run("openssl req -new -key \"/home/v2/certificate/v2_key.pem\" -out \"/home/v2/certificate/v2.csr\" -subj \"/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=gateway\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_create_cert_req.returncode == SUCCESS:
            print("Vehicle 2: Certificate request created!\n")

def get_cert_request():
    p_check_cert_req = subprocess.run("cat /home/v2/certificate/v2.csr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_check_cert_req.returncode == SUCCESS:
        pass
    return p_check_cert_req.stdout[:-1]

def request_certificate(client):
    create_folder_certificate()
    create_key_pairs()
    create_cert_request()
    cert_req = get_cert_request()
    send_cert_request(client, "cert_req", "v2", "192.168.0.3", "/cert_requests",cert_req)
    print("Vehicle 2: Certificate request sent to CA (192.168.0.4)!\n")

# ************************** PART: managing certificate received *********************************

def save_certificate_pki(received):
    with open('/home/v2/certificate/pki.crt','w') as fd :
        fd.write(received['pki_cert'])
        fd.close()
        print("Vehicle 2: PKI Certificate received from CA ({})!".format(received['ip']))

def save_certificate_user(received):
    with open('/home/v2/certificate/v2.crt','w') as fd :
        fd.write(received['user_cert'])
        fd.close()
        print("Vehicle 2: V2 Certificate received from CA ({})!\n".format(received['ip']))

def save_pki_pub_key(received):
    with open('/home/v2/certificate/pki_pub_key.pem','w') as fd:
        fd.write(received['pki_pub_key'])
        fd.close()
        print("Vehicle 2: PKI public key received from CA ({})!".format(received['ip']))

def save_data(received):
    save_certificate_pki(received)
    save_pki_pub_key(received)
    save_certificate_user(received)

# ************************** PART: managing the sent of messages to other vehicles *********************************

def read_cert():
    data = ""
    with open('/home/v2/certificate/v2.crt','r') as fd :
        data = fd.read()
        fd.close()

    return data[:-1]

def read_pub_key():
    data = ""
    with open('/home/v2/certificate/v2_pub_key.pem', 'r') as fd:
        data = fd.read()
        fd.close()

    return data[:-1]

def send_msg(client):
    cert = read_cert()
    pub_key = read_pub_key()
    msg = {"stationId":"v2", "stationType":5,"name":"vehicle2", "causeEvent":4, "lon":17.025, "lat":5.215}
    send_msg_request(client, "msg_req", "v2", "192.168.0.2", "192.168.0.3", "/msg_requests", cert, pub_key, msg)
    print("Vehicle 1: DENM message sent to Gateway (192.168.0.4)!")

# ************************** PART: managing the reception of message from other vehicles *********************************

def save_cert_user(received):
    with open('/home/v2/certificate/{}.crt'.format(received['name']),'w') as fd:
        fd.write(received['cert'])
        fd.close()
        print("Vehicle 2: V1 Certificate received from Gateway ({})!".format(received['ip_s']))

def save_pub_key_user(received):
    with open('/home/v2/certificate/{}_pub_key.pem'.format(received['name']),'w') as fd:
        fd.write(received['pub_key'])
        fd.close()
        print("Vehicle 2: V1 public key received from Gateway ({})!\n".format(received['ip_s']))

def cert_cleaned(received):
    print("Vehicle 2: V1 Certificate verification...")
    cert_verified = False
    result = str()
    p_verify = subprocess.run("openssl verify -CAfile \"/home/v2/certificate/pki.crt\" \"/home/v2/certificate/{}.crt\" | grep OK".format(received['name']), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_verify.returncode == SUCCESS:
        result = p_verify.stdout

    if result[:-1] == "/home/v2/certificate/v1.crt: OK":
        cert_verified = True 

    return  cert_verified

def verify_authentification(received):

    cert_to_check = x509.load_pem_x509_certificate(byteArray)
    issuer_public_key.verify(
        cert_to_check.signature,
        cert_to_check.tbs_certificate_bytes,
        # Depends on the algorithm used to create the certificate
        padding.PKCS1v15(),
        cert_to_check.signature_hash_algorithm,
    )

def user_authentified(received):
    print("Vehicle 2: V1 authentification process...!")
    auth = True

    f = open("/home/v2/certificate/pki_pub_key.pem")
    imagestring = f.read()
    byteArray = bytes(imagestring,encoding='utf8')

    issuer_public_key = load_pem_public_key(byteArray)

    f = open("/home/v2/certificate/{}.crt".format(received['name']))
    imagestring = f.read()
    byteArray = bytes(imagestring,encoding='utf8')

    try:
        cert_to_check = x509.load_pem_x509_certificate(byteArray)
        issuer_public_key.verify(
                cert_to_check.signature,
                cert_to_check.tbs_certificate_bytes,
                # Depends on the algorithm used to create the certificate
                padding.PKCS1v15(),
                cert_to_check.signature_hash_algorithm,
        )
    except cryptography.exceptions.InvalidSignature:
        print("Vehicle 2: User not authentified!")
        auth = False    

    return auth

def manage_response(received):
    print("Vehicle 2: DENM message received from Gateway ({})!".format(received['ip_s']))
    #Save certificat & pub key
    save_cert_user(received)
    save_pub_key_user(received)

    #Verify certificate
    if cert_cleaned(received) :
        print("Vehicle 2: YES, V1 Certificate is valid!\n")
        
        #Verify authentification
        if user_authentified(received) :
            print("Vehicle 2: User V1 authentified!\n")

            #Print message from user
            print("Vehicle 2: DENM Message from user V1:")
            print("stationId: {}".format(received['msg']['stationId']))
            print("stationType: {}".format(received['msg']['stationType']))
            print("causeEvent: {}".format(received['msg']['causeEvent']))
            print("name: {}".format(received['msg']['name']))
            print("lon: {}".format(received['msg']['lon']))
            print("lat: {}".format(received['msg']['lat']))

    #Send back a message

