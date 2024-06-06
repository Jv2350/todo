from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # add item button
        self.add_pushButton_1 = QtWidgets.QPushButton(self.centralwidget, clicked=self.add_item)
        self.add_pushButton_1.setGeometry(QtCore.QRect(590, 80, 161, 51))
        font.setPointSize(16)
        self.add_pushButton_1.setFont(font)
        self.add_pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_pushButton_1.setObjectName("add_pushButton_1")

        # list widget: To display the items
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 151, 701, 321))
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setObjectName("listWidget")

        # line Edit: Input for new item
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 501, 51))
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setObjectName("lineEdit")

        # clear The List button
        self.clear_all_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=self.clear_all_item)
        self.clear_all_pushButton_2.setGeometry(QtCore.QRect(419, 490, 331, 60))
        self.clear_all_pushButton_2.setFont(font)
        self.clear_all_pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_all_pushButton_2.setObjectName("clear_all_pushButton_2")

        # Button: Delete Item from List
        self.delete_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=self.delete_item)
        self.delete_pushButton_3.setGeometry(QtCore.QRect(50, 490, 331, 60))
        self.delete_pushButton_3.setFont(font)
        self.delete_pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_pushButton_3.setObjectName("delete_pushButton_3")

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # add item to the list
    def add_item(self):
        item = self.lineEdit.text()
        self.listWidget.addItem(item)
        self.lineEdit.setText("")

    # delete the selected item from the list
    def delete_item(self):
        clicked = self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)

    # clear all items from the list
    def clear_all_item(self):
        self.listWidget.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.add_pushButton_1.setText(_translate("MainWindow", "Add Item"))
        self.label.setText(_translate("MainWindow", "To Do List"))
        self.clear_all_pushButton_2.setText(_translate("MainWindow", "Clear The List"))
        self.delete_pushButton_3.setText(_translate("MainWindow", "Delete Item from List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
