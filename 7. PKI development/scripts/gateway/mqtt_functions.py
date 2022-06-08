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

def send_cert_response(client, code, name, ip_source, path, user_cert, pki_cert, pki_pub_key):
    msg = {"code":code,"name":name,"ip":ip_source,"user_cert":user_cert, "pki_cert":pki_cert, "pki_pub_key":pki_pub_key}
    client.publish(path, json.dumps(msg))

def send_msg_response(client, code, name, ip_destination, ip_source, path, certificate, pub_key, msg):
    msg = {"code":code,"name":name, "ip_d":ip_destination,"ip_s":ip_source,"cert":certificate,"pub_key":pub_key,"msg":msg}
    client.publish(path, json.dumps(msg))