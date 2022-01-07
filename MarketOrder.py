import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyupbit
import selectcoin
import time


class MarketOrderWorker(QThread):
    data_seed = pyqtSignal(float)
    
    def __init__(self):     # ticker는 코인의 약어
        super().__init__()
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림
    def run(self):
        while self.alive:
            data = pyupbit.get_current_price(selectcoin.mainticker)
            self.data_seed.emit(data)

             # 업비트 호가창을 매수/매도 각각 15개씩만 얻어옴 (딕셔너리형태)
            time.sleep(0.5)    # 초당 20번 수행
            #self.data_seed.emit(waitCurrPrice)    # 딕셔너리 형태 호가 정보를 슬롯으로 전달
    
    def close(self):
        self.alive = False

class MarketOrder(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.show()
        
        self.mw = MarketOrderWorker()
        self.mw.data_seed.connect(self.get_data)
        self.mw.start()

    def setupUI(self):
        self.setGeometry(600, 400, 300, 140)
        self.setWindowTitle('시장가 매수')
        self.setWindowIcon(QIcon("resource/doge.png"))
        ticker = selectcoin.mainticker
        self.cp = pyupbit.get_current_price(ticker)
        '''
        주문 수량 = 주문총액 / 매수가격
        슬라이드값 = 주문가능 잔고
        주문총액, 슬라이드값은 같이 움직인다.
        주문총액은 주문가능 잔고를 넘어서면 안된다.
        주문수량이 표시되지 않아도 selectcoin모듈에 값을 넘겨줘야한다.
        
        
        
        '''
       
        
        self.slider = QSlider(Qt.Horizontal, self)
        max_range = int(selectcoin.user_money)
        self.slider.setRange(0, max_range)
        self.slider.move(25, 0)
        self.slider.resize(250, 22)
        self.slider.setTickPosition(QSlider.NoTicks)
        self.slider.valueChanged.connect(self.slide_changed)
  
        self.mylabel = QLabel(f"주문가능(잔고) : {selectcoin.user_money:,} 원", self)
        self.mylabel.move(10, 30)
        self.mylabel.resize(250, 22)

        self.percent = QLabel(self)
        self.percent.move(200, 30)
        self.percent.resize(50, 22)
        
        self.orderLabel = QLabel("주문총액: ", self)
        self.orderLabel.move(10, 70)
        self.orderLine = QSpinBox(self)
        self.orderLine.setRange(0, max_range)
        self.orderLine.move(70, 65)
        self.orderLine.resize(200, 22)
        
        self.orderLine.valueChanged.connect(self.orderLine_changed)
        
        self.button = QPushButton(self)
        self.button.move(10, 100)
        self.button.resize(280, 30)
        self.button.setText('매수')
        self.button.clicked.connect(self.button_clicked)

    @pyqtSlot(float)
    def get_data(self, data):
        self.cp = data
        
    
    def slide_changed(self):
        val = self.slider.value()
        self.orderLine.setValue(val)
        self.percent.setText(f"({val/selectcoin.user_money*100:.2f}%)")
        
    def orderLine_changed(self):
        val = self.orderLine.value()
        self.slider.setValue(val)
        self.percent.setText(f"({val/selectcoin.user_money*100:.2f}%)")
        
    def button_clicked(self):
        val1 = self.orderLine.value()   # 주문총액
        val2 = val1 / self.cp   # 주문 수량
        ticker = selectcoin.mainticker
       
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['ticker'] == ticker:
                selectcoin.coin['rfee'] += val1 * 0.05
                selectcoin.coin['rtotalbuy'] += val1
                selectcoin.coin['rtotalamount'] += val2
                selectcoin.coin['own'] = True
                selectcoin.buychecker = True
                selectcoin.user_money -= (selectcoin.coin['fee'] + val1)
        self.accept()
        
        