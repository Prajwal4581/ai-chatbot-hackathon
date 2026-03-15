# 🤖 AI Chatbot — Hackathon Project

A conversational AI chatbot powered by **Groq's ultra-fast LLaMA3 inference API**, built with a clean **Streamlit** interface. Developed as part of a hackathon with a focus on speed, simplicity, and real-time AI responses.

---

## ✨ Features

- 💬 Real-time conversational AI using LLaMA3
- ⚡ Ultra-fast responses via Groq inference engine
- 🧠 Multi-turn conversation with chat history
- 🖥️ Clean and minimal Streamlit web interface
- 🔌 Easy to run locally with minimal setup

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| AI Model | LLaMA3 (via Groq API) |
| Backend | Python |
| API Client | Groq Python SDK |

---

## 📂 Project Structure

```
ai-chatbot-hackathon/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores API keys and env files
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Prajwal4581/ai-chatbot-hackathon.git
cd ai-chatbot-hackathon
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your Groq API Key

Get your free API key from [console.groq.com](https://console.groq.com)

Create a `.env` file in the root:
```
GROQ_API_KEY=your_api_key_here
```

Or set it directly as an environment variable:
```bash
export GROQ_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

App will open at `http://localhost:8501`

---

## 🖥️ How It Works

1. User types a message in the Streamlit chat input
2. The message is sent to Groq's API with the full conversation history
3. LLaMA3 generates a response at blazing-fast speed
4. Response is streamed back and displayed in the chat UI
5. Conversation history is maintained for context-aware replies

---

## 🚀 Why Groq?

Groq's inference engine is significantly faster than standard GPU-based inference. For a hackathon demo where response speed matters, Groq delivers near-instant replies — making the chatbot feel genuinely responsive rather than laggy.

---

## 📌 Future Improvements

- [ ] Add system prompt customization
- [ ] Support multiple LLM model selection (Mixtral, Gemma, etc.)
- [ ] Deploy on Streamlit Cloud
- [ ] Add conversation export feature

---

## 👨‍💻 Developer

**Prajwal Santosh Jadhav**  
PG-DAC, Sunbeam Institute | Aug 2025 Batch  
[GitHub](https://github.com/Prajwal4581) · [LinkedIn](https://www.linkedin.com/in/prajwal-jadhav45)

---

> ⚠️ **Note:** Never commit your `GROQ_API_KEY` to the repository. Always use `.env` files or environment variables.
