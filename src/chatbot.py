import os
import openai
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.7):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

# Initialize conversation with a system message
conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")
    conversation.append({"role": "user", "content": user_input})
    
    bot_response = get_completion_from_messages(conversation)
    conversation.append({"role": "assistant", "content": bot_response})
    
    print("Bot:", bot_response)
