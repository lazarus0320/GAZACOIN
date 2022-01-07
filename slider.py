import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 설정
        self.setGeometry(200, 100, 300, 300)  # x, y, w, h
        self.setWindowTitle('QSlider Sample Window')
        my_balance = 400000
        # QSliter  추가
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(10, 10, 200, 30)
        self.slider.setRange(0, my_balance)
        self.slider.setTickInterval(20)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.valueChanged.connect(self.value_changed)
        
        # QSlider 데이터를 표시할 라벨
 
        self.label.setValidator(QIntValidator(self))
        self.label.setGeometry(10, 50, 100, 30)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label.setStyleSheet("border-radius: 5px;"
                                  "border: 1px solid gray;"
                                  "background-color: #BBDEFB")
        self.label.textChanged.connect(lambda x: self.slider.setValue(int(x)))
        

    # 슬라이드 시그널 valueChanged 연결 함수
    def value_changed(self, value):
        self.label.setText(str(value))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
