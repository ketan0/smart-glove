#!/usr/bin/env python3
import os

from fbchat import Client
from fbchat.models import *

ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
client = Client(os.environ['FB_EMAIL'], os.environ['FB_PASSWORD'], user_agent=ua)

def send_message(text, thread_id):
    client.send(Message(text=text), thread_id=thread_id)

def send_message_self(text):
    client.send(Message(text=text), thread_id=client.uid)
