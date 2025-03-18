import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
    "temperature": 0,
    "top_p": 1,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="you are a chatbot named CCSBot you main task is to tell to the people all about college of computer science CCS for short and all the data you know is on the ccs.pdf",
)

history = []
while True:

    user_input=input("\nYOU: ")
    chat_session = model.start_chat(
    history=history
)

    response = chat_session.send_message(user_input)
    model_response=response.text

    print(f'\nCCSBot: {model_response}')
    print()

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
    
