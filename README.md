# 🔐 Cybersecurity Research Assistant

A personal learning project to master the core structure of AI agents, building a security focused research assistant from scratch, 
deliberately avoiding frameworks first to understand what's happening under the hood.

## Motivation

Most AI agent tutorials start with LangChain or similar frameworks but this project build everything manually first, 
understand the fundamentals, then layer in frameworks at a later stage.

## Current Status

🚧 **Phase 1** — Raw LLM chat with conversation history
🚧 **Phase 2 in progress** — Function Calling/ Tools

## Installation

1. Install Ollama and pull the model
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
```

2. Install dependencies
```bash
pip install requests rich python-dotenv tiktoken
```

3. Create `.env` file
```
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=llama3.2:3b
```

4. Run
```bash
python3 main.py
```

## Commands

| Command | Description |
|---------|-------------|
| `/save` | Save current session |
| `/load` | Load a previous session |
| `/history` | Show last N turns |
| `/export` | Export conversation as .txt |
| `/clear` | Reset history |
| `/quit` | Exit |


## Project Structure

```
research-assistant/
├── main.py              # Entry point, CLI loop
├── config.py            # Constants and configuration
├── prompts.py           # Canned AppSec prompt templates
├── src/
│   ├── chat/
│   │   ├── client.py        # Ollama API client
│   │   └── conversation.py  # History management
│   └── utils/
│       ├── session.py       # Save/load sessions
│       ├── logger.py        # JSONL conversation logging
│       └── token_counter.py # Token counting with tiktoken
└── tests/
    └── test_conversation.py
```