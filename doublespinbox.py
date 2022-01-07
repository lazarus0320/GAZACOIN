import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import math

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.money = 1000000        #주문 가능 잔고
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 300, 300)
        self.currentprice = 130000
        self.totalprice = 0
        label1 = QLabel("매수가격: ", self)
        label1.move(10, 20)
        self.DoublespinBox = QDoubleSpinBox(self)
        self.DoublespinBox.setValue(self.currentprice)
        self.DoublespinBox.move(70, 25)
        self.DoublespinBox.resize(80, 22)
        self.DoublespinBox.setRange(1, 99999999)
        
        
        if self.DoublespinBox.value() < 10:
            self.DoublespinBox.setSingleStep(0.01)
            
        elif 10 <= self.DoublespinBox.value() < 100 :
             self.DoublespinBox.setSingleStep(0.1)
        
        elif 100 <= self.DoublespinBox.value() < 1000 :
             self.DoublespinBox.setSingleStep(1)
             
        elif 1000 <= self.DoublespinBox.value() < 10000 :
             self.DoublespinBox.setSingleStep(5)
        
        elif 10000 <= self.DoublespinBox.value() < 100000 :
             self.DoublespinBox.setSingleStep(10)
        
        elif 100000 <= self.DoublespinBox.value() < 1000000 :
             self.DoublespinBox.setSingleStep(50)
        
        elif 1000000 <= self.DoublespinBox.value() < 10000000 :
             self.DoublespinBox.setSingleStep(500)
             
        elif 10000000 <= self.DoublespinBox.value() :
             self.DoublespinBox.setSingleStep(1000)
        self.DoublespinBox.valueChanged.connect(self.DoublespinBoxChanged)
       
        label2 = QLabel("주문수량: ", self)
        label2.move(10, 50)
        self.DoublespinBox2 = QDoubleSpinBox(self)
        self.DoublespinBox2.move(70, 55)
        self.DoublespinBox2.resize(80, 22)
        max_range = float(self.money/self.DoublespinBox.value())
        self.DoublespinBox2.setRange(0, max_range)
        self.DoublespinBox2.valueChanged.connect(self.DoublespinBoxChanged2)

        self.mylabel = QLabel(f"주문가능(잔고) : {self.money:,} 원", self)
        self.mylabel.move(10, 100)
        self.mylabel.resize(250, 22)
       
        self.label3 = QLabel(self)
        self.label3.move(10, 130)
        self.label3.resize(250, 22)
       
        self.label4 = QLabel(self)
        self.label4.move(10, 160)
        self.label4.resize(250, 22)
       
        self.label5 = QLabel(self)
        self.label5.move(10, 190)
        self.label5.resize(300, 22)
       
        self.slider = QSlider(Qt.Horizontal, self)
        max_range = int(self.money/self.DoublespinBox.value())
        self.slider.setRange(0, max_range)
        self.slider.move(25, 0)
        self.slider.resize(250, 22)
        self.slider.setTickPosition(QSlider.NoTicks)
        self.slider.valueChanged.connect(self.slide_changed)
        self.DoublespinBox2.valueChanged.connect(self.slider.setValue)
        
        self.labelcheck = QLabel(self)
        self.labelcheck.move(10, 220)
        self.labelcheck.resize(300, 22)
        
        self.button = QPushButton(self)
        self.button.move(10, 260)
        self.button.resize(280, 30)
        self.button.setText('매수')
        self.button.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        if self.currentprice < 10:
            val = round(self.DoublespinBox.value(), 2)
        elif 10 <= self.currentprice < 100:
            val = round(self.DoublespinBox.value(), 1)
        elif 100 <= self.currentprice < 1000:
            val = round(self.DoublespinBox.value())
        elif 1000 <= self.currentprice < 10000:
            unval = self.DoublespinBox.value()
            val = round((unval)/5) * 5
        elif 10000 <= self.currentprice < 100000:
            unval = self.DoublespinBox.value()
            val = round((unval)/10) * 10
        elif 100000 <= self.currentprice < 1000000:
            unval = self.DoublespinBox.value()
            val = round((unval)/50) * 50
        elif 1000000 <= self.currentprice < 10000000:
            unval = self.DoublespinBox.value()
            val = round((unval)/500) * 500
        elif 10000000 <= self.currentprice < 100000000:
            unval = self.DoublespinBox.value()
            val = round((unval)/1000) * 1000
        val2 = self.DoublespinBox2.value()
        msg = QMessageBox()
        msg.setGeometry(850, 500, 300, 300)
        msg.setWindowTitle('WARNING')
        msg.setText(f'매수가격 : {val:,}  주문수량 : {val2:,}\n주문총액 : {val*val2:,.2f} 원에 매수합니다.')
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        result = msg.exec_()
        
        


    def DoublespinBoxChanged(self):
        val1 = self.DoublespinBox.value()
        val2 = self.DoublespinBox2.value()
        if self.currentprice < 10.0:
            self.DoublespinBox.setSingleStep(0.01)
            self.labelcheck.setText('매수가격은 0.01단위로 주문 가능합니다.')
        elif 10 <= self.currentprice <= 100 :
            self.DoublespinBox.setSingleStep(0.1)
            self.labelcheck.setText('매수가격은 0.1단위로 주문 가능합니다.')
        elif 100 <= self.currentprice < 1000 :
            self.DoublespinBox.setSingleStep(1)
            self.labelcheck.setText('매수가격은 1단위로 주문 가능합니다.')
        elif 1000 <= self.currentprice < 10000 :
            self.DoublespinBox.setSingleStep(5)
            self.labelcheck.setText('매수가격은 5단위로 주문 가능합니다.')
        elif 10000 <= self.currentprice < 100000 :
            self.DoublespinBox.setSingleStep(10)
            self.labelcheck.setText('매수가격은 10단위로 주문 가능합니다.')
        elif 100000 <= self.currentprice < 1000000 :
            self.DoublespinBox.setSingleStep(50)
            self.labelcheck.setText('매수가격은 50단위로 주문 가능합니다.')
        elif 1000000 <= self.currentprice < 10000000 :
            self.DoublespinBox.setSingleStep(500)
            self.labelcheck.setText('매수가격은 500단위로 주문 가능합니다.')
        elif 10000000 <= self.currentprice :
            self.DoublespinBox.setSingleStep(1000)
            self.labelcheck.setText('매수가격은 1000단위로 주문 가능합니다.')
        self.label3.setText(f'매수가격 : {val1:,.2f} 원')
        self.total_buy_price(val1, val2)
        self.max_unit = float(self.money/self.DoublespinBox.value())
        self.slider.setRange(0, self.max_unit)

    def DoublespinBoxChanged2(self):
        val1 = self.DoublespinBox.value()
        val2 = self.DoublespinBox2.value()
        self.slide_changed()
        self.label4.setText(f'주문수량 : {val2:,.6f} 개')
        self.total_buy_price(val1, val2)

    def slide_changed(self):
        val1 = self.DoublespinBox.value()
        val2 = self.slider.value()
        self.label4.setText(f'주문수량 : {val2:,.6f} 개')
        self.total_buy_price(val1, val2)
        self.DoublespinBox2.setValue(val2)
    
    
    # 그냥 범위에 맞는 최소 단위까지 반올림시키고 결재진행할 것.
    
    def total_buy_price(self, val1, val2):
        #self.totalprice = val1*val2
        self.label5.setText(f'주문총액 : {val1*val2:,.2f} 원에 매수합니다. ({val1*val2/self.money*100:.2f}%)')
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
