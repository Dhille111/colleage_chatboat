🎓 Narasaraopeta Engineering College – AI Chatbot

An AI-powered college information assistant built using Google Gemini API and Gradio, designed to provide accurate, real-time information about Narasaraopeta Engineering College by sourcing data directly from the official website.

📌 Project Overview

The Narasaraopeta Engineering College AI Chatbot acts as a virtual helpdesk for students, parents, and visitors.
It answers college-related queries such as:

Admissions information

Courses and departments

Academic schedules

Campus facilities

General college-related FAQs

The chatbot uses Google Gemini (Generative AI) combined with Google Search Tool to ensure reliable and up-to-date responses.

🚀 Key Features

🤖 AI-Powered Responses using Gemini 2.5 Flash Lite

🔍 Real-time Web Search Integration (College website only)

🏫 Official College Helpdesk Tone

⚡ Fast and Lightweight UI with Gradio

🛡️ Controlled Domain Search (nrtec.in)

🧑‍🎓 Student-Friendly & Accurate Answers

🛠️ Tech Stack
Technology	Purpose
Python	Backend logic
Google Gemini API	AI response generation
Google Search Tool	Real-time information retrieval
Gradio	Web-based user interface
LLM Prompt Engineering	Professional response control
🧠 System Architecture

User enters a query in the chatbot UI

Query is sent to the Gemini LLM

Gemini uses Google Search Tool to fetch data

Responses are filtered using system instructions

Final answer is displayed to the user

📂 Project Structure
college-chatbot/
│
├── app.py               # Main application file
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── assets/              # (Optional) screenshots or logos

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/college-chatbot.git
cd college-chatbot

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Environment Configuration

Create a .env file (recommended) and add:

GEMINI_API_KEY=your_api_key_here


⚠️ Never expose your API key in public repositories

▶️ Run the Application
python app.py


The chatbot will be available at:

http://localhost:7860

🧪 Sample Queries

“What courses are offered at Narasaraopeta Engineering College?”

“Tell me about the admission process.”

“Where is the college located?”

“Does the college have hostel facilities?”

📈 Use Cases

College websites

Student helpdesks

Admission support systems

AI-powered institutional assistants

Internship & academic projects

🔐 Security Considerations

API keys should be stored in environment variables

Domain-restricted search ensures data authenticity

System instruction prevents hallucinations

🏆 Future Enhancements

🔐 User authentication

💬 Conversation history

📊 Analytics dashboard

🧾 PDF document ingestion

🌐 Multi-language support

👨‍🎓 Developed By

Kotilingala Dhille Rao
3rd Year B.Tech – AIML
Graduating in 2027

📄 License

This project is developed for educational and academic purposes.
All college information belongs to Narasaraopeta Engineering College.

⭐ Final Note

This project demonstrates real-world AI integration, prompt engineering, and production-style application design, making it suitable for:

Internships

Final-year projects

Resume & GitHub portfolio
