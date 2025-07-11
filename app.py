# app.py – TripPlanner AI: Personalized Travel Itinerary Generator

import streamlit as st
import ollama
from datetime import datetime, timedelta

# --- Step 1: Collect User Preferences ---
def get_user_inputs():
    with st.form("trip_form"):
        destination = st.text_input("🌍 Enter Destination (e.g., Tokyo, Paris)")
        start_date = st.date_input("📅 Start Date")
        end_date = st.date_input("📅 End Date")
        group_type = st.selectbox("👥 Travel Group", ["Solo", "Couple", "Family", "Senior", "Friends"])
        interests = st.multiselect("🎯 Interests", ["Nature", "Adventure", "Culture", "Food", "Shopping", "Relaxation"])
        budget = st.selectbox("💰 Budget Range", ["Economy", "Mid-range", "Luxury"])
        submitted = st.form_submit_button("🧭 Generate Itinerary")

    if submitted:
        return {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "group_type": group_type,
            "interests": interests,
            "budget": budget
        }
    return None

# --- Step 2: Generate LLM Prompt ---
def build_itinerary_prompt(info):
    total_days = (info['end_date'] - info['start_date']).days + 1
    prompt = f"""
You are a travel expert. Based on the user's preferences, create a {total_days}-day travel itinerary.

Destination: {info['destination']}
Dates: {info['start_date']} to {info['end_date']}
Group Type: {info['group_type']}
Budget: {info['budget']}
Interests: {', '.join(info['interests'])}

Provide:
1. Daily itinerary with Morning, Afternoon, Evening
2. 1–2 local food/restaurant suggestions per day
3. A few travel tips for the location
4. Return response in Markdown format
"""
    return prompt

# --- Step 3: Query Ollama (LLaMA3) ---
def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="TripPlanner AI", layout="centered")
st.title("🧳 TripPlanner AI – Smart Travel Itinerary Generator")
st.markdown("_Plan your next adventure with AI in seconds!_ 🚀")

user_info = get_user_inputs()
if user_info:
    with st.spinner("Crafting your custom itinerary..."):
        prompt = build_itinerary_prompt(user_info)
        result = query_llm(prompt)
        st.markdown("### 🗓️ Your Personalized Itinerary")
        st.markdown(result, unsafe_allow_html=True)
