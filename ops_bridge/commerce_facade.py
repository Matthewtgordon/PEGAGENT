from typing import Dict, Any
from .router import get_connector
def get_order(platform: str, order_id: str) -> Dict[str, Any]:
    return get_connector(platform).get_order(order_id)
def create_refund(platform: str, order_id: str, amount: float, reason: str) -> Dict[str, Any]:
    return get_connector(platform).create_refund(order_id, amount, reason)
def update_address(platform: str, order_id: str, address: Dict[str, Any]) -> Dict[str, Any]:
    return get_connector(platform).update_address(order_id, address)
def create_order(platform: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return get_connector(platform).create_order(payload)
