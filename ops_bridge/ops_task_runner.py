from ops_bridge import commerce_facade as cf
from ops_bridge.approvals import guard
def run_task(task: dict):
    action = task["action"]; platform = task["platform"]
    def on_timeout(): pass
    if action == "refund":
        guard("refund", f"Refund {task['amount']} on {platform} order {task['order_id']}", on_timeout)
        return cf.create_refund(platform, task["order_id"], task["amount"], task.get("reason",""))
    if action == "address_change":
        guard("address_change", f"Update address on {platform} order {task['order_id']}", on_timeout)
        return cf.update_address(platform, task["order_id"], task["address"])
    if action == "purchase":
        guard("purchase", f"Create order on {platform}", on_timeout)
        return cf.create_order(platform, task["payload"])
    if action == "status":
        return cf.get_order(platform, task["order_id"])
    raise ValueError(f"Unknown action: {action}")
