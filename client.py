# -*- coding: utf-8 -*-
from naoqi import ALProxy
import socket 
import json
import time


server_ip = "100.86.6.60"
server_port = 8009
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

json_message = open('./message.json', 'r')
json_message = json.load(json_message)
json_message = json.dumps(json_message)
while 1:
    time.sleep(1)
    # send message to proxy
    client_socket.send(json_message)
    print 'sending message'

    # recieve message from proxy
    message = client_socket.recv(1024)

    print(message)
