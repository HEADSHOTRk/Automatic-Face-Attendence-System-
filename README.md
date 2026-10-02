# Face Recognition Attendance System

AI-powered attendance using InsightFace (ArcFace), OpenCV, SQLite and Streamlit, with a Claude-powered assistant.

## Features
- Real-time multi-face recognition from a webcam
- Blink-based liveness check (anti-spoofing)
- One entry per person per day, with Present / Late status
- Optional emotion detection (DeepFace)
- Admin dashboard: register people, records, analytics, defaulters, Excel/CSV export
- AI assistant: ask attendance questions in plain English
- Email alerts to absentees

## Setup
```bash
python -m venv venv
venv\Scripts\activate          # Windows   (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python main.py init
```
Windows note: if `insightface` fails to install, install "Microsoft C++ Build Tools" first and retry.

## Usage
```bash
python main.py dashboard       # admin UI (default login: admin / admin123)
python main.py register        # enrol a face from the webcam
python main.py attend          # live attendance (press Q to quit)
```

## Optional environment variables
```
ADMIN_USERNAME, ADMIN_PASSWORD
SMTP_USER, SMTP_PASSWORD       # Gmail address + App Password
ANTHROPIC_API_KEY              # enables the AI assistant
```

## Project structure
```
main.py        entry point
config.py      all settings
database/      models, connection, queries
core/          face engine, matcher, liveness, emotion
services/      registration, live attendance, reports, email, AI assistant
app/           Streamlit dashboard + login
utils/         camera, logging, helpers
```
