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
# phone_dir = {1:["first_name", "second_name", "number", "discription"],
#               2:["first_name", "second_name", "number", "discription"]}
# key_count -счетчик id

from os.path import join, abspath, dirname

phone_direct = {1: ['Иванов', 'Иван', '+7(xxx)xxx-xx-xx', 'desription_Иванов'], 
            2: ['Петров', 'Петр', '+7(---)xxx-xx-xx', 'desription_Петров'], 
            3: ['Соколов', 'Илья', '+7(---)---------', 'desription_Соколов'], 
            4: ['Павельев', 'Андрей','+7(***)***-**-**', 'desription_Павельев'], 
            5: ['Пешехов', 'Антон', '+7++++++++++', 'desription_Пешехов'],
            6: ['Сааков', 'Илья', '+7(+++)+++-++-++', 'desription_Сааков'], }

def Input_Users() -> list:
    user = []
    user.append(input("Input first name: "))
    user.append(input ("Input secomd name: "))
    user.append(input("Input phone number: "))
    user.append(input("Input description: "))
    return user
#print(Input_Users())

# key_count = 0
# phone_dir = dict()
def create(phone_dir_local:dict, idc: int, user : list ) -> dict:
    idc += 1
    phone_dir_local[idc] = user
    return phone_dir_local, idc

# user1 = ["first_name1", "second_name1", "number1", "discription1"]
# user2 = ["first_name2", "second_name2", "number2", "discription2"]

# phone_dir,key_count = create (phone_dir, key_count,user1)
# phone_dir,key_count = create (phone_dir, key_count,user2)
#print(phone_dir)


def menu ():
    print("Введите 1 если хотите ввести пользователя: ")
    print("Введите 2 если хотите распечатать спрвочник: ")
    print("Введите 3 для экспорта ")
    print("Введите 4 для поиска ")
    print("Введите 5 если хотите удалить пользователя ")
    print("Введите 6 что бы редактировать запись")
    key_count = 0
    phone_dir = dict()
    number = 0
    fio = ""
    while True:
        num = int(input("Выберите операция "))
        if num == 0:
            break
        if num == 1:
            user = Input_Users()
            phone_dir,key_count = create (phone_dir, key_count,user)
        if num == 2:
            print(phone_dir)
        if num == 3:
            file_name = input ("Выберите имя файла ")
            export_phone_dir(phone_dir, file_name)
        if num == 4:
            serching = input("Кого ищем? ")
            number, fio =search_user(phone_dir,serching)
            print(f"пользователь{fio} находитсяпод номеро{number}")
        if num == 5 :
            deleted_name = input("кого удалить? ")
            phone_dir = delete( phone_dir,deleted_name)
            print(phone_dir) 
        if num == 6:
            change_element = input("Введите кого редактирвать ")
            phone_dir = update (phone_dir, change_element)
            print (phone_dir)





def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name+'txt')
    with open(full_name,mode= 'w', encoding='utf-8' ) as file:
        for idc,user in phone_dir.items():
            file.write(f"{idc}#{user[0]}#{user[1]}#{user[2]}#{user[3]}\n")
 



def search_user(phone_dir: dict,searching: str) -> int:
    for idc,user in phone_dir.items():
        if user[0].startswith(searching):
            return idc,user
        
def print_dict(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}:{user[0]} {user[1]} {user[2]} {user[3]}")

def delete(phone_dir: dict, searching : str):
    tmp = search_user(phone_dir,searching)
    if tmp is not None:
        idc, _ = tmp
        phone_dir.pop(idc)
    else:
        print("пользователя нет")
    return phone_dir
def update (phone_dir: dict, searching: str):
    tmp =search_user(phone_dir,searching)
    if tmp is None:
        print("Пользователь не найден")
        return phone_dir
    idc, _ = tmp
    new_second_name =input("Введите фиамилию")
    new_name = input("введите имя")
    new_phone = input('ведите номер')
    new_description = input("введите описнаие")
    if len(new_second_name) >= 1:
        phone_dir[idc][0]= new_second_name
    if len(new_name) >= 1:
        phone_dir[idc][1]= new_name
    if len(new_phone) >= 1:
        phone_dir[idc][2]= new_phone
    if len(new_description) >= 1:
        phone_dir[idc][3]= new_description
        
    return(phone_dir)





#print_dict(phone_dir)
#print(phone_dir)
menu()
#export_phone_dir(phone_dir, "phones")
#search_user(phone_dir,"Иван")
#print(search_user(phone_dir, "Пе"))
#print(import_dir("phones.txt"))