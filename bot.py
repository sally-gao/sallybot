from slackclient import SlackClient
import time
import random
import os
import message

class Bot:
    
    def __init__(self, token):
        self.slack_client = SlackClient(token)
        self.bot_uid = os.environ.get('bot_uid')
        self.random_messages = self.get_messages('random_messages.txt')
        self.events = []
        
    
    def get_messages(self, filepath):
        with open(filepath) as file:     
            msgs = tuple(line.strip() for line in file.readlines())
            
        return msgs
    
    def listen(self):
        if self.slack_client.rtm_connect(with_team_state=False):
            while True:
                self.wait()
                 
                time.sleep(1)
        else:
            exit("Connection failed")
    
    def wait(self):
        events = self.slack_client.rtm_read()
        
        if events and len(events) > 0:
            for event in events:
                if event['type']=='message':
                    self.log(event)
                    self.respond(event)
    
    def log(self, event):
        self.slack_client.api_call("chat.postMessage",
                                   channel="D92M6HY8H",
                                   text=str(event),
                                   as_user=True)
    
    def respond(self, event):
        
        msg = message.Message(event)
        response = msg.get_response()
        
        if response=="do nothing":
            pass
        
        elif response=="random message":
            self.random_message(msg)
        
        elif response=="say meow":
            self.say_meow(msg)
    
    
    def random_message(self, msg):
        self.slack_client.api_call("chat.postMessage",
                                   channel=msg.channel,
                                   text=random.choice(self.random_messages),
                                   as_user=True)
    
    def say_meow(self, msg):
        self.slack_client.api_call("chat.postMessage",
                                   channel=msg.channel,
                                   text='meow!',
                                   as_user=True)
        

