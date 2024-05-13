import csv
from list import list_notes
def delete_note(index):
    notes = list_notes()
    if 0 < index <= len(notes):
        del notes[index - 1]
        with open('notes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(notes)
        print("Заметка успешно удалена.")
    else:
        print("Заметка с таким номером не найдена.")