# -*- coding: utf-8 -*-
from naoqi import ALProxy
import socket 
import json
import time
import argparse


parser = argparse.ArgumentParser(description='Client for NAO Proxy') 

parser.add_argument('ip_server', type=str)
parser.add_argument('port_server', type=int)
args = parser.parse_args()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((args.ip_server, args.port_server))

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