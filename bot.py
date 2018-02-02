from slackclient import SlackClient
import time
import random

class Bot:
    
    def __init__(self, token):
        self.slack_client = SlackClient(token)
        self.bot_id = self.get_bot_id()
        self.respond_types = ['message']
        self.random_messages = ['purrr', 'meow!', 'hi there!', 'beep beep boop',
                                'am I a sally bot or sally gao? #existentialdilemma']
        
    
    def get_bot_id(self):
        
        users = self.slack_client.api_call("users.list")["members"]
        
        for user in users:
            if user['name'] == 'sallybot':
                return (user['id'])
        
        return None
    
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
                if event['type'] in self.respond_types:
                    self.respond(event)
    
    def respond(self, event):
        
        if event['type'] == 'message':
            
            # if bot is mentioned, respond 'meow!'
            if ("<@%s>" % self.bot_id) in event['text']:
                self.slack_client.api_call("chat.postMessage",
                                           channel=event['channel'],
                                           text='meow!',
                                           as_user=True)
            
        
            # else if bot is DM'd, respond with one of the preset responses:
            elif not(event['user']==self.bot_id) and event['channel'][0]=='D':
                self.slack_client.api_call("chat.postMessage",
                                           channel=event['channel'],
                                           text=random.choice(self.random_messages),
                                           as_user=True)
            
