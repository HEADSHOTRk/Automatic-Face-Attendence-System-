"""Central settings. Change values here instead of hunting through the code."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
KNOWN_FACES_DIR = DATA_DIR / "known_faces"
REPORTS_DIR = BASE_DIR / "reports"
DB_PATH = DATA_DIR / "attendance.db"

for _d in (DATA_DIR, KNOWN_FACES_DIR, REPORTS_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# ---- Face recognition ----
MODEL_NAME = "buffalo_l"          # InsightFace model pack (auto-downloads on first run)
DET_SIZE = (640, 640)
MATCH_THRESHOLD = 0.45            # cosine similarity; raise for stricter matching
CAMERA_INDEX = 0
PROCESS_EVERY_N_FRAMES = 2        # increase if the live feed is laggy

# ---- Attendance rules ----
SHIFT_START = "09:00"             # HH:MM
LATE_AFTER_MINUTES = 15           # arrive after 09:15 -> "Late"
MIN_ATTENDANCE_PERCENT = 75.0     # below this -> defaulter

# ---- Liveness (anti-spoofing) ----
ENABLE_LIVENESS = True
BLINKS_REQUIRED = 1
EAR_THRESHOLD = 0.21              # eye aspect ratio below this = eye closed

# ---- Emotion detection (optional, needs deepface) ----
ENABLE_EMOTION = False

# ---- Admin login for the dashboard (override with environment variables) ----
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

# ---- Email notifications (use a Gmail App Password) ----
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# ---- AI assistant (Claude API) ----
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")
