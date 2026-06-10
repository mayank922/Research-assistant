from config import OLLAMA_BASE_URL , MODEL_NAME
import requests
import json
import time


API_chat_URL = OLLAMA_BASE_URL + "/api/chat"


def chat(messages:list) -> str:
    request_body = {
        "model": MODEL_NAME,
        "messages" : messages,
        "stream" : False
    }

    try:
        req = requests.post(url=API_chat_URL , data=json.dumps(request_body)) #json.dumps to convert to json

    except requests.ConnectionError:
        print('Ollama is not running. Please start with: ollama serve')
        return
    
    return req.json()['message']['content']

"""
Stream provides output one by by using yield, so we dont have to wait for complete respononse but see it in real time
"""

def stream_chat(messages:list) ->str:
    request_body = {
        "model": MODEL_NAME,
        "messages" : messages,
        "stream" : True
    }
    
    try:
        req = requests.post(url=API_chat_URL , json = request_body, stream=True)
    
    except requests.ConnectionError:
        print('Ollama is not running. Please start with: ollama serve')
        return

    for lines in req.iter_lines():
        parsed = json.loads(lines)
        content = parsed['message']['content']
        if parsed["done"]:
            break
        else:
            yield content

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