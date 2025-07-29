import json, time
from pathlib import Path
from .notifier import send_notice
CONFIG = json.loads(Path(__file__).with_name("approvals.json").read_text())
def require_approval(action: str) -> bool:
    rule = CONFIG.get(action); return rule == "manual"
def delay_auto_params(action: str):
    rule = CONFIG.get(action)
    if isinstance(rule, dict) and rule.get("mode") == "delay_auto":
        return rule.get("delay_minutes", 10)
    return None
def guard(action: str, summary: str, on_timeout):
    if require_approval(action):
        send_notice(f"APPROVAL REQUIRED: {summary}")
        raise RuntimeError("Awaiting human approval")
    delay = delay_auto_params(action)
    if delay:
        send_notice(f"PENDING: {summary}\nAuto-approve in {delay} minutes unless you reply STOP.")
        time.sleep(delay * 60); on_timeout()
