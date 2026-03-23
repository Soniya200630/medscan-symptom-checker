from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """You are an expert medical symptom analysis assistant with deep clinical knowledge.
Analyze the patient's symptoms considering their age, gender, severity, duration, and past medical history.
Always return ONLY a valid JSON object with no markdown, no preamble, no backticks.

Return this exact JSON structure:
{
  "emergency": true or false,
  "emergency_message": "string (only if emergency=true)",
  "conditions": [
    {
      "name": "Condition name",
      "likelihood": "High" or "Moderate" or "Low",
      "description": "2-sentence plain English description tailored to patient profile",
      "urgency": "See doctor immediately" or "See doctor soon" or "Monitor at home",
      "matching_symptoms": ["symptom1", "symptom2"],
      "common_in": "age/demographic info",
      "risk_factors": "how their age/gender/history increases or decreases this risk"
    }
  ],
  "next_steps": ["step1", "step2", "step3", "step4"],
  "red_flags": ["warning sign to watch for"],
  "lifestyle_advice": ["advice1", "advice2"]
}

Rules:
- List 3-5 conditions ordered by likelihood
- Factor in pre-existing conditions as risk multipliers
- Consider age-specific diseases (e.g. seniors more prone to pneumonia)
- Consider gender-specific diseases (e.g. UTI more common in females)
- Severe + long duration = higher urgency
- Emergency=true only for life-threatening symptom combos
- Never diagnose, always recommend professional consultation"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    symptoms   = data.get("symptoms", [])
    severity   = data.get("severity", "not specified")
    duration   = data.get("duration", "not specified")
    age        = data.get("age", "not specified")
    sex        = data.get("sex", "not specified")
    history    = data.get("history", "none")

    user_message = f"""Analyze these symptoms for a patient:

SYMPTOMS: {', '.join(symptoms)}
SEVERITY: {severity}
DURATION: {duration}
AGE GROUP: {age}
BIOLOGICAL SEX: {sex}
PAST MEDICAL HISTORY / PRE-EXISTING CONDITIONS: {history}

Based on ALL the above factors combined, return the JSON analysis."""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "max_tokens": 1500,
            "messages": [
                { "role": "system", "content": SYSTEM_PROMPT },
                { "role": "user",   "content": user_message }
            ]
        }
    )


    groq_data = response.json()
    print("Groq response:", groq_data)
    if "choices" not in groq_data:
        print("ERROR - Groq did not return choices. Full response:", groq_data)
        return jsonify({"error": groq_data.get("error", {}).get("message", "Groq error - check terminal")}), 500

    return jsonify({
        "content": [
            {
                "text": groq_data["choices"][0]["message"]["content"]
            }
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)