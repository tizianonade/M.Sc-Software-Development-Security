import threading
import json
from mqtt_functions import *
from cert_functions import *
import time

def on_certificate_received(client, userdata, message):
    received = json.loads(str(message.payload.decode("utf-8")))
    if received['code'] == 'cert_resp':
        save_data(received)

def on_message_received(client, userdata, message):
    received = json.loads(str(message.payload.decode("utf-8")))
    if received['code'] == "msg_resp":
        manage_response(received)

#Send request to pki for getting certificate
def main1():
    client = connect_to_broker("v2_1","192.168.0.4")
    request_certificate(client)

#Receive certificate
def main2():
    client = subscribe_to_broker("v2_2", "127.0.0.1", "/certificate")
    client.on_message = on_certificate_received
    client.loop_forever()

def main3():
    client = subscribe_to_broker("v2_3", "127.0.0.1", "/msg_responses")
    client.on_message = on_message_received
    client.loop_forever()

th1 = threading.Thread(target=main1)
th2 = threading.Thread(target=main2)
th3 = threading.Thread(target=main3)
th1.start()
th2.start()
th3.start()
th1.join()
th2.join()
th3.join()