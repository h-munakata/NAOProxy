# -*- coding: utf-8 -*-
from naoqi import ALProxy
import socket 
import utils
import json
import sys


class NAOProxy:
    def __init__(self, ip_NAO, port_NAO, ip_server, port_server, path_json_behavior, send_message=True):
        self.send_message = send_message
        self.ip_NAO = ip_NAO
        self.port_NAO = port_NAO
        self.init_server(ip_server, port_server)
        self.motion = NAO_Motion(ip_NAO, port_NAO, path_json_behavior)

    def init_server(self, ip_server, port_server):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip_server, port_server))
        self.sock.listen(1)
        self.sock.settimeout(100)
        self.client, self.address_server = self.sock.accept()
        print('success to connect to client, IP:{}, port:{}'.format(self.address_server[0], self.address_server[1]))

    
    def wait_message(self,buffer_size=1024):
        json_message = self.client.recv(buffer_size)
        if len(json_message)==0:
            print "connection is lost"
            return False
        return json_message


    def process_message(self):
        try:
            while(1):
                print 'waiting message'
                json_message = self.wait_message()
                if not json_message:
                    print 'disconnect with client'
                    self.disconnect()
                    break
                else:
                    message = json.loads(json_message)
                    self.action(message)
                    print 'recieved message:{}'.format(message)
                    self.send('{"result":"success-end"}')

        except:
            print 'some errors occured'
            self.disconnect()


    def send(self,message):
        if self.send_message:
            self.client.send(message)
        else:
            pass


    def action(self, message):
        action_type, key  = message.items()[0]
        if action_type=="playmotion":
            self.motion.play(key)

    def disconnect(self):
        print "disconected"
        self.sock.close()
        self.motion.exit()




class NAO_Motion:
    def __init__(self, ip_NAO, port_NAO, path_json_behavior):
        json_behavior = open(path_json_behavior,'r')
        behavior = json.load(json_behavior)
        playmotion = behavior["playmotion"]

        proxy = ALProxy("ALMotion", ip_NAO, port_NAO)
        proxy.stiffnessInterpolation("Body", 0.9, 1.0)

        # Refer to ALFrameManager.py
        self.frame = ALProxy("ALFrameManager", ip_NAO, port_NAO)

        self.dict_motion = {}
        
        for key_motion, path_xarfile in playmotion.items():
            print "loading behavior file:{}".format(path_xarfile.encode("UTF-8"))
            self.dict_motion[key_motion] = self.frame.newBehaviorFromFile(path_xarfile.encode("UTF-8"), "")


    def play(self, key_motion):
        self.frame.playBehavior(self.dict_motion[key_motion])

    def exit(self):
        self.frame.cleanBehaviors()


if __name__ == "__main__":
    ip_NAO = sys.argv[1]
    port_NAO = int(sys.argv[2])
    ip_server = sys.argv[3]
    port_server = int(sys.argv[4])
    path_json_behavior = "./behavior.json"

    nao_proxy = NAOProxy(ip_NAO=ip_NAO, port_NAO=port_NAO, 
                            ip_server=ip_server, port_server=port_server,
                            path_json_behavior=path_json_behavior)
    try:
        nao_proxy.process_message()
    except:
        nao_proxy.disconnect()