import re
import requests
import json


def get_pattern_car_id():
    return r'^([АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})$'


def get_region_by_code(code):
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/antirek/russian-codes/master/data/codes.json')
        response.raise_for_status()

        data = response.json()
        result = ''

        for region in data['regions']:
            if str(code) in str(region['gibdd']):
                result = f"{code} - {region['title']}"
            else:
                if not len(result):
                    result = "Регион не найден"

        return result

    except Exception as err:
        print(f'Произошла ошибка при получении данных: {err}')


def is_valid(item, pattern):
    car_id_upper = item.upper()

    match = re.fullmatch(pattern, car_id_upper)

    if match:
        return f"Номер {match.group(1)} валиден. Регион: {get_region_by_code(match.group(2))}."
    else:
        return "Номер не валиден."


print(is_valid('А257ВС58', get_pattern_car_id()))
print(is_valid('А222ВС96', get_pattern_car_id()))
print(is_valid('АБ22ВВ193', get_pattern_car_id()))
