
# 🎭 Guess the Emoji – AI Game Show

An interactive web-based game where users make funny faces on camera, and an AI guesses the emotion and returns a matching emoji! Built using Google Cloud Vision API + Cloud Functions.

---

## 🚀 Features

- 🎥 Live webcam capture
- 🤖 Emotion detection using AI (Vision API)
- 😄 Returns emoji based on detected emotion
- ☁️ Backend hosted on Google Cloud Functions
- 💻 Fun frontend using HTML, JS & CSS

---

## 🛠️ Tech Stack

- Frontend: HTML, JavaScript, Canvas API
- Backend: Python (Google Cloud Function)
- AI: Google Cloud Vision API
- Deployment: Google Cloud Platform (GCP)

---

## 📦 Project Structure

```
guess-the-emoji/
├── frontend/
│   └── index.html
├── cloud-function/
│   ├── main.py
│   └── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. User opens the webpage, sees themselves via webcam.
2. Pressing **Submit Face** captures a snapshot.
3. Snapshot is sent to a Cloud Function via HTTP POST.
4. Vision API detects facial emotion.
5. Server returns the best matching emoji.
6. Emoji is displayed on the frontend.

---

## ⚙️ Setup & Deployment

### ✅ Prerequisites

- Google Cloud project
- Vision API enabled
- Billing enabled
- Python 3.10
- Google Cloud SDK installed

### ⬆️ Deploying the Cloud Function

1. Navigate to the function folder:
   ```bash
   cd cloud-function/
   ```

2. Deploy:
   ```bash
   gcloud functions deploy guessEmoji \
     --runtime python310 \
     --trigger-http \
     --entry-point analyze_face \
     --allow-unauthenticated \
     --region us-central1
   ```

3. Copy the deployed URL.

### 🌐 Run Frontend Locally

1. Replace `"YOUR_CLOUD_FUNCTION_URL"` in `index.html` with your actual function URL.
2. Open `index.html` in a browser using Live Server or a local web server:
   ```bash
   # Python 3
   python -m http.server
   ```

---

## 🥳 Demo

> “Can you guess what emoji I am? 😜😲😡😢”

📸 Smile. Frown. Look shocked.
Let AI read your face and react with an emoji.

---

## 📄 License

MIT License © 2025 
