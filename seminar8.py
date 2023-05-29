# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной последовательности
# 4. Использование функций. Программа не должна быть линейной

import json
import re

def verify_input(string):
    return string == '' or re.match("^\s+$", string)

def input_str(message: str, condition, warning_message: str):
    while True:
        s = input(f'{message}: ')
        if condition(s):
            print(warning_message)
        else:
            return s.strip()

def write_file(data: str):
    with open(PHONE_BOOK, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def read_file():
    with open(PHONE_BOOK, 'r', encoding='utf-8') as file:
        return file.read()

def load_cfg():
    try:
        obj = json.loads(read_file())
        return obj[-1]['id']
    except:
        open(PHONE_BOOK, 'w', encoding='utf-8').close()
        return 0

def add_contact():
    print(TEXTS['id1'])
    CFG['ID'] += 1
    data = {
        'id': CFG['ID'],
        'sn':    '',
        'n':     '',
        'secn':  '',
        'phone': ''
    }

    try:
        json_data = json.loads(read_file())
    except:
        json_data = []

    for i in range(len(FIELDS_NAMES)):
        s = input_str(FIELDS_NAMES[i], verify_input, TEXTS['id2'])
        data[FIELDS_CODES[i]] = str(s)

    json_data.append(data)
    write_file(json_data)
    print(TEXTS['id3'])

def modify_contact():
    print(TEXTS['id4'])
    flag = True
    while flag:
        id = int(input_str(TEXTS['id5'], lambda x: x == '' or not re.match("^\d+$", x), TEXTS['id6']))
        data = json.loads(read_file())
        for dct in data:
            if dct['id'] == id:
                field_name  = input_str(TEXTS['id8'], lambda x: x not in FIELDS_NAMES, TEXTS['id9'])
                field_value = input_str(TEXTS['id10'] + f'" {field_name}"', verify_input, TEXTS['id2'])
                dct[FIELDS_CODES[FIELDS_NAMES.index(field_name)]] = field_value
                flag = False
                break
        else: print(f"ID = {id} {TEXTS['id7']}")  
    write_file(data)
    print(TEXTS['id11'])

def delete_contact():
    print(TEXTS['id13'])
    flag = True
    while flag:
        id = int(input_str(TEXTS['id14'], lambda x: x == '' or not re.match("^\d+$", x), TEXTS['id6']))
        data = json.loads(read_file())
        for dct in data:
            if dct['id'] == id:
                data.remove(dct)
                flag = False
                break
        else: print(f"ID = {id} {TEXTS['id7']}")
    write_file(data)
    print(TEXTS['id15'])

def search_contact():
    print(TEXTS['id16'])
    idxs = []
    flag = True
    while flag:
        field   = input_str(TEXTS['id17'], lambda x: not(re.match("^\*$", x) or x in FIELDS_NAMES), TEXTS['id18'])
        pattern = input_str(TEXTS['id20'], verify_input, TEXTS['id2'])
        data = json.loads(read_file())

        if field == '*':
            for contact in data:
                for code in contact:
                    if re.findall(pattern, str(contact[code]), re.IGNORECASE):
                        idxs.append(data.index(contact))
        else:
            for contact in data:
                if re.findall(pattern, contact[FIELDS_CODES[FIELDS_NAMES.index(field)]], re.IGNORECASE):
                    idxs.append(data.index(contact))
                    
        if len(idxs) > 0: flag = False
        else:             print(TEXTS['id19'])
    print(TEXTS['id21'])
    show_contacts([data[i] for i in set(idxs)])

def show_contacts(data):
    for i in range(len(data)):
        print("{}№{} - ID: {}, {}: {}, {}: {}, {}: {}, {}: {}".
        format(TEXTS['id12'] ,i+1, data[i]['id'], FIELDS_NAMES[0], 
        data[i][FIELDS_CODES[0]], FIELDS_NAMES[1], data[i][FIELDS_CODES[1]], 
        FIELDS_NAMES[2], data[i][FIELDS_CODES[2]], FIELDS_NAMES[3], data[i][FIELDS_CODES[3]]))

def show_menu(menu_items, verified_items):
    flag = True
    while flag:
        print(TEXTS['id22'])
        print(TEXTS['id23'])
        for key in menu_items:
            print(f'{key} - {MENU[key]}')
        s = int(input_str(TEXTS['id24'], lambda x: not re.match(f"^{verified_items}$", x), TEXTS['id25']))

        if   s == 1: show_contacts(json.loads(read_file()))
        elif s == 2: add_contact()
        elif s == 3: search_contact()
        elif s == 4: modify_contact()
        elif s == 5: delete_contact()
        else:        flag = False

def main():
    if verify_input(read_file()):
        print(TEXTS['id26'])
        show_menu([2, 6], "[2, 6]")
    else:
        show_menu(range(1, len(MENU) + 1), "[1-6]")

PHONE_BOOK = "phone_book.txt"
FIELDS_NAMES = ('Фамилия', 'Имя', 'Отчество', 'Номер телефона')
FIELDS_CODES = ('sn', 'n', 'secn', 'phone')
CFG = {
    'ID': load_cfg()
}
TEXTS = {
    'id1':  "Добавление контакта",
    'id2':  "Ошибка при вводе. Ввод не может быть пустым",
    'id3':  "Контакт добавлен успешно",
    'id4':  "Изменение контакта",
    'id5':  "Введите ID контакта, который хотите изменить",
    'id6':  "Ошибка при вводе ID. Он должен состоять только из цифр",
    'id7':  "не найден. Повторите попытку",
    'id8':  "Введите параметр, который хотите изменить (Фамилия, Имя, Отчество, Номер телефона)",
    'id9':  "Ошибка при вводе! Введите одно из следующих значений с учётом регистра (Фамилия, Имя, Отчество, Номер телефона)",
    'id10': "Введите новое значение для параметра",
    'id11': "Контакт изменен",
    'id12': "Контакт ",
    'id13': "Удаление контакта",
    'id14': "Введите ID контакта, который хотите удалить",
    'id15': "Контакт удалён",
    'id16': "Поиск контакта",
    'id17': "Введите конкретное поле, по которому хотите найти контакт (Фамилия, Имя, Отчество, Номер телефона), либо * для поиска по любым полям",
    'id18': "Ошибка при вводе данных! Введите значение из допустимых полей (Фамилия, Имя, Отчество, Номер телефона) или введите *",
    'id19': "Данных, удовлетворяющих условию поиска, не найдено",
    'id20': "Введите шаблон для поиска",
    'id21': "Найдены следующие контакты",
    'id22': "Главное меню",
    'id23': "Выберите пункт меню из списка ниже",
    'id24': "Выбранный пункт",
    'id25': "Ошибка при вводе. Выберите, пожалуйста, значения, перечисленные выше",
    'id26': "Телефонная книга пуста. Добавьте первый контакт"
}

MENU = {
    1: "Показать все контакты",
    2: "Добавить контакт",
    3: "Найти контакт",
    4: "Изменить контакт",
    5: "Удалить контакт",
    6: "Выйти из программы"
}

main()