# Lahore Orange Line Chatbot

## 📜 Project Description

This chatbot assists passengers of the **Lahore Orange Line Train** with a variety of tasks, including:
- Providing **ticketing** information.
- Answering questions about **train schedules**.
- Offering information about **stations** along the route.
- Giving **general travel advice**.

It is built using **Gradio**, an interactive Python library for creating UIs, and is powered by **Groq's API** to handle chat interactions.

---

## 🚀 How to Run the Chatbot Locally

1. **Clone the repository**:
   ```bash
   git clone https://huggingface.co/spaces/your-space-name
🛠️ Tech Stack
Component	Purpose
Gradio	Interactive UI and chat history management
Groq API	NLP responses and intelligent answer generation
Python	Core logic and API handling
📝 Architecture
User Query: Inputs question (e.g., "Next train timing?")

System Prompt: Defines chatbot's travel-assistant role

API Interaction: Queries Groq with user input

Response: Displays API-generated answer in UI

💡 UI Features
Topic Dropdown: Pre-select categories (Ticketing, Schedules, etc.)

Persistent Chat History: Continuous conversation tracking

Clear Chat Button: Conversation reset option

🔑 API Setup
Obtain key from Groq Console

Configure either:

Environment variable: GROQ_API_KEY

Hugging Face Secrets (for Spaces deployment)

🚀 Deployment (Hugging Face)
Create new Gradio Space

Upload:

app.py

requirements.txt

Add API key in Settings > Secrets

Deploy!

📋 Roadmap
Enhanced station details

Improved NLP accuracy

Real-time schedule integration

Delay notifications

🔗 Resources
Hugging Face Space

Groq API Documentation
