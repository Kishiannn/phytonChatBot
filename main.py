'''
NOT YET FINISH

import os
import google.generativeai as genai  

# Configure API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Initialize the Model
model = genai.GenerativeModel("gemini-2.0-flash")

def generate(prompt):
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
    )
    return response.text  # ✅ Fixed indentation

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("CCSBot: Goodbye!")
            break

        response = generate(user_input)
        print("CCSBot:", response)

'''
