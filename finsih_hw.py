import csv


def load_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:
            # Преобразуем возраст в целые числа
            row['age'] = float(row['age']) if '.' in row['age'] else int(row['age'])
            data.append(row)
    return data


def create_description(row):
    # Создаём словарь для гендера
    gender_map = {
        'female': 'женского',
        'male': 'мужского'
    }
    gender = gender_map.get(row['sex'], 'неопределенного')
    description = (f"Пользователь {row['name']} {gender} пола, {convert_years(row['age'])} "
                   f"совершил(а) покупку на {row['bill']} у.е. с {row['device_type']} браузера {row['browser']}. "
                   f"Регион, из которого совершалась покупка: {row['region']}.")
    return description


def convert_years(age):
    # Склоняем число в текстовом формате
    suffix = 'лет' if 11 <= age % 100 <= 14 else {1: 'год', 2: 'года', 3: 'года', 4: 'года'}.get(age % 10, 'лет')
    return f'{age} {suffix}'


def process_file(input_file, output_file):
    # Читаем из csv и преобразуем в txt
    data = load_csv(input_file)
    with open(output_file, mode='w', encoding='utf-8') as file:
        for row in data:
            description = create_description(row)
            file.write(description + '\n')


process_file("./web_clients_correct.csv", "load.txt")
