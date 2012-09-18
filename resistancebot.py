"""
A Skype Bot that monitors a game of The Resistance

Built on top of Jordan Sherer's chatbot (https://bitbucket.org/widefido/chatbot)
"""

import Skype4Py
import time

import parse
import dispatch


class Bot(object):
    def __init__(self, name="resistancebot", send_announcements=False):
        self.skype = None
        self.name = name
        self.send_announcements = send_announcements
        self.count = 0
       
    def connect_and_listen(self):
        self.skype = Skype4Py.Skype()
        self.skype.Attach()
        self.skype.OnMessageStatus = self.message_status
        
        self.announce("ChatBot Ready...")
        
        try:
            while self.skype.AttachmentStatus == Skype4Py.apiAttachSuccess:
                time.sleep(10)
        except KeyboardInterrupt:
            self.announce("Signing off. Goodbye!")
            print
    
    
    def get_name(self):
        name = self.name
        if self.is_attached():
            user = self.skype.CurrentUser
            name = user.DisplayName
            if not name:
                name = user.FullName
        return name.lower()

        
    def is_attached(self):
        return self.skype.AttachmentStatus == Skype4Py.apiAttachSuccess

        
    def announce(self, message, force=False):
        print message
        if not self.is_attached() or (not force and not self.send_announcements):
            return
        for chat in self.skype.Chats:
            chat.SendMessage(message)
    
    
    def added_to_chat(self, chat):
        chat.SendMessage("Hello!")
    
    
    def message_status(self, message, status):
        # Dispatch all messages
        if status == Skype4Py.cmsReceived:
            self.message_received(message)
        
        # Dispatch everytime chatbot is added to a chat
        if message.Type == Skype4Py.cmeAddedMembers:
            for user in message.Users:
                if user.Handle == self.skype.CurrentUser.Handle:
                    self.added_to_chat(message.Chat)
                    return


    def message_received(self, message):
        try:
            result = self.process_command(message)
            
        except Exception, e:
            import traceback
            result = "Error: {0}".format(e)
            print result
            traceback.print_exc()
            
        if result:
            self.send_reply(message, result)
    
    
    def send_reply(self, message, result):
        message.Chat.SendMessage(result)
        
    
    def process_command(self, message):
        command_string = message.Body.strip()

        command_string = command_string.strip()
        
        command, arguments = parse.parse_command(command_string)

        return self.dispatch_command(command, arguments, message=message, bot=self)
    

    def dispatch_command(self, command, *args, **kwargs):

        return dispatch.dispatch_to_handlers(command, *args, **kwargs)

def main():
    bot = Bot()
    bot.connect_and_listen()

if __name__ == "__main__":
        main()