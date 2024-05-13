import csv
import datetime
def filter_notes_by_date(date):
    notes = []
    with open('notes.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            note_date = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
            if note_date.date() == datetime.datetime.strptime(date, '%Y-%m-%d').date():
                print(f"Дата: {row[0]}, Заголовок: {row[1]}, Сообщение: {row[2]}")
                notes.append(row)
    if not notes:
        print("Заметок за эту дату не найдено.")