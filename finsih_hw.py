import csv


def load_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data
# {'name': 'Allison  Miss. Helen Loraine', 'device_type': 'laptop', 'browser': 'Firefox', 'sex': 'female', 'age': '48', 'bill': '1034', 'region': 'Montreal: PQ / Chesterville: ON'}


def create_description(row):
    gender = 'женского' if row['sex'] == 'female' else 'мужского'
    description = f"Пользователь {row['name']} {gender} пола, {convert_years(row['age'])} совершил(а) покупку на {row['bill']} у.е. с {row['device_type']} браузера {row['browser']}. Регион, из которого совершалась покупка: {row['region']}."
    return description


def convert_years(age):
    if age.isdigit() == 1:
        age = int(age)
    else:
        age = float(age)
    suffix = 'лет'
    if (age // 10) % 10 != 1:
        if age % 10 == 1:
            suffix = 'год'
        elif age % 10 in (2, 3, 4):
            suffix = 'года'
    return f'{age} {suffix}'


def process_file(input_file, output_file):
    data = load_csv(input_file)
    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            description = create_description(row)
            writer.writerow([description])


process_file("./web_clients_correct.csv", "load.txt")
