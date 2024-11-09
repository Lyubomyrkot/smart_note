from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from qt_material import apply_stylesheet
import json



class SmartNotes(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_note()
        self.ui.note_list.itemClicked.connect(self.show_note)

    def load_note(self):
        self.notes = {
            "Нова нотатка": {
                "text": "Тут буде ваші нотатки",
                "tags": [],
            }
        }
        self.ui.note_list.addItems(self.notes)

    def show_note(self):
        self.name = self.ui.note_list.selectedItems()[0].text()#отримуєм назву нотатки
        self.ui.note_title.setText(self.name)
        self.ui.note_text.setText(self.notes[self.name]["text"])
        self.ui.save_btn.clicked.connect(self.save_note)

    def save_note(self):
        self.notes[self.name]["text"] = self.ui.note_text.toPlainText()
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(self.note,file, ensure_ascii=False)


app = QApplication([])
ex = SmartNotes()

apply_stylesheet(app, theme='dark_red.xml')
ex.show()
app.exec()