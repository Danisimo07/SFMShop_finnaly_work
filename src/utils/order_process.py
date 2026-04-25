from typing import Dict


def process_order_file(input_file: str = '../../data/orders.txt',
                       output_file: str = '../../data/processed_orders_report.txt'
                       ) -> Dict:
    try:
        from load_order import load_order_from_file
        from procces_orders import procces_orders
        from analyze_order import analyze_orders


        raw_orders = load_order_from_file(input_file)
        processed_ordres = procces_orders(raw_orders)
        stats = analyze_orders(processed_ordres)

        by_state = stats['by_status']
        by_status = [f"{k}: {v}" for k, v in by_state.items()]
        """
        Параметр output_file принимает в себя путь файла
        """
        report_lines = [
            f"Обработано заказов: {stats['total_orders']}",
            f"Общая сумма: {stats['total_sum']:.2f} руб.",
            f"По статусам: {', '.join(by_status)}",
            f"Уникальных пользователей: {len(stats['unique_users'])}"
        ]

        # Запись в файл с переносом строк
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(report_lines))

        return stats
    except ValueError:
        print("❌ Неверный ввод")
    except FileNotFoundError:
        print("❌ Файл не найден!")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

# print(process_order_file())
