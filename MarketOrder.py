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
        super(MarketOrderWorker, self).__init__()
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림
    def run(self):
        while self.alive:
            try:
                data = pyupbit.get_current_price(selectcoin.mainticker)
                self.data_seed.emit(data)

             # 업비트 호가창을 매수/매도 각각 15개씩만 얻어옴 (딕셔너리형태)
                time.sleep(0.5)    # 초당 20번 수행
            #self.data_seed.emit(waitCurrPrice)    # 딕셔너리 형태 호가 정보를 슬롯으로 전달
            except:
                time.sleep(0.5)
    
    def close(self):
        self.alive = False
        self.quit()
        self.wait(3000)

class MarketOrder(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.show()
        
        self.mw = MarketOrderWorker()
        self.mw.data_seed.connect(self.get_data)
        self.mw.start()

    def setupUI(self):
        self.setGeometry(600, 400, 300, 180)
        self.setWindowTitle('시장가 매수')
        self.setWindowIcon(QIcon("resource/doge.png"))
        ticker = selectcoin.mainticker
        try:
            self.cp = pyupbit.get_current_price(ticker)
        except:
            time.sleep(0.5)
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
  
        self.mylabel = QLabel(f"주문가능(잔고) : {selectcoin.user_money:,.2f} 원", self)
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
        
        if selectcoin.mainticker == "KRW-XLM" or selectcoin.mainticker == "KRW-ETH" or selectcoin.mainticker == "KRW-BTC" or selectcoin.mainticker == "KRW-ADA" or selectcoin.mainticker == "KRW-EOS" or selectcoin.mainticker == "KRW-SNT" or selectcoin.mainticker == "KRW-BCH" or selectcoin.mainticker == "KRW-XEM": 
            self.fee_label = QLabel(f"최소 주문금액 : 5000KRW   수수료 : 0.05%", self)
        else: 
            self.fee_label = QLabel(f"최소 주문금액 : 1000KRW   수수료 : 0.05%", self)
        self.fee_label.move(10, 105)
        
        self.orderLine.valueChanged.connect(self.orderLine_changed)
        
        
        self.button = QPushButton(self)
        self.button.move(10, 140)
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
    
    def closeEvent(self, event):    # 스레드 종료를 위해 QWidget의 메서드를 오버라이딩, 메인 위젯 종료시 closeEvent 메서드 실행
        self.mw.close()
        
    def button_clicked(self):
        jumper = False
        buyprice = self.orderLine.value()   # 주문총액
        amount = round(buyprice / self.cp, 8)   # 주문 수량
        ticker = selectcoin.mainticker

        
        if selectcoin.mainticker == "KRW-XLM" or selectcoin.mainticker == "KRW-ETH" or selectcoin.mainticker == "KRW-BTC" or selectcoin.mainticker == "KRW-ADA" or selectcoin.mainticker == "KRW-EOS" or selectcoin.mainticker == "KRW-SNT" or selectcoin.mainticker == "KRW-BCH" or selectcoin.mainticker == "KRW-XEM": 
            if int((self.orderLine.value())) < 5000:
                msg2 = QMessageBox()     
                msg2.setWindowTitle('WARNING')
                msg2.setText("해당 코인의 경우 최소 5000원 이상 주문만 가능합니다.")
                result2 = msg2.exec()
                if result2 == QMessageBox.Ok:
                    self.close
                    jumper = True
        
        elif selectcoin.user_money <= buyprice:
            msg3 = QMessageBox()     
            msg3.setWindowTitle('WARNING')
            msg3.setText("잔액이 부족합니다.(매수 주문시 수수료도 함께 계산됩니다.)")
            result3 = msg3.exec()
            if result3 == QMessageBox.Ok:
                self.close
                jumper = True
    
        else : 
            if int((self.orderLine.value())) < 1000:
                msg2 = QMessageBox()     
                msg2.setWindowTitle('WARNING')
                msg2.setText("해당 코인의 경우 최소 1000원 이상 주문만 가능합니다.")
                result2 = msg2.exec()
                if result2 == QMessageBox.Ok:
                    self.close
                    jumper = True
        
        if jumper == False:  
            for selectcoin.coin in selectcoin.coin_dict:
                if selectcoin.coin['ticker'] == ticker:
                    #수량은 매수에서 손해봐야하므로 수수료로 *0.95
                    #총액은 내가 들인 금액이므로 
                    #fee = val1 * 0.05
                    #selectcoin.coin['rfee'] += (val1 * 0.05)
                    selectcoin.coin['buyprice'] = self.cp   # 현재가로 얼마에 샀는지 표시를 하기 위함
                    selectcoin.coin['buyamount'] = amount
                    #selectcoin.coin['totalbuy'] = val1*0.95
                    selectcoin.coin['rtotalbuy'] += buyprice
                    selectcoin.coin['rtotalamount'] += amount
                    selectcoin.coin['own'] = True
                    selectcoin.coin['buychecker'] = True
                    selectcoin.accepted = True
                    selectcoin.user_money -= (buyprice*1.0005)
                jumper = False
        self.accept()
        