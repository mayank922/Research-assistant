from src.chatt.ollama_client import stream_chat, check_ollama, chat
from rich.console import Console
from src.chatt.conversation import ConversationHistory
from config import SYSTEM_PROMPT, MODEL_NAME
from src.utils.session import load_session , save_session
from src.utils.logger import log_qa
import os
from datetime import datetime
from rich.progress import Progress, BarColumn, TextColumn
from rich.text import Text
from rich.panel import Panel

console = Console()

history = ConversationHistory()

def conversation():

    if not check_ollama():
        return
    
    show_splash()

    while(True):
        show_token_bar(history)
        user_input = console.input("[bold green]You: [/bold green]")
        if(user_input == "/quit"):
            console.print("[dim]Goodbye![/dim]")
            break

        elif user_input == "/clear":
            history.clear()
            history.add('system', SYSTEM_PROMPT)
            console.print("[dim]History cleared![/dim]\n")
            continue

        elif user_input == "/save":
            session_name = console.input("[dim]Enter session name: [/dim]")
            save_session(history, session_name)
            console.print(f"[dim]Session '{session_name}' saved![/dim]\n")
            continue
        
        elif user_input == "/load":
            session_name = console.input("[dim]Enter session name to load: [/dim]")
            loaded_messages = load_session(session_name)
            if loaded_messages is not None:
                history.messages = loaded_messages
                console.print(f"[dim]Session '{session_name}' loaded![/dim]\n")
                console.print(f"[dim]Loaded {len(history.messages)} messages[/dim]")
            continue
        
        elif user_input == "/export":
            os.makedirs('logs', exist_ok=True)
            export_file = f"logs/export_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            with open(export_file, 'w') as f:
                for msg in history.get_messages()[1:]:  # skip system prompt
                    f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
            console.print(f"[dim]Exported to {export_file}[/dim]\n")
            continue

       
        # message = {"role":"user" , "content" : user_input}
        #chat_history.append(message)
        history.add('user' , user_input)
        console.print(f"\n[bold blue]Assistant:[/bold blue]", end = "")

        full_response = ""
        for chunk in stream_chat(messages=history.get_messages()):
            print(chunk , end="" , flush=True)
            full_response+=chunk
            
        print("\n")
            
        history.add('assistant', full_response)
        log_qa(user_input, full_response) #logging reponse
        history.trim_to_limit()



def show_token_bar(history, max_tokens=3000):
    used = history.token_count()
    percentage = used / max_tokens
    color = "green" if percentage < 0.7 else "yellow" if percentage < 0.9 else "red"
    console.print(f"[dim]Tokens: [{color}]{used}[/{color}]/{max_tokens}[/dim]")

def show_splash():
    content = Text()
    content.append("Model: ", style="dim")
    content.append(f"{MODEL_NAME}\n", style="bold cyan")
    content.append("Token Budget: ", style="dim")
    content.append("3000\n", style="bold cyan")
    content.append("\nCommands: ", style="dim")
    content.append("/save /load /clear /history /export /quit", style="bold green")
    
    console.print(Panel(
        content,
        title="[bold cyan]🔐 Cybersecurity Research Assistant[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    ))

if __name__ == "__main__":
    conversation()

