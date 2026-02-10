import google.generativeai as genai
import os

# 1. SETUP: Put your API Key here
# Get one for free at: https://aistudio.google.com/app/apikey
API_KEY = "AIzaSyBcssvdo5SZjWE_b6G5rlU4O8cz3RQgTWg"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-flash-latest')

# 3. START CHAT: This history list keeps track of the conversation
chat = model.start_chat(history=[])

print("AI: Hello Harsh! I am ready. Type 'exit' to stop.")

# 4. THE LOOP: This keeps the conversation going
while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break
    
    # Send message to AI and print response
    response = chat.send_message(user_input)
    print(f"AI: {response.text}")