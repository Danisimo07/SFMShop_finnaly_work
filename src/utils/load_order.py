from typing import List


def load_order_from_file(filename: str = '../../data/orders.txt') -> List[str]:
    lst_data_order = []

    try:
        with open(filename.strip(), 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip()

                if clean_line and ':' in clean_line:
                    lst_data_order.append(clean_line)

        return lst_data_order

    except FileNotFoundError:
        print(f"❌ К сожалению файл {filename} не найден!")
    except Exception as e:
        print(f"❌ Ошибка чтения: {e}")


# score = 0
# for line in load_order_from_file():
#     score += 1
#     print(f"Строка №{score}: \"{line}\"")