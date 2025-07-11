# JU11--TripPlanner-AI
GEN AI
🧳 TripPlanner AI – Personalized Travel Itinerary Generator
🌍 What It Does
TripPlanner AI helps users create smart, customized travel itineraries based on their:

🎯 Destination

📅 Travel dates

👨‍👩‍👧 Travel group (solo, couple, family)

💰 Budget

🧡 Interests (nature, culture, adventure, food, etc.)

✨ Key Features
Feature	Description
🛫 Location & Date Input	Enter destination, start & end dates
👤 Traveler Profile	Select type: solo, couple, family, senior
🧭 Smart Itinerary Builder	LLM generates daily plan with places, timings, tips
🍽️ Meal & Cafe Suggestion	Suggests 2–3 popular or local food options per day
💬 Travel Tips	Local etiquette, safety tips, and must-haves
📄 Export PDF Itinerary	Download your plan as a trip-ready document

🌐 Tech Stack
Layer	Tool
UI	Streamlit
LLM	Ollama (LLaMA3) or GPT
Travel Data	OpenAI, static knowledge, or optional integration with APIs
Export	fpdf or python-docx for downloadable itineraries

🧠 Sample Output
json
Copy
Edit
{
  "Day 1": {
    "Morning": "Arrival in Paris, check-in at hotel",
    "Afternoon": "Visit Eiffel Tower, Seine River walk",
    "Evening": "Dinner at Le Jules Verne, Paris",
    "Tips": ["Buy museum pass", "Keep metro card ready"]
  },
  "Day 2": {
    "Morning": "Louvre Museum guided tour",
    "Afternoon": "Explore Montmartre",
    "Evening": "Sunset at Sacré-Cœur"
  }
}
🧳 Use Cases
First-time travelers needing daily plans

Honeymoon or family trip planners

Students or bloggers generating travel blogs

Travel agencies offering AI-generated itinerary previews

🔮 Future Add-ons
Real-time weather & map info

Auto-booking suggestions (hotels/flights)

Group travel optimization

Multi-country trip support

# 🧳 TripPlanner AI – Smart Travel Itinerary Generator

TripPlanner AI helps you plan the perfect trip using LLMs. Based on your preferences, it generates a detailed day-by-day itinerary, food suggestions, and local travel tips.

## ✨ Features

- Enter destination, dates, group type, interests, and budget
- AI-generated daily itinerary (morning, afternoon, evening)
- Food & restaurant recommendations
- Local travel tips
- Markdown-formatted travel plan

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/tripplanner-ai.git
cd tripplanner-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
