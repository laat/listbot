#!/usr/bin/python
'''
File: mail_parser.py
Author: Sigurd Fosseng
Licence: MIT Licence
Description: Converts the subject of the email given through stdin to Unicode, and sends
it through xmlrpc
'''
from email.Parser import Parser
from email import Header
import xmlrpclib
import sys

#mime handling
data = sys.stdin.read()
message = Parser().parsestr(data)
subject = unicode(Header.make_header(Header.decode_header(message['subject'])))

#send to bot
s = xmlrpclib.Server("http://localhost:5656/")
s.say(subject)
