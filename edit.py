import csv
import datetime
def edit_note(index, title, message):
    notes = list_notes()
    if 0 < index <= len(notes):
        notes[index - 1] = [str(datetime.datetime.now()), title, message]
        with open('notes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(notes)
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка с таким номером не найдена.")