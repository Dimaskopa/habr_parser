# Список команд:
# p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
# s – команда, которая спросит номер документа и выведет номер полки, на которой он находится
# l - команда, которая выведет список всех документов
# a -  команда, которая добавит новый документ в каталог и в перечень полок
# d - команда, которая спросит номер документа и удалит его из каталога и из перечня полок
# m - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
# as - команда, которая спросит номер новой полки и добавит ее в перечень
# q - выход из программы
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def people(number):
    for i in documents:
        a = {}
        for key, value in i.items():
            a[key] = value
        if a['number'] == number:
            return a['name']

def shelf(button):
    count = 0
    for key, value in directories.items():
        if button in value:
            return f'{key}'
            break
        count += 1
    if count == len(directories):
        return 'Такого документа не существует!'



def people_list():
    for i in documents:
        return f'{i["type"]} "{i["number"]}" "{i["name"]}"'

def add(number_shelf, type_shelf, number_doc, name_shelf):
    # number_shelf = input("Номер полки:")
    if number_shelf in directories:
        # type_shelf = input("Тип:")
        # number_doc = input("Номер документа:")
        # name_shelf = input("Имя:")
        new_doc = [{"type": type_shelf, "number": number_doc, "name": name_shelf}]
        new_doc.append(documents)
        directories[number_shelf].append(number_doc)
        documents.append({"type": type_shelf, "number": number_doc, "name": name_shelf})
        return f'{name_shelf} добавлен'
    else:
        return 'Такой полки не существует!'

def move(number_doc, number_key):
    if number_key in directories:
        count_miss = 0
        for key, value in directories.items():
            if number_doc in value:
                value.remove(number_doc)
                directories[number_key].append(number_doc)
                return directories
                break
            else:
                count_miss += 1
        if count_miss >= len(directories):
            return "Такого документа не существует"
    else:
        return "Такой полки не существует!"

def delete_doc(number):
    for i in documents:
        if i["number"] == number:
            i["number"] = ""

    for key, value in directories.items():
        if number in value:
            value.remove(number)
        return 'Документ удален'

def add_shelf(number_shelf):
    if number_shelf in directories:
        return 'Такая полка уже существует'
    if number_shelf not in directories:
        directories[number_shelf] = []
    return f'Полка номер {number_shelf} добавлена'


# def main():
#     while True:
#         user_input = input("Введите необходимое действие: ").lower()
#         if user_input == 'p':
#             print(people(input('Введите номер документа: ')))
#         elif user_input == 's':
#             print(shelf(input('Введите номер документа: ')))
#         elif user_input == 'l':
#             print(people_list())
#         elif user_input == 'a':
#             print(add())
#         elif user_input == 'd':
#             print(delete_doc(input('Введите номер документа: ')))
#         elif user_input == 'm':
#             print(move(input('Номер документа который необходимо переместить: '), input('Номер полки : ')))
#         elif user_input == 'as':
#             print(add_shelf(input('Введите номер полки которую хотите создать: ')))
#         elif user_input == 'q':
#             print('Программа закрыта')
#             break
# main()
#
