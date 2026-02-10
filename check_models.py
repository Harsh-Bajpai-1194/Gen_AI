import google.generativeai as genai
import os

# Paste your API key here again
API_KEY = "AIzaSyBcssvdo5SZjWE_b6G5rlU4O8cz3RQgTWg"
genai.configure(api_key=API_KEY)

print("Listing available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)