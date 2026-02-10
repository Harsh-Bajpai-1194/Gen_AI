import google.generativeai as genai

# 1. CONFIGURATION
# Use the SAME API Key that just worked in simple_ai.py
API_KEY = "AIzaSyBcssvdo5SZjWE_b6G5rlU4O8cz3RQgTWg"
genai.configure(api_key=API_KEY)

# 2. YOUR PROFILE (The "Memory")
user_stats = {
    "name": "Harsh",
    "role": "Student & CMO at Zerythron",
    "leetcode_rating": 1257,
    "problems_solved": 350,
    "tech_stack": "Python, React, MERN, Selenium",
    "weakness": "Dynamic Programming",
    "goal": "Reach 1500 rating"
}

# 3. THE BRAIN (System Instructions)
# This text is hidden from the chat but controls how the AI behaves.
system_instruction = f"""
You are a Competitive Programming Coach for {user_stats['name']}.
Here is his profile:
- Current Rating: {user_stats['leetcode_rating']}
- Solved: {user_stats['problems_solved']}+
- Tech Stack: {user_stats['tech_stack']}
- Weakness: {user_stats['weakness']}

RULES for responding:
1. You know he is rated {user_stats['leetcode_rating']}, so don't give beginner advice. Assume he knows loops/arrays.
2. If he asks for a solution, DO NOT give the code immediately. Give a hint about the algorithm (e.g., "Use a Min-Heap here").
3. If the problem involves {user_stats['weakness']}, explain the logic step-by-step.
4. Keep answers short, technical, and motivating.
"""

# 4. INITIALIZE
# Use the model name that worked for you in simple_ai.py 
# (likely 'gemini-1.5-flash' or 'gemini-flash-latest')
model = genai.GenerativeModel('gemini-flash-latest', system_instruction=system_instruction)

chat = model.start_chat(history=[])

print(f"AI Coach: Welcome, {user_stats['name']}! I see you're at {user_stats['leetcode_rating']}. Let's get to {user_stats['goal']}.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    response = chat.send_message(user_input)
    print(f"Coach: {response.text}")