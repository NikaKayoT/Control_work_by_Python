import csv
def list_notes():
    notes = []
    with open('notes.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            print(f"{index + 1}. Дата: {row[0]}, Заголовок: {row[1]}, Сообщение: {row[2]}")
            notes.append(row)
    if not notes:
        print("Список заметок пуст.")