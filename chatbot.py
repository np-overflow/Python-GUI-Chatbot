import openai
import tkinter as tk
from tkinter import scrolledtext

# Initialize OpenAI client
client = openai.OpenAI(
    base_url="http://localhost:8080/v1",  # Replace with your API server IP and port
    api_key="sk-no-key-required"
)

def send_message():
    user_message = entry.get()
    if user_message.strip() == "":
        return
    
    # Immediately display the user's message
    chat_history.insert(tk.END, "You: " + user_message + "\n")
    chat_history.yview(tk.END)
    entry.delete(0, tk.END)
    
    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
            {"role": "user", "content": user_message}
        ]
    )
    
    bot_message = response.choices[0].message.content
    chat_history.insert(tk.END, "Chatbot: " + bot_message[:-4] + "\n")
    chat_history.yview(tk.END)

# Set up the main window
root = tk.Tk()
root.title("Chatbot Client")

title = tk.Label(root, text="Chatbot Client")
title.pack(padx=10, pady=10)

# Chat history display
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='normal')
chat_history.pack(padx=10, pady=10)

# User message entry
entry = tk.Entry(root, width=60)
entry.pack(padx=10, pady=10, side=tk.LEFT)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.LEFT)

# Start the Tkinter event loop
root.mainloop()
