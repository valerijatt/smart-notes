from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit, QLineEdit, QInputDialog
import json

with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

#with open("notes.json","w", encoding="utf-8") as file:
    #json.dump(notes, file)
def show_note():
    name = notes_list.selectedItems()[0].text()
    text_edit.setText(notes[name]["текст"])
    tags_list.clear()
    tags_list.addItems(notes[name]["Теги"])

def add_note():
    note_name, ok = QInputDialog.getText(main_win, "Добавить заметку","Название заметки:")
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "Теги": []}
        notes_list.addItem(note_name)

def del_note():
    if notes_list.selectedItems():
        name = notes_list.selectedItems()[0].text()
        del notes[name]
        notes_list.clear()
        tags_list.clear()
        text_edit.clear()
        notes_list.addItems(notes)

def save_notes():
    if notes_list.selectedItems():
        name = notes_list.selectedItems()[0].text()
        textx = text_edit.toPlainText()
        notes[name]["текст"] = textx        

def add_tag():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = text.text()
        if not tag in notes[key]["Теги"]:
            notes[key]["Теги"].append(tag)
            tags_list.addItem(tag)
            text.clear()
    
def del_tag():
    if tags_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = tags_list.selectedItems()[0].text()
        notes[key]["Теги"].remove(tag)
        tags_list.clear()
        tags_list.addItems(notes[key]["Теги"])

def search_tag():
    tag = text.text()
    if search_notes.text() == "Искать заметки по тегу" and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["Теги"]:
                notes_filtered[note]= notes[note]
        search_notes.setText("Сбросить поиск")
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes_filtered)
    elif search_notes.text() == "Сбросить поиск" :
        text.clear()
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes)
        search_notes.setText("Искать заметки по тегу") 
    else:
        pass      

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Умные заметки')
main_win.resize(900,600)
text_edit = QTextEdit()
notes_list = QListWidget()
tags_list = QListWidget()
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить замету')
pin_note = QPushButton('Добавить к заметке')
unpin_note = QPushButton('Открепить от заметки')
search_notes = QPushButton('Искать заметки по тегу')
n_list_text = QLabel('Список заметок')
t_list_text = QLabel('Список тегов')
text = QLineEdit()
text.setPlaceholderText('Введите тег...')

main_layout = QHBoxLayout()
buttons1_layout = QHBoxLayout()
buttons2_layout = QHBoxLayout()
right_column = QVBoxLayout()
#прекрипление лэйаутов
buttons1_layout.addWidget(create_note)
buttons1_layout.addWidget(delete_note)
buttons2_layout.addWidget(pin_note)
buttons2_layout.addWidget(unpin_note)
right_column.addWidget(n_list_text)
right_column.addWidget(notes_list)
right_column.addLayout(buttons1_layout)
right_column.addWidget(save_note)
right_column.addWidget(t_list_text)
right_column.addWidget(tags_list)
right_column.addWidget(text)
right_column.addLayout(buttons2_layout)
right_column.addWidget(search_notes)
main_layout.addWidget(text_edit)
main_layout.addLayout(right_column)
main_win.setLayout(main_layout)
#оснавной код
notes_list.addItems(notes)
notes_list.itemClicked.connect(show_note)
create_note.clicked.connect(add_note)
delete_note.clicked.connect(del_note)
save_note.clicked.connect(save_notes)
pin_note.clicked.connect(add_tag)
unpin_note.clicked.connect(del_tag)
search_notes.clicked.connect(search_tag)
main_win.show()
app.exec_()

with open("notes.json","w", encoding="utf-8") as file:
    json.dump(notes, file)







