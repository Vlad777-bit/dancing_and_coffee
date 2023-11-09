from datetime import datetime

def parse_date(date_string):
    formats = ["%A, %B %d, %Y", "%A, %d.%m.%y", "%A, %d %B %Y"]
    for format_str in formats:
        try:
            date_obj = datetime.strptime(date_string, format_str)
            return date_obj
        except ValueError:
            pass
    return None


def main():
    while True:
        input_date = input(
            "Введите дату (или введите 'exit' для завершения): ")

        if input_date.lower() == 'exit':
            break

        try:
            parsed_date = parse_date(input_date)
            if parsed_date:
                print(parsed_date)
            else:
                print("Неверный формат даты. Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
