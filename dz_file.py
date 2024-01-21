def work_with_phon():
    choice=show_menu()
    filename = input('Введите путь к файлу: ') 
    phone_book=read_txt(filename)
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Фамилия: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            new_number=input('Номер телефона: ')
            print(change_number(phone_book,new_number))
	    	
        elif choice==4:
            add_new_abon(phone_book)            
        elif choice==5:
            write_txt(filename, phone_book)
        elif choice==6:
            file_line_wrap(phone_book)
        elif choice==7:
            print('Программа завершена всего доброго!!!')
            break
        choice=show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в исходном файле\n"
          "6. Перенести строку из одного файла в другой\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, [value.strip() for value in line.split(',')]))
            phone_book.append(record)	
    return phone_book


def write_txt(filename , phone_book):
    with open(filename,'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')


def print_result(book):
   for line in book:
       print(", ".join(f"{key} : {value}" for key,value in line.items()))
       

def find_by_lastname(book,surname):
    for i in range(len(book)):
        if surname in book[i].values():
            return ", ".join(f"{key} : {value}" for key,value in book[i].items())
    return 'Абонент не найден' 


def change_number(book, num):
    for i in range(len(book)):
        if num in book[i].values():
            return ", ".join(f"{key} : {value}" for key,value in book[i].items())
    return 'Абонент не найден' 

    
def add_new_abon(phone_book):
    surname = input('Фамилия: ') 
    name = input('Имя: ')
    number = input('Номер телефона: ')
    description = input('Описание абонента: ')
    keys = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    values = [surname, name, number, description]
    info = dict(zip(keys, values))
    phone_book.append(info)
    return phone_book


def file_line_wrap(book):
    destination_file = input('Введите путь к файлу в который нужно перенести строку: ')
    line_number = int(input('Введите номер строки: '))
    book_to_copy = book[line_number - 1]

    with open(destination_file, 'a') as file:
        line = ','.join(book_to_copy.values())
        file.write(f'{line}\n')


work_with_phon()

