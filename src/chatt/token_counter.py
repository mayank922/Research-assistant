import tiktoken

def count_tokens(messages,model) -> int:

    encoding = tiktoken.get_encoding('cl100k_base')
    no_of_tokens = 0
    for i in messages:
        no_of_tokens += len(encoding.encode(i["content"]))
    
    return no_of_tokens 