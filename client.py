# -*- coding: utf-8 -*-
from naoqi import ALProxy
import socket 
import json
import sys
import time



server_ip = sys.argv[1]
server_port = int(sys.argv[2])
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

try:
    while 1:
        time.sleep(1)
        message = input()
        json_message = json.dumps(message)
        print 'sending message :{}'.format(json_message)

        # send message to proxy
        client_socket.send(json_message)
        # recieve message from proxy
        recieved_message = client_socket.recv(1024)

        if len(recieved_message)==0:
            print "server is closed"
            break
        else:
            print 'recieved_message :{}'.format(recieved_message)

except KeyboardInterrupt:
    client_socket.close()