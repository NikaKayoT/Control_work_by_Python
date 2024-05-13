import csv
import datetime
def add_note(title, message):
    with open('notes.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([str(datetime.datetime.now()), title, message])        