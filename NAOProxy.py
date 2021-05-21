from naoqi import ALProxy

audioProxy = ALProxy("ALTextToSpeech","100.86.6.156", 9559)
audioProxy.post.say("I am hanakusomaru") 