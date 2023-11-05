documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def owner(number_doc):
    """
    Функция возвращает по номеру документа данные о его владельце
    """
    owner_name = ''
    for row in documents:
        if row['number'] == number_doc:
            owner_name = 'Владелец документа: ' + row['name']
    if owner_name == '':
        owner_name = 'Документ не найден в базе'
    return owner_name


def doc_dir(number_doc):
    """
    Функция возвращает по номеру документа данные о месте хранения
    """
    shelf = ''
    for item, values in directories.items():
        if number_doc in values:
            shelf = 'Документ хранится на полке: ' + item
    if shelf == '':
        shelf = 'Документ не найден в базе'
    return shelf


def list_doc():
    """
    Функция возвращает список документов на полках
    """
    for i in documents:
        for item, values in directories.items():
            if i['number'] in values:
                print('№ ' + i['number'] + ', тип: ' + i['type'] +
                      ', владелец: ' + i['name'] + ', полка хранения: ' + item)


def list_shelf():
    """
    Функция возвращает список полок
    """
    listshelf = ''
    for item, values in directories.items():
        listshelf = listshelf + item + ','
    listshelf = listshelf[:-1] + '.'
    return listshelf


def del_shelf(number_shelf):
    """
    Функция удаляе полку, если она не пустая
    """
    count = 0
    for item, values in directories.items():
        if number_shelf in item:
            count = 1
            if values != []:
                count = 2
    if count == 1:
        del directories[number_shelf]
        print('Полка удалена. Текущий перечень полок: ' + list_shelf())
    elif count == 2:
        print('На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: ' + list_shelf())
    else:
        print('Такая полка не существует. Текущий перечень полок: ' + list_shelf())


def add_shelf(number_shelf):
    """
    Функция добавляет полку, если такой ещё нет
    """
    count = 0
    for item, values in directories.items():
        if number_shelf in item:
            count = 1
    if count == 1:
        print('Такая полка уже существует. Текущий перечень полок: ' + list_shelf())
    else:
        directories[number_shelf] = []
        print('Полка добавлена. Текущий перечень полок: ' + list_shelf())


def main():
    """
    Основная функция автоматизации работы секретаря
    """
    a = 0
    while a < 1:
        command_input = input('Введите команду: \n')
        if command_input == 'p':
            number_input = input('Введите номер документа: \n')
            print(owner(number_input))
        elif command_input == 's':
            number_input = input('Введите номер документа: \n')
            print(doc_dir(number_input))
        elif command_input == 'l':
            list_doc()
        elif command_input == 'as':
            number_input = input('Введите номер полки: \n')
            add_shelf(number_input)
        elif command_input == 'ds':
            number_input = input('Введите номер полки: \n')
            del_shelf(number_input)
        elif command_input == 'q':
            break
        else:
            print('Нет такой команды')


main()
