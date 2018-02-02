from slackclient import SlackClient
import time

class Bot:
    
    def __init__(self, token):
        self.slack_client = SlackClient(token)
        self.bot_id = self.get_bot_id()
        
    
    def get_bot_id(self):
        
        users = self.slack_client.api_call("users.list")["members"]
        
        for user in users:
            if user['name'] == 'sallybot':
                return ("<@%s>" % user['id'])
        
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
                self.respond(event)
    
    def respond(self, event):
        
        if event['type'] == 'message':
            if self.bot_id in event['text']:
                self.slack_client.api_call("chat.postMessage",
                                           channel=event['channel'],
                                           text='meow!',
                                           as_user=True)
