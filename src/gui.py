# import tkinter as tk

# def create_gui(root, conversation, chatbot_function):
#     text_widget = tk.Text(root)
#     text_widget.pack()

#     entry_widget = tk.Entry(root)
#     entry_widget.pack()

#     def send_message():
#         user_input = entry_widget.get()
#         conversation.append({"role": "user", "content": user_input})
#         bot_response = chatbot_function(conversation)
#         conversation.append({"role": "assistant", "content": bot_response})
#         text_widget.insert(tk.END, f"You: {user_input}\nBot: {bot_response}\n")
#         entry_widget.delete(0, tk.END)

#     send_button = tk.Button(root, text="Send", command=send_message)
#     send_button.pack()
