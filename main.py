"""Entry point.

    python main.py init                      # create the database
    python main.py register                  # enrol a face with the webcam
    python main.py attend                    # start live attendance
    python main.py dashboard                 # open the admin dashboard
"""
import argparse
import subprocess
import sys

import config


def main() -> None:
    parser = argparse.ArgumentParser(description="Face Recognition Attendance System")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="create the database")
    sub.add_parser("attend", help="start live webcam attendance")
    sub.add_parser("dashboard", help="open the Streamlit admin dashboard")

    reg = sub.add_parser("register", help="register a person using the webcam")
    reg.add_argument("--id")
    reg.add_argument("--name")
    reg.add_argument("--email", default="")
    reg.add_argument("--dept", default="")

    args = parser.parse_args()

    if args.cmd == "init":
        from database.db import init_db
        init_db()
        print(f"Database ready at {config.DB_PATH}")

    elif args.cmd == "register":
        from services.register_user import register_from_webcam
        emp_id = args.id or input("ID: ")
        name = args.name or input("Name: ")
        ok, msg = register_from_webcam(emp_id, name, args.email, args.dept)
        print(msg)

    elif args.cmd == "attend":
        from services.attendance_service import run_live_attendance
        run_live_attendance()

    elif args.cmd == "dashboard":
        subprocess.run([sys.executable, "-m", "streamlit", "run", str(config.BASE_DIR / "app" / "dashboard.py")])


if __name__ == "__main__":
    main()
