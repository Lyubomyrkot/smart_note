# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_col = QtWidgets.QVBoxLayout()
        self.left_col.setContentsMargins(0, 0, 0, 0)
        self.left_col.setObjectName("left_col")
        self.new_note = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_note.sizePolicy().hasHeightForWidth())
        self.new_note.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Користувач/Downloads/circle-plus.svg"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.new_note.setIcon(icon)
        self.new_note.setObjectName("new_note")
        self.left_col.addWidget(self.new_note)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Користувач/Downloads/search.svg"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.left_col.addLayout(self.horizontalLayout_3)
        self.note_list = QtWidgets.QListWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note_list.sizePolicy().hasHeightForWidth())
        self.note_list.setSizePolicy(sizePolicy)
        self.note_list.setObjectName("note_list")
        self.left_col.addWidget(self.note_list)
        self.horizontalLayout_2.addLayout(self.left_col)
        self.right_col = QtWidgets.QVBoxLayout()
        self.right_col.setObjectName("right_col")
        self.note_title = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.note_title.setObjectName("note_title")
        self.right_col.addWidget(self.note_title)
        self.note_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.note_text.setObjectName("note_text")
        self.right_col.addWidget(self.note_text)
        self.save_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Користувач/Downloads/download.svg"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.save_btn.setIcon(icon2)
        self.save_btn.setObjectName("save_btn")
        self.right_col.addWidget(self.save_btn)
        self.delete_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Користувач/Downloads/trash.svg"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.delete_btn.setIcon(icon3)
        self.delete_btn.setObjectName("delete_btn")
        self.right_col.addWidget(self.delete_btn)
        self.horizontalLayout_2.addLayout(self.right_col)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_note.setText(_translate("MainWindow", "Додати нову нататку"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Пошук"))
        self.pushButton.setText(_translate("MainWindow", "Шукати"))
        self.note_title.setPlaceholderText(_translate("MainWindow", "Назва замітки"))
        self.note_text.setPlaceholderText(_translate("MainWindow", "Текст замітки"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти"))
        self.delete_btn.setText(_translate("MainWindow", "Видалити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())