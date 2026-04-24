from utils.order_process import process_order_file

def main():
    stats = process_order_file()
    return stats


if __name__ == "__main__":
    print(main())
