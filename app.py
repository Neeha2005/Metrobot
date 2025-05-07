import gradio as gr
import requests
import os

# You will use Hugging Face Secrets to hide this API key in deployment
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b-8192"

# Customize for Orange Line
SYSTEM_PROMPT = """You are a helpful assistant for Lahore's Orange Line Metro Train. 
You answer questions clearly and concisely about routes, timings, ticket prices, stations, and facilities."""

def query_groq(message, chat_history):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for user, bot in chat_history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    
    messages.append({"role": "user", "content": message})

    response = requests.post(GROQ_API_URL, headers=headers, json={
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.7
    })

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

def respond(message, chat_history):
    reply = query_groq(message, chat_history)
    chat_history.append((message, reply))
    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("## 🚇 Orange Line Metro Assistant")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Ask me anything about Lahore's Orange Line Metro")
    clear = gr.Button("Clear")
    state = gr.State([])

    msg.submit(respond, [msg, state], [msg, chatbot])
    clear.click(lambda: ([], []), None, [chatbot, state])

demo.launch()
import gradio as gr
import os
import requests

# Set your GROQ API Key here (make sure it's correct)
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b-8192"  # This is just an example; adjust it as needed

# Customize this system prompt to reflect your chatbot's role
SYSTEM_PROMPT = """You are a helpful assistant for the Lahore Orange Line Train. 
You assist users with queries related to ticketing, stations, timings, and general travel information."""

# Function to query GROQ API
def query_groq(message, chat_history):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for user, bot in chat_history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": message})

    # Send request to GROQ API
    response = requests.post(GROQ_API_URL, headers=headers, json={
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.6
    })

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

# Function to respond to user messages
def respond(message, topic, chat_history):
    full_message = f"[Topic: {topic}] {message}" if topic else message
    reply = query_groq(full_message, chat_history)
    chat_history.append((message, reply))
    return "", chat_history

# Build the Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🚌 **Lahore Orange Line Chatbot**")
    gr.Markdown("Ask me anything about train routes, tickets, stations, and schedules!")

    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Ask your question")
    topic = gr.Dropdown(["Ticketing", "Train Schedule", "Stations Info", "General Help"], label="Select Topic (Optional)", interactive=True)
    state = gr.State([])

    send_btn = gr.Button("Send")
    clear_btn = gr.Button("Clear Chat")

    send_btn.click(respond, [msg, topic, state], [msg, chatbot])
    msg.submit(respond, [msg, topic, state], [msg, chatbot])
    clear_btn.click(lambda: ([], []), None, [chatbot, state])

demo.launch()
