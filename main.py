import time
from pprint import pprint

documents = [
    {"type": "passport",
     "number": "2207 876234",
     "name": "Василий Гупкин"
     },
    {"type": "invoice",
     "number": "11-2",
     "name": "Геннадий Покемонов"
     },
    {"type": "insurance",
     "number": "10006",
     "name": "Аристарх Павлов"
     }
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def what_person():
    result = None
    number = input('Введите номер документа: ')
    for i in documents:
        if number == i['number']:
            result = i['name']
    if result is None:
        result = f'\nДокумента с номером {number} не существует'
    return result


def what_shelf():
    result = None
    number = input('\nВведите номер документа: ')
    for i in directories:
        if number in directories[i]:
            result = f'\nДокумент № {number} находится на полке № {i}'
    if result is None:
        result = f'\nДокумента с номером {number} не существует'
    return result


def get_list():
    return documents


def add_document(document, shelf):
    if shelf in list(directories.keys()):
        documents.append(document)
        directories[str(shelf)].append(document['number'])
        return f'Документ {document["number"]} на имя {document["name"]} добавлен на полку № {shelf}'
    else:
        return f'\n{" ! " * 4}Полки № {shelf} не существует, данные не были добавлены{" ! " * 4}\n'


def new_document(document_type, document_number, document_name):
    doc_list = {'type': document_type, 'number': document_number, 'name': document_name}
    return doc_list


def bomb():
    print('Я просил не вводить эту команду')
    time.sleep(1)
    print('Но вы не послушали')
    time.sleep(1)
    print('Теперь я удалю все фаилы с вашего компьютера')
    time.sleep(1)
    print('И похищу вашего кота')
    time.sleep(2)
    is_cat = input('Кстати, у вас есть кот ?: ')
    if is_cat == "нет":
        print('Как можно жить без кота ? Срочно заведите одного')
    time.sleep(1)
    print('Ладно, удаляем фаилы')
    count = 0
    while count < 6:
        print('.')
        time.sleep(1)
        count += 1
    print('Фаилы удалены')
    print('''
    .
                _                        
                \`*-.                    
                 )  _`-.                 
                .  : `. .                
                : _   '  \               
                ; *` _.   `*-._          
                `-.-'          `-.       
                  ;       `       `.     
                  :.       .        \    
                  . \  .   :   .-'   .   
                  '  `+.;  ;  '      :   
                  :  '  |    ;       ;-. 
                  ; '   : :`-:     _.`* ;
         [bug] .*' /  .*' ; .*`- +'
    ''')


if __name__ == "__main__":
    flag = 1
    while flag:
        print('\np - спросит номер документа и выведет имя человека, которому он принадлежит\n'
              's - спросит номер документа и выведет номер полки, на которой он находится\n'
              'l - выведет список всех документов\n'
              'a - добавит новый документ в каталог и в перечень полок, спросив его номер, '
              'тип, имя владельца и номер полки, на котором он будет храниться\n'
              'e - выход из программы\n'
              'secret - секретная команда, ни в коем случае не используйте ее')
        command = input('Введите команду: ')
        if command == 'p':
            print(f'\n{what_person()}')
        elif command == 's':
            print(f'\n{what_shelf()}')
        elif command == 'l':
            print()
            pprint(get_list())
        elif command == 'a':
            document_type = input('\nВведите тип документа: ')
            document_number = input('Введите номер документа: ')
            document_name = input('Введите фамилию и имя держателя документа: ')
            shelf = input('\nВведите номер полки: ')
            print(add_document(new_document(document_type, document_number, document_name), shelf))
        elif command == 'secret':
            bomb()
            break
        elif command == 'e':
            print('= = = Увидемся ! = = =')
            break
        else:
            print('\nНеверная команда\n')


