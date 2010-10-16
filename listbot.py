#!/usr/bin/python
'''
File: listbot.py
Author: Sigurd Fosseng
Licence: MIT Licence
Description: Simple bot that says everything it gets through xmlrpc to the
channel
'''
from twisted.words.protocols import irc
from twisted.web import xmlrpc, server
from twisted.internet.protocol import ReconnectingClientFactory


class RustBot(irc.IRCClient):
    nickname = "botname"
    channel = "#support"
    instance = None
   
    def signedOn(self):
        self.factory.instance = self
        self.join(self.channel)
        print "signed on"
   
    def joined(self, channel):
        print "Joined %s" % channel
   
    def say_channel(self, message):
        self.say(self.channel, message)

class Remote(xmlrpc.XMLRPC):
    def xmlrpc_say(self, message):
        if factory.instance:
            factory.instance.say_channel(message.encode("utf-8"))
            return True
        else:
            return False

if __name__ == '__main__':
    factory = ReconnectingClientFactory()
    factory.protocol = RustBot
   
    r = Remote()
   
    from twisted.internet import reactor
    reactor.connectTCP('irc.homelien.no',6667,factory)
    reactor.listenTCP(5656, server.Site(r), interface="127.0.0.1")
    reactor.run()
