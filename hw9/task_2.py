import re


def get_pattern():
    return r'\b(\w+)(\s+\1\b)+'


def remove_consecutive_duplicates(source_string, pattern):
    result = re.sub(pattern, r'\1', source_string)
    return result


some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений'

result = remove_consecutive_duplicates(some_string, get_pattern())
print(result)
