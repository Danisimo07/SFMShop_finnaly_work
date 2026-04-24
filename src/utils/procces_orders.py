from working_num import calculate_order_total, get_discount_by_total
from load_order import load_order_from_file
from typing import List, Dict


def procces_orders(order_data: List[str] = None) -> List[Dict]:
    orders = []

    if order_data:
        order_line = order_data
    else:
        order_line = load_order_from_file()

    for line in order_line:
        order = line.split(":")

        if len(order) >= 4:
            order_d = {}

            order_d['order_id'] = order[0]
            order_d['total'] = calculate_order_total(
                order[1],
                get_discount_by_total(float(order[1]))
                )
            order_d['status'] = order[2]
            order_d['user'] = order[3]

            orders.append(order_d)
    return orders


# lst = procces_orders()
# print(f"📦 Обработано заказов: {len(lst)}")

# index = 0
# finish_index = len(lst)
# while index < finish_index:
#     order = lst[index]
#     print(order)
#     index += 1
