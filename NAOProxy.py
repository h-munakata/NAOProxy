# -*- coding: utf-8 -*-
from naoqi import ALProxy
import socket 
import utils


# buffer_size = 1024
# while 1:
#     json_massage = client.recv(buffer_size)
#     print json_massage



class NAOProxy:
    def __init__(self, ip_NAO, port_NAO, ip_server, port_server):
        self.ip_NAO = ip_NAO
        self.port_NAO = port_NAO

        self.ip_server = ip_server
        self.port_server = port_server

        self.init_server()


    def init_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip_server, self.port_server))
        self.sock.listen(1)
        self.sock.settimeout(100)
        self.controller, self.address_server = self.sock.accept()
        print('connect to controller, IP:{}, port:{}'.format(self.address_server[0], self.address_server[1]))

    
    def connect_NAO(self):
        self.audioProxy = ALProxy("ALTextToSpeech",self.IP_NAO, self.port_NAO)

    
    def wait_massage(self,buffer_size):
        while 1:
            status = self.sock.connect_ex(self.address_server)
            json_massage = self.controller.recv(buffer_size)
            print(json_massage)


    def say_NAO(self, text):
        self.audioProxy.post.say(text)


ip_NAO = "100.86.6.156"
port_NAO=9559
ip_server = "100.86.6.60"
port_server = 8008

nao_proxy = NAOProxy(ip_NAO=ip_NAO, port_NAO=port_NAO, ip_server=ip_server, port_server=port_server)
nao_proxy.wait_massage(buffer_size=1024)