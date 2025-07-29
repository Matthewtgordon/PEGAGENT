def get_order(order_id: str):
    return {"id": order_id, "platform": "etsy", "status": "stub"}
def create_refund(order_id: str, amount: float, reason: str):
    return {"ok": True, "order_id": order_id, "amount": amount, "reason": reason}
def update_address(order_id: str, address: dict):
    return {"ok": True, "order_id": order_id, "address": address}
def create_order(payload: dict):
    return {"ok": True, "order_id": "TBD", "payload": payload}
