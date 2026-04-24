def calculate_order_total(price: int, discount_rate: float) -> float:
    final_price = round(float(price) * (1 - discount_rate), 2)
    return final_price


def get_discount_by_total(total: int) -> float:
    if total > 10_000:
        return 0.15
    elif total > 5_000:
        return 0.10
    elif 0 < total <= 5_000:
        return 0.05
    else:
        return 0
