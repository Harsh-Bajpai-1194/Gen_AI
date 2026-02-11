import streamlit as st
import google.generativeai as genai
import time

# 1. SETUP & PROFILE (From your coach.py)
API_KEY = "AIzaSyBcssvdo5SZjWE_b6G5rlU4O8cz3RQgTWg"
genai.configure(api_key=API_KEY)

user_stats = {
    "name": "Harsh",
    "role": "Student & CMO at Zerythron",
    "leetcode_rating": 1257,
    "tech_stack": "Python, React, MERN, Selenium",
    "weakness": "Dynamic Programming",
    "goal": "Reach 1500 rating"
}

system_instruction = f"""
You are a Competitive Programming Coach for {user_stats['name']}.
Profile: {user_stats['leetcode_rating']} rating, focuses on {user_stats['tech_stack']}.
Rules: Assume high technical knowledge. Give hints before code. 
Focus on his goal: {user_stats['goal']}.
"""

# 2. INITIALIZE MODEL
if "chat" not in st.session_state:
    model = genai.GenerativeModel('gemini-flash-latest', system_instruction=system_instruction)
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []

# 3. UI LAYOUT
st.set_page_config(page_title="Gen AI Coach", page_icon="🤖")
st.title("🚀 GEN_AI Coach")
st.caption(f"Target: {user_stats['goal']} | Current: {user_stats['leetcode_rating']}")

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. CHAT LOGIC
if prompt := st.chat_input("Ask about a LeetCode problem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Call the actual Gemini API
        response = st.session_state.chat.send_message(prompt)
        full_response = response.text
        
        # Clean typing effect
        displayed_text = ""
        for char in full_response:
            displayed_text += char
            message_placeholder.markdown(displayed_text + "▌")
            time.sleep(0.005)
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})