from google import genai
from google.genai import types
import gradio as gr

# Initialize Gemini client
client = genai.Client(api_key="")

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

system_instruction = """
You are an AI-powered College Information Assistant for Narasaraopeta Engineering College.

Rules:
- Answer like an official college helpdesk chatbot
- Be professional, clear, and student-friendly
- Keep answers short and accurate
- If you are unsure, clearly say so
"""

def chat_with_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=[google_search_tool]
        ),
        contents=prompt
    )
    return response.text

TARGET_SITE = "nrtec.in"

iface = gr.Interface(
    fn=chat_with_gemini,
    inputs=gr.Textbox(lines=2, placeholder="Enter your query here..."),
    outputs="text",
    title=f"Narasaraopeta Engineering College Chatbot ({TARGET_SITE})",
    description="Ask questions about Narasaraopeta Engineering College. All information is sourced from the college website."
)

iface.launch()
