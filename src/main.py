import os
import openai
from dotenv import load_dotenv, find_dotenv
from src.chatbot import get_completion_from_messages  # Updated import path

# Load environment variables from .env file
load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize conversation history
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

  