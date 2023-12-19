import re


def get_pattern_car_id():
    return r'^([АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})$'


def is_valid(item, pattern):
    car_id_upper = item.upper()

    match = re.fullmatch(pattern, car_id_upper)

    if match:
        return f"Номер {match.group(1)} валиден. Регион: {match.group(2)}."
    else:
        return "Номер не валиден."


print(is_valid('А222ВС96', get_pattern_car_id()))
print(is_valid('АБ22ВВ193', get_pattern_car_id()))
