from typing import List, Dict
from procces_orders import procces_orders


def analyze_orders(processed_orders: List[Dict] = None) -> Dict:
    stats = {
        'total_orders': 0,
        'total_sum': 0,
        'by_status': {},
        'unique_users': set()
    }

    if processed_orders:
        lst = processed_orders
    else:
        lst = procces_orders()

    for order in lst:
        stats['total_orders'] += 1

        stats['total_sum'] += order['total']

        status = order['status']
        if status in stats['by_status']:
            stats['by_status'][status] += 1
        else:
            stats['by_status'][status] = 1

        stats['unique_users'].add(order['user'])

    stats['unique_users'] = list(stats['unique_users'])
    return stats


# for v in analyze_orders().values():
#     value = v
    