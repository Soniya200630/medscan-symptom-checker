# 🩺 MedScan — AI Symptom Checker

An AI-powered symptom checker built with vanilla HTML/CSS/JS and the Anthropic Claude API.

## Features
- Tag-based symptom input with quick-add chips
- Patient context (age, sex, pre-existing conditions)
- Severity + duration sliders
- AI returns ranked possible conditions with urgency levels
- Emergency alert detection

## Tech Stack
- Pure HTML + CSS + JavaScript (no frameworks)
- Anthropic Claude API (`claude-sonnet-4-20250514`)

## Setup

1. Clone the repo:
   git clone https://github.com/YOUR_USERNAME/medscan-symptom-checker.git

2. Open index.html in a browser
   - Double-click the file, OR
   - Use VS Code Live Server extension

> ⚠️ The app calls the Anthropic API directly from the browser.
> Make sure you're running it via claude.ai Artifacts or a host
> that supports the `anthropic-dangerous-direct-browser-access` header.

## Disclaimer
This tool is for educational purposes only and is NOT a substitute
for professional medical advice. Always consult a doctor.
```

---

## 📄 File 3: `.gitignore` (optional)
```
.DS_Store
Thumbs.db
*.env
node_modules/