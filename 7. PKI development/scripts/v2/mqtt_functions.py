import json
import paho.mqtt.client as mqtt

def connect_to_broker(name_client, ip_broker):
    client = mqtt.Client(name_client)
    client.connect(ip_broker,1883,60)
    return client

def subscribe_to_broker(name_client, ip_broker, path):
    client = mqtt.Client(name_client)
    client.connect(ip_broker,1883,60)
    client.subscribe(path)
    return client

def send_cert_request(client,code, name, ip_source, path, data):
    msg = {"code":code,"name":name,"ip":ip_source,"data":data}
    client.publish(path, json.dumps(msg))

def send_msg_request(client, code, name, ip_destination, ip_source, path, certificate, pub_key, msg):
    msg = {"code":code,"name":name, "ip_d":ip_destination,"ip_s":ip_source,"cert":certificate,"pub_key":pub_key,"msg":msg}
    client.publish(path, json.dumps(msg))