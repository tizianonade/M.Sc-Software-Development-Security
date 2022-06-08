#!/bin/python3
import threading
import json
import time
from mqtt_functions import *
from cert_functions import build_pki, response_certificate, response_msg

def on_cert_received(client, userdata, message):
    received = json.loads(str(message.payload.decode("utf-8")))
    if received["code"] == "cert_req":
        response_certificate(received)

def on_msg_received(client, userdata, message):
    received = json.loads(str(message.payload.decode("utf-8")))
    if received["code"] == "msg_req":
        response_msg(received)

def main1():
    build_pki()
    client = subscribe_to_broker("gateway1", "127.0.0.1", "/cert_requests")
    client.on_message = on_cert_received
    client.loop_forever()

def main2():
    client = subscribe_to_broker("gateway2", "127.0.0.1", "/msg_requests")
    client.on_message = on_msg_received
    client.loop_forever()

th1 = threading.Thread(target=main1)
th2 = threading.Thread(target=main2)
th1.start()
th2.start()
th1.join()
th2.join()