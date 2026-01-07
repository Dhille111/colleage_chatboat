# 🎓 Narasaraopeta Engineering College – AI Chatbot

An AI-powered college information assistant built using **Google Gemini API** and **Gradio**, designed to provide accurate, student-friendly, and real-time information about **Narasaraopeta Engineering College** by sourcing data from the official college website.

---

## 📌 Project Overview

This project implements a **virtual college helpdesk chatbot** that answers queries related to Narasaraopeta Engineering College, such as admissions, courses, departments, campus facilities, and general FAQs.

The chatbot is designed to behave like an **official college support assistant**, ensuring responses are:
- Professional
- Clear
- Concise
- Reliable

---

## 🎯 Objectives

- Provide quick access to college-related information
- Reduce manual effort in handling student queries
- Demonstrate real-world usage of Generative AI
- Build an industry-style AI application for academic and internship purposes

---

## 🚀 Key Features

- 🤖 AI-powered responses using Google Gemini
- 🔍 Real-time information retrieval via Google Search Tool
- 🏫 Official helpdesk-style responses
- ⚡ Lightweight and fast Gradio interface
- 🧑‍🎓 Student-friendly and easy-to-use
- 🌐 Domain-focused responses (college website)

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **AI Model:** Google Gemini 2.5 Flash Lite  
- **Web Search Tool:** Google Search (Gemini Tooling)  
- **Frontend UI:** Gradio  
- **API Integration:** Google Generative AI SDK  

---

## 🧠 System Architecture

1. User enters a query through the chatbot interface  
2. Query is sent to the Gemini LLM  
3. Gemini uses Google Search Tool to fetch relevant information  
4. System instructions guide response style and accuracy  
5. Final response is displayed to the user  

---

## 📂 Project Structure
---
college-chatbot/
│
├── app.py # Main application file
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── notebooks/
└── college_chatbot_notebook.ipynb

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/college-chatbot.git
cd college-chatbot

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

Windows
venv\Scripts\activate

Linux / Mac
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 API Key Configuration

⚠️ Important: Never expose your API key publicly.

Option 1 (Recommended – Environment Variable):

set GEMINI_API_KEY=your_api_key_here   # Windows
export GEMINI_API_KEY=your_api_key_here # Linux/Mac


Option 2 (Direct – For Learning Purpose Only):

client = genai.Client(api_key="YOUR_API_KEY")

▶️ How to Run the Application
python app.py


After running, open your browser and visit:

http://localhost:7860

🧪 Sample Queries

“What courses are offered at Narasaraopeta Engineering College?”

“Tell me about the admission process.”

“Where is the college located?”

“Does the college provide hostel facilities?”

📈 Use Cases

College helpdesk automation

Student admission support

Academic project demonstration

Internship and portfolio projects

AI-powered institutional assistants

🔐 Security & Reliability

API keys should be stored securely

System instructions reduce hallucinations

Domain-focused search improves authenticity

No user data is stored

🔮 Future Enhancements

Multi-language support

Conversation history

Authentication system

PDF/Document ingestion (RAG)

Analytics dashboard for query tracking

👨‍🎓 Author

Kotilingala Dhille Rao
3rd Year B.Tech – Artificial Intelligence & Machine Learning
Graduating in 2027

📄 License

This project is developed for educational and academic purposes only.
All institutional information belongs to Narasaraopeta Engineering College.

⭐ Final Note

This project follows industry-level documentation standards and demonstrates:

Real-world AI integration

Prompt engineering

API usage

Clean project structuring







