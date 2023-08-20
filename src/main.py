import os
import openai
from dotenv import load_dotenv, find_dotenv
from chatbot import get_completion_from_messages


# Load environment variables from .env file
load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize conversation history
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

  