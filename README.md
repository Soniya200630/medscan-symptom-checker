# 🩺 MedScan — AI Symptom Checker

> An intelligent, AI-powered medical symptom checker that analyzes your symptoms and provides possible conditions, urgency levels, and personalized health guidance.

![MedScan](https://img.shields.io/badge/MedScan-AI%20Symptom%20Checker-38bdf8?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-F55036?style=for-the-badge)

---

## ✨ Features

- 🔍 **AI-Powered Analysis** — Uses Groq's LLaMA 3.3 model to analyze symptoms
- 🏷️ **Tag-based Symptom Input** — Add symptoms easily with quick-add chips
- 👤 **Patient Context** — Age, sex, pre-existing conditions all factored in
- 📊 **Ranked Conditions** — 3–5 possible conditions ordered by likelihood (High / Moderate / Low)
- 🚨 **Emergency Detection** — Auto-detects life-threatening symptom combinations
- 💡 **Lifestyle Advice** — Personalized tips based on your profile
- 📋 **Next Steps** — Clear recommended actions after analysis
- ⚡ **Fast & Free** — Powered by Groq's ultra-fast inference (no paid API needed for free tier)

---

## 🖥️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Backend | Python, Flask |
| AI Model | LLaMA 3.3 70B via Groq API |
| Styling | Custom CSS with dark theme |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/medscan-symptom-checker.git
cd medscan-symptom-checker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Your FREE Groq API Key
- Go to 👉 [console.groq.com](https://console.groq.com)
- Sign up (no credit card needed)
- Create an API Key

### 4. Create `.env` File
Create a file named `.env` in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App
```bash
python app.py
```

### 6. Open in Browser
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
medscan-symptom-checker/
├── app.py              ← Flask backend + Groq API proxy
├── requirements.txt    ← Python dependencies
├── .env                ← API key (never commit this!)
├── .gitignore          ← Protects .env from GitHub
├── README.md           ← You are here
└── templates/
    └── index.html      ← Full frontend (HTML + CSS + JS)
```

---

## 📦 Requirements

```
flask
python-dotenv
requests
```

---

## ⚠️ Disclaimer

> MedScan is an **educational tool only**. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any medical concerns. In case of emergency, call your local emergency services immediately.

---

## 🔒 Security Notes

- Never commit your `.env` file to GitHub
- The `.gitignore` is already configured to exclude it
- If you accidentally expose your API key, revoke it immediately at [console.groq.com](https://console.groq.com)

---

## 🙋‍♀️ Author

Made with ❤️ by **Sonia**
