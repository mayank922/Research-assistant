from config import SYSTEM_PROMPT
from src.chatt.token_counter import count_tokens

class ConversationHistory:

    def __init__(self):
        self.messages = [] #List to maintain the converstation in dict
        self.add(role='system' , content=SYSTEM_PROMPT) #Intializes already with the role of the agent

    def add(self,role,content):
        msg = {'role' : role , 'content' : content}
        self.messages.append(msg)

    def get_messages(self):
        return self.messages
    
    def clear(self):
        self.messages = []

    def token_count(self):
        return count_tokens(self.messages, None)

        # content_counter = 0
        # for i in self.messages:
        #     content_counter = content_counter + len(i['content'])
        
        # return content_counter

    def trim_to_limit(self , max_tokens=3000): #maintains context window

        while self.token_count() > max_tokens and len(self.messages) > 1:
            self.messages.pop(1)
        # if(self.token_count() < max_tokens):
        #     return
        
        # while(self.token_count() > max_tokens):
        #     self.messages.pop(1)
        



    

    

    