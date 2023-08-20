import os
import openai
import tkinter as tk
from dotenv import load_dotenv, find_dotenv
from chatbot import get_completion_from_messages
from gui import create_gui

# Load environment variables from .env file
load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize conversation history
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

# Create the GUI
root = tk.Tk()
create_gui(root, conversation, get_completion_from_messages)
root.mainloop()

