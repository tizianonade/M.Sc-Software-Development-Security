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