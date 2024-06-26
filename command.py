import sys
from greeting import greet_user
from add import add_note
from list import list_notes
from edit import edit_note
from delete import delete_note
from date import filter_notes_by_date
greet_user()
while True:
    command = input("Введите команду: ")
    if command == 'add':
        title = input("Введите заголовок заметки: ")
        message = input("Введите тело заметки: ")
        add_note(title, message)
        print("Заметка успешно сохранена")
    elif command == 'list':
        list_notes()
    elif command == 'filter':
        date = input("Введите дату для фильтрации заметок (формат YYYY-MM-DD): ")
        filter_notes_by_date(date)    
    elif command == 'edit':
        index = int(input("Введите номер заметки для редактирования: "))
        title = input("Введите новый заголовок заметки: ")
        message = input("Введите новое тело заметки: ")
        edit_note(index, title, message)
    elif command == 'delete':
        index = int(input("Введите номер заметки для удаления: "))
        delete_note(index)
    elif command == 'exit':
        print("Выход из программы...")
        sys.exit()
    else:
        print("Неизвестная команда, попробуйте снова.")