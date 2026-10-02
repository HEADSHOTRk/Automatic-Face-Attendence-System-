# Automatic-Face-Attendence-System-
An AI-powered Automatic Face Attendance System designed to automate tracking for schools and offices. Built with Python and Computer Vision, it utilizes real-time face recognition to verify identities via a webcam, prevent proxy entries, and automatically export precise, timestamped attendance logs directly into CSV/Excel files.
# 🤖 Automatic Face Attendance System

An AI-powered, contactless **Automatic Face Attendance System** designed to automate attendance tracking for schools, universities, and corporate offices. This system utilizes advanced **Computer Vision** algorithms to recognize faces in real-time via a webcam or video stream, automatically log timestamps, and export accurate sheets.

Eliminate buddy-punching, manual paperwork, and proxy attendance with a secure, deep-learning-driven biometric solution.

---

## 🌟 Key Features

*   **Real-Time Face Recognition:** Instantly detects and recognizes registered individuals through standard webcam or external IP camera inputs.
*   **One-Click Enrollment:** Intuitive interface to capture up to 50 sample photos per individual to train the dataset locally.
*   **Anti-Spoofing & Liveness Detection:** Employs advanced deep learning filters to prevent spoofing attempts via printed photos or phone screens.
*   **Automated Log Management:** Generates structured hourly/daily attendance records exported instantly as CSV or Excel sheets.
*   **Interactive Dashboard:** Elegant GUI to view analytics, register new entries, and manage existing user databases.

---

## 🛠️ Tech Stack & Architecture

This repository contains implementations utilizing the following industry-standard libraries and frameworks:

*   **Core Language:** [Python](https://python.org) 3.9+
*   **Computer Vision:** [OpenCV](https://opencv.org) (Haar-Cascade / LBPH Classifier) & [Dlib](http://dlib.net)
*   **Deep Learning (Optional):** [TensorFlow](https://tensorflow.org) / Keras (FaceNet or DeepFace embeddings)
*   **Frontend UI:** Tkinter (Desktop App) or Streamlit / Flask (Web Interface)
*   **Database:** SQLite3 or Firebase Realtime Database

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed, then set up your environment:
```bash
git clone https://github.com
cd Automatic-Face-Attendance-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Usage Workflow
1.  **Registration:** Run the main application, input the User ID & Name, and capture images using your camera.
2.  **Training:** Click on `Train Images` to convert raw pixel profiles into trained face-encoding vectors.
3.  **Track Attendance:** Start the live tracking mode. The camera frame will label recognized individuals and automatically log their status.

---

## 📁 Repository Structure
```text
├── datasets/             # Directory where raw user image samples are stored
├── TrainingImage/        # Encoded numeric vectors after model training
├── attendance_logs/      # Generated CSV/Excel daily reports
├── app.py                # Main application entry point (GUI or Web Portal)
├── attendance.py         # Face tracking logic and detection loops
└── requirements.txt      # Python package dependencies
```

---

## 🤝 Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
