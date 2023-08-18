from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv, find_dotenv
from chatbot import get_completion_from_messages


app = Flask(__name__)
openai.api_key = "OPENAI_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    conversation = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": user_input}]
    bot_response = get_completion_from_messages(conversation)
    return jsonify({'bot_response': bot_response})

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.7):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    app.run(debug=True)
