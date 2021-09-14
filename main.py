import json
import sys

import jsonpath
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from mainWindow import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.print_res)
        self.lineEdit.textChanged.connect(self.print_res)
        self.plainTextEdit.textChanged.connect(self.print_res)
        self.pushButton_1.clicked.connect(self.json_format)
        self.pushButton_2.clicked.connect(self.json_reduce)

    def json_format_check(self):
        json_str = self.plainTextEdit.toPlainText()
        if json_str:
            try:
                json_obj = json.loads(json_str)
            except:
                self.label_4.setText("JSON格式错误")
                self.label_4.setStyleSheet("color:red")
            else:
                self.label_4.setText("JSON格式正确")
                self.label_4.setStyleSheet("color:green")
                return json_obj
        else:
            self.label_4.setText("")
            self.label_4.setStyleSheet("color:black")

    def json_format(self):
        json_obj = self.json_format_check()
        if json_obj:
            s = json.dumps(json_obj, indent=4, ensure_ascii=False, sort_keys=True)
            self.plainTextEdit.setPlainText(s)

    def json_reduce(self):
        json_obj = self.json_format_check()
        if json_obj:
            s = json.dumps(json_obj, ensure_ascii=False, sort_keys=True)
            self.plainTextEdit.setPlainText(s)

    def print_res(self) -> None:
        path = self.lineEdit.text()
        json_obj = self.json_format_check()
        if json_obj and path:
            r = jsonpath.jsonpath(json_obj, path)
            if r:
                r = json.dumps(r, indent=4, ensure_ascii=False, sort_keys=True)
                self.textBrowser.setText(r)
            else:
                self.textBrowser.setText("无匹配结果")
        else:
            self.textBrowser.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
