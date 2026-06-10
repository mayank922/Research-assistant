from src.chatt.conversation import ConversationHistory

def test_add_message():
    history = ConversationHistory()
    history.add('user', 'hello')
    messages = history.get_messages()
    assert messages[-1]['content'] == 'hello'
    assert messages[-1]['role'] == 'user'

def test_clear():
    history = ConversationHistory()
    history.add('user', 'hello')
    history.clear()
    history.add('system', 'test prompt')
    assert len(history.get_messages()) == 1

def test_trim():
    history = ConversationHistory()
    for i in range(50):
        history.add('user', 'x' * 100)
        history.add('assistant', 'y' * 100)
    history.trim_to_limit(max_tokens=3000)
    assert history.token_count() <= 3000

def test_token_count():
    history = ConversationHistory()
    history.add('user', 'hello')
    assert history.token_count() > 0