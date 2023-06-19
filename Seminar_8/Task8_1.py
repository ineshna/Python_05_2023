








# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
#    Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#    Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#    Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
#    Берем первое совпадение по фамилии.
#    Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#    Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# user = ["first_name", "second_name", "number", "discription"]
# dictionary = {1:["first_name", "second_name", "number", "discription"],
#               2:["first_name", "second_name", "number", "discription"]}

def inputUsers() -> list:
    user = []
    user.append(input("Input first name: "))
    user.append(input ("Input secomd name: "))
    user.append(input("Input phone number: "))
    user.append(input("Input description: "))
    return user

print(inputUsers())
 #   def create(user : list) -> dict: