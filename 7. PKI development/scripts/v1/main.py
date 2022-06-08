import threading
import json
from mqtt_functions import *
from cert_functions import *
import time

VAR = 0

def on_message_received(client, userdata, message):
    global VAR
    received = json.loads(str(message.payload.decode("utf-8")))
    
    if received['code'] == 'cert_resp':
        save_data(received)
        VAR += 1

#Send request to pki for getting certificate
def main1():
    client = connect_to_broker("v1_1","192.168.0.4")
    request_certificate(client)

#Receive certificate
def main2():
    client = subscribe_to_broker("v1_2", "127.0.0.1", "/certificate")
    client.on_message = on_message_received
    client.loop_forever()

#Send msg to v2
def main3():
    VAR

    client = connect_to_broker("v1_3","192.168.0.4")
    time.sleep(5)
    if VAR == 1:
        send_msg(client)

th1 = threading.Thread(target=main1)
th2 = threading.Thread(target=main2)
th3 = threading.Thread(target=main3)
th1.start()
th2.start()
th3.start()
th1.join()
th2.join()
th3.join()