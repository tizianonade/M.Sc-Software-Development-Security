#!/bin/python3
import threading
import json
from mqtt_functions import *
from cert_functions import request_certificate, save_certificate


def on_message_received(client, userdata, message):
    received = json.loads(str(message.payload.decode("utf-8")))
    if received['code'] == 'cert_resp':
        save_certificate(received)

#Send request to pki for getting certificate
def main1():
    #Connect to broker pki 
    client = connect_to_broker("hub","192.168.0.4")
    #Send request a certificate to pki
    request_certificate(client)

#Receive certificate
def main2():
    #Connect to broker gateway
    client = subscribe_to_broker("hub", "127.0.0.1", "/home/hub/certificate")
    #Thread role
    client.on_message = on_message_received
    client.loop_forever()

th1 = threading.Thread(target=main1)
th2 = threading.Thread(target=main2)
th1.start()
th2.start()
th1.join()
th2.join()
