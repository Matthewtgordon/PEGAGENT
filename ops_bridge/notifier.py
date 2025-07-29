import json
from pathlib import Path
CONFIG = json.loads(Path(__file__).with_name("notify_config.json").read_text())
def send_notice(message: str):
    print(f"[NOTICE] {message}")
