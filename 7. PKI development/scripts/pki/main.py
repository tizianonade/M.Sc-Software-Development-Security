#!/bin/python3

import threading
import json
from mqtt_functions import *
from cert_functions import build_pki, response_certificate

def on_message_received(client, userdata, message):
    received = json.loads(str(message.payload.decode("utf-8")))
    # print(str(received))
    if received["code"] == "cert_req":
        response_certificate(received)

def main():
    #Build the pki environment
    build_pki()

    #Connect to broker pki
    client = subscribe_to_broker("pki", "127.0.0.1", "/home/pki/cert_requests")

    #Thread role
    client.on_message = on_message_received
    client.loop_forever()

th1 = threading.Thread(target=main)
th1.start()
th1.join()
