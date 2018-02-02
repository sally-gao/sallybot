from slackclient import SlackClient

class Bot:
    
    def __init__(self, token):
        self.slack_client = SlackClient(token)
    
    