import csv


class CustomerDescriptionGenerator:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def load_csv(self):
        """ Загружает данные из CSV-файла и преобразует возраст в числовой формат. """

        with open(self.input_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = []

            for row in csv_reader:
                row['age'] = self._parse_age(row['age'])
                data.append(row)

        return data

    @staticmethod
    def _parse_age(age):
        """ Преобразует строку возраста в числовой формат. """

        return float(age) if '.' in age else int(age)

    @staticmethod
    def _create_description(row):
        """ Создает описание клиента на основе его данных. """

        gender_map = {
            'female': 'женского',
            'male': 'мужского'
        }
        gender = gender_map.get(row['sex'], 'неопределенного')

        age = CustomerDescriptionGenerator._convert_years(row['age'])
        device = CustomerDescriptionGenerator._translate_device(row['device_type'])

        description = (
            f"Пользователь {row['name']} {gender} пола, {age} "
            f"совершил(а) покупку на {row['bill']} у.е. с {device} браузера {row['browser']}. "
            f"Регион, из которого совершалась покупка: {row['region']}."
        )

        return description

    @staticmethod
    def _translate_device(device_type):
        """ Выполняет перевод устройства с англ. на рус. """

        devices = {
            'mobile': 'мобильного',
            'tablet': 'планшетного',
            'laptop': 'переносного компьютера',
            'desktop': 'стационарного компьютера',
        }

        return devices.get(device_type, "пользовательского устройства")

    @staticmethod
    def _convert_years(age):
        """ Преобразует число лет в текстовый формат с правильным склонением. """

        suffix = 'лет' if 11 <= age % 100 <= 14 else {
            1: 'год',
            2: 'года',
            3: 'года',
            4: 'года'
        }.get(age % 10, 'лет')

        return f'{age} {suffix}'

    def process_file(self):
        """ Читает данные из CSV-файла и записывает описания в TXT-файл. """

        data = self.load_csv()

        with open(self.output_file, mode='w', encoding='utf-8') as file:
            for row in data:
                description = self._create_description(row)
                file.write(description + '\n\n')


# Создаём инстанс класса, принимающий исходный файл и название финального файла
generator = CustomerDescriptionGenerator(
    "./web_clients_correct.csv", "load.txt"
)
# Запускаем конвектор
generator.process_file()
