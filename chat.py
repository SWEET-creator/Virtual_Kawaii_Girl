from openai import OpenAI
import json
import setting

client = OpenAI(
    api_key=setting.open_ai_api_key,
)


def initialize_conversation(file_path="conversation_history.json"):
    """
    Initialize the conversation with a system message if the conversation history is empty.

    :param file_path: The file path where the conversation data is stored.
    :param initial_message: The initial system message to start the conversation.
    """
    # Check if the conversation history exists and is not empty
    try:
        with open(file_path, "r") as file:
            conversations = json.load(file)
        if not conversations:  # If the conversation history is empty
            raise FileNotFoundError  # Proceed to initialize
    except FileNotFoundError:
        # Initialize the conversation with a system message
        with open("init_prompt.txt", "r", encoding="utf-8") as file:
            init_prompt = file.read()
        conversations = [{
            "role": "system",
            "content": init_prompt,
        }]
        with open(file_path, "w") as file:
            json.dump(conversations, file)

def save_conversation(conversations, file_path="conversation_history.json"):
    """
    Save conversation history to a file.
    """
    with open(file_path, "w") as file:
        json.dump(conversations, file)

def load_conversation(file_path="conversation_history.json"):
    """
    Load conversation history from a file.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist.

def set_emotion(emotion, file_path="conversation_history.json"):
    conversations = [{
        "role": "system",
        "content": "あなたは" + emotion + "な感情で振る舞ってください．",
    }]
    with open(file_path, "w") as file:
        json.dump(conversations, file)

def chat(content, file_path="conversation_history.json"):
    # Load past conversations
    past_conversations = load_conversation(file_path)

    # Append the new message to the past conversations
    past_conversations.append({
        "role": "user",
        "content": content,
    })

    chat_completion = client.chat.completions.create(
        messages=past_conversations,
        model="gpt-3.5-turbo",
    )
    print(past_conversations)
    outputs = chat_completion.choices[0].message.content

    # Save the updated conversations, including the latest response
    past_conversations.append({
        "role": "system",
        "content": outputs,
    })
    save_conversation(past_conversations, file_path)

    return outputs

def speak(content, file_path="conversation_history.json"):
    # Load past conversations
    past_conversations = load_conversation(file_path)

    # Append the new message to the past conversations
    past_conversations.append({
        "role": "system",
        "content": content,
    })

    chat_completion = client.chat.completions.create(
        messages=past_conversations,
        model="gpt-3.5-turbo",
    )
    print(past_conversations)
    outputs = chat_completion.choices[0].message.content

    # Save the updated conversations, including the latest response
    past_conversations.append({
        "role": "system",
        "content": outputs,
    })
    save_conversation(past_conversations, file_path)

    return outputs

if __name__ == "__main__":
    initialize_conversation()  # Ensure the conversation is initialized
    print(chat("hello"))
