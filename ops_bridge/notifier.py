import json
from pathlib import Path
CONFIG = json.loads(Path(__file__).with_name("notify_config.json").read_text())
def send_notice(message: str):
    """Send a notification to operators.

    Currently just prints to stdout. TODO: integrate Twilio for SMS and
    SendGrid for email using values from ``notify_config.json``.
    """
    print(f"[NOTICE] {message}")
