from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class second(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("resource/multi_2.ui", self)
        self.show()

class first(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("resource/multi_1.ui", self)
        
        self.pushButton.clicked.connect(self.second_window)
        
        self.show()
        
    def second_window(self):
        window_2 = second()
        window_2.exec_()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = first()
    window.show()
    app.exec_()
       