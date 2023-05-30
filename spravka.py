print("Добро пожаловать в телефонный справочник. Для работы с программой вам необходимо выбрать задачу:")

def modif ():
    print("Введите - 1, если хотите внести нового пользователя в телефонный справочник")
    print("Введите - 2, если хотите просмотреть телефонный справочник полностью")
    print("Введите - 3, если хотите выполнить поиск по фамилии")
    print("Введите - 4, если хотите остановить программу")
    numbs = input()
    if numbs == '1':
        imp()
    if numbs == '2':
        exs()
    if numbs == '3':
        search()
    if numbs == '4':
        exit()
    else: modif()

def imp ():
    with open('spravka.txt', 'a', encoding='utf-8') as file:
        lastname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        middlename = input("Введите отчество: ")
        age = input("Введите возрастр: ")
        number = input("Введите номер телефона: ")
        file.write(lastname+' ')
        file.write(name+' ')
        file.write(middlename+' ')
        file.write(age+' ')
        file.write(number+'\n')
        print("Данные успешно внесены")

def exs ():
    with open('spravka.txt', 'r', encoding='utf-8') as file:
        all_spisok = file.read()
        print(all_spisok)      

def search ():
    female = input("Введите фамилию: ")
    with open('spravka.txt', 'r', encoding='utf-8') as file:
        all_spisok = file.read()
        search_sanname = all_spisok.split('\n')
        for u in search_sanname:
            for ud in u.split():
                if ud == female:
                    print("Нашел: " + u)

modif()