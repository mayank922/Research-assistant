
import os
import json

def save_session(history, filename):
    json_filename = filename + '.json'
    final_path = os.path.join('session' , json_filename)
    os.makedirs('session' , exist_ok=True)
    

# Creates json file
# Writes json data as returned by history function in converstaion class
    with open(final_path , 'w') as f :
        json.dump(history.get_messages(), f)



def load_session(filename):
    final_path = os.path.join('session/', filename + '.json')
    print(final_path)
    try:
        with open(final_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Session {filename} not found")
        return None










