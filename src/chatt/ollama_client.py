from config import OLLAMA_BASE_URL , MODEL_NAME
import requests
import json
import time
from src.tools.registry import TOOLS
from typing import Union


API_chat_URL = OLLAMA_BASE_URL + "/api/chat"


def chat(messages:list) -> Union[str, dict]:
    request_body = {
        "model": MODEL_NAME,
        "messages" : messages,
        "stream" : False,
        "tools" : TOOLS
    }

    try:
        req = requests.post(url=API_chat_URL , data=json.dumps(request_body)) #json.dumps to convert to json

    except requests.ConnectionError:
        print('Ollama is not running. Please start with: ollama serve')
        return
    
    if( "tool_calls" in req.json()['message'] and req.json()['message']["tool_calls"]):
        return req.json()['message']
    else:    
        return req.json()['message']['content']

"""
Stream provides output one by by using yield, so we dont have to wait for complete respononse but see it in real time
"""

def stream_chat(messages:list) ->str:
    request_body = {
        "model": MODEL_NAME,
        "messages" : messages,
        "stream" : True,
        "tools" : TOOLS
    }
    
    try:
        req = requests.post(url=API_chat_URL , json = request_body, stream=True)
    
    except requests.ConnectionError:
        print('Ollama is not running. Please start with: ollama serve')
        return

    for lines in req.iter_lines():
        
        if lines:
            parsed = json.loads(lines)
        
        message = parsed.get("message", {})
        
        # if tool call detected, yield it as special marker and stop
        if "tool_calls" in message and message["tool_calls"]:
            yield {"tool_calls": message["tool_calls"]}
            return
            
        # returns normal chunks
        content = message.get("content", "")
        if content:
            yield content
            
        if parsed.get("done"):
            break
        

def check_ollama(): #Provides a helpful msg to the user if Ollama is not running
    try:
        response = requests.get(OLLAMA_BASE_URL)
        if response.status_code == 200:
            print(f"Ollama is running — {MODEL_NAME} ready \n")
            return True
    except requests.ConnectionError:
        print(f"✗ Cannot connect to Ollama at {OLLAMA_BASE_URL}")
        print(f"Run: ollama serve")
        print(f"Run: ollama pull {MODEL_NAME}")
        return False

def retry_chat(messages, retries=3, backoff=2.0): #Function to wait few seconds to send req again to the server
    for attempt in range(retries):
        try:
            return chat(messages)
        except requests.ConnectionError:
            if attempt < retries - 1:
                print(f'Retrying in {backoff} seconds... (attempt {attempt + 1}/{retries})')
                time.sleep(backoff)
                backoff *= 2
            else:
                print(f'Failed after {retries} attempts. Is Ollama running?')
                return None

if __name__ == "__main__":
    user_message = str(input("What do you want to chat about? "))
    message = [{"role":"user" , "content" : user_message}]
    print(chat(messages=message))