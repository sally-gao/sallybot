import os

class Message:
    
    def __init__(self, event):
        self.user = event['user']
        self.channel = event['channel']
        self.text = event['text']
        self.bot_uid = os.environ.get('bot_uid')
        
    def get_response(self):
        
        # if bot is user, ignore
        if (self.user==self.bot_uid):
            return "do nothing"
        
        # else parse message text
        else:
            return self.parse_text()
    
        
    def parse_text(self):
        
        # if not DM and not mentioned, return "do nothing"
        if not(self.channel[0]=='D') and not(("<@%s>" % self.bot_id) in self.text):
            return "do nothing"
        
        elif "say meow" in self.text:
            return "say meow"
        
        elif self.text.lower().startswith(('hi','hey','hello','howdy','sup')):
            return "say hi"
        
        else:
            return "random message"

        
    
    