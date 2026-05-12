from paper.paper_models import VirtualOrder
from paper.paper_labels import validate_virtual_order_status

def validate_virtual_order(order: VirtualOrder) -> dict:
    warnings = {}
    try:
        validate_virtual_order_status(order.order_status)
    except Exception as e:
        warnings["status"] = str(e)

    if order.adjusted_theoretical_units <= 0:
        warnings["units"] = "Units <= 0"

    if order.stop_level is None or order.target_level is None:
        warnings["geometry"] = "Missing stop or target level"

    return warnings

def reject_virtual_order(order: VirtualOrder, reasons: list[str]) -> VirtualOrder:
    order.order_status = "virtual_rejected"
    order.rejection_reasons.extend(reasons)
    return order

def expire_virtual_order(order: VirtualOrder, timestamp: str, reason: str | None = None) -> VirtualOrder:
    order.order_status = "virtual_expired"
    order.expiry_timestamp = timestamp
    if reason:
        order.notes += f" Expired: {reason}"
    return order

def mark_virtual_order_filled(order: VirtualOrder, fill_timestamp: str, fill_price: float) -> VirtualOrder:
    order.order_status = "virtual_filled"
    order.requested_price = fill_price # Store the actual fill price here or in execution model
    order.notes += f" Filled at {fill_timestamp} price {fill_price}."
    return order

def virtual_order_is_active(order: VirtualOrder) -> bool:
    return order.order_status == "virtual_pending"
