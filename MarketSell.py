import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyupbit
import selectcoin
import time

class MarketSellWorker(QThread):
    data_seed = pyqtSignal(float)
    
    def __init__(self):     # ticker는 코인의 약어
        super(MarketSellWorker, self).__init__()
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
        self.quit()
        self.wait(3000)
class MarketSell(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.show()
        
        self.ms = MarketSellWorker()
        self.ms.data_seed.connect(self.get_data)
        self.ms.start()

    def setupUI(self):
        self.setGeometry(600, 400, 300, 160)
        self.setWindowTitle('시장가 매도')
        self.setWindowIcon(QIcon("resource/doge.png"))
        self.ticker = selectcoin.mainticker
        self.cp = pyupbit.get_current_price(self.ticker)
        self.sel_amount = 0
        '''
        
        
        '''
        for selectcoin.coin in selectcoin.coin_dict:
            if self.ticker == selectcoin.coin['ticker']:
                self.rtotalbuy = selectcoin.coin['rtotalbuy']
                self.rtotalamount = selectcoin.coin['rtotalamount']


        
        self.orderLabel = QLabel(f"{selectcoin.mainticker}  수량 : {self.rtotalamount:,} 개", self)
        self.orderLabel.move(10, 20)
        
        self.button10 = QPushButton(self)
        self.button10.move(15, 50)
        self.button10.resize(60, 30)
        self.button10.setText('10%')
        self.button10.clicked.connect(self.button10_clicked)
        
        self.button25 = QPushButton(self)
        self.button25.move(85, 50)
        self.button25.resize(60, 30)
        self.button25.setText('25%')
        self.button25.clicked.connect(self.button25_clicked)
        
        self.button50 = QPushButton(self)
        self.button50.move(155, 50)
        self.button50.resize(60, 30)
        self.button50.setText('50%')
        self.button50.clicked.connect(self.button50_clicked)
        
        self.button_all = QPushButton(self)
        self.button_all.move(225, 50)
        self.button_all.resize(60, 30)
        self.button_all.setText('최대')
        self.button_all.clicked.connect(self.button_all_clicked)
        
        self.amountLabel = QLabel("수량 :", self)
        self.amountLabel.move(10, 90)
        self.amountLabel.resize(40, 22)
        
        self.amountLabel_val = QLabel(self)
        self.amountLabel_val.move(50, 90)
        self.amountLabel_val.resize(100, 22)
        
        self.button = QPushButton(self)
        self.button.move(10, 120)
        self.button.resize(280, 30)
        self.button.setText('매도')
        self.button.clicked.connect(self.button_clicked)

    @pyqtSlot(float)
    def get_data(self, data):
        self.cp = data
        self.nowvalue = self.rtotalamount*self.cp   # 코인수량x현재가 = 실시간 총액
        self.mylabel = QLabel(f"총액 : {self.nowvalue:,} 원", self)
        self.mylabel.move(10, 30)
        self.mylabel.resize(250, 22)
        
    def button10_clicked(self):
        self.sel_amount = self.rtotalamount * 0.1
        self.amountLabel_val.setText(str(float(self.sel_amount)))
    def button25_clicked(self):
        self.sel_amount = self.rtotalamount * 0.25
        self.amountLabel_val.setText(str(float(self.sel_amount)))
    
    def button50_clicked(self):
        self.sel_amount = self.rtotalamount * 0.5
        self.amountLabel_val.setText(str(float(self.sel_amount)))
    
    def button_all_clicked(self):
        self.sel_amount = self.rtotalamount
        self.amountLabel_val.setText(str(self.rtotalamount))
        
    def closeEvent(self, event):    # 스레드 종료를 위해 QWidget의 메서드를 오버라이딩, 메인 위젯 종료시 closeEvent 메서드 실행
        self.ms.close()


        
    def button_clicked(self):

        ticker = selectcoin.mainticker
       
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['ticker'] == ticker:
                averageprice = selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount'] #당시주가, 평단가
                sellbenefit = (self.cp*self.sel_amount) - (averageprice*self.sel_amount) # 매도차익(음수 혹은 양수)
                #sellpercent = sellbenefit / (self.cp * val1) * 100
                #selectcoin.coin['rfee'] += val1 * 0.05
                selectcoin.coin['buyamount'] = self.sel_amount
                selectcoin.coin['buyprice'] = self.cp
                selectcoin.user_money += (self.sel_amount*self.cp)*0.9995
                selectcoin.coin['rtotalamount'] -= self.sel_amount
                selectcoin.coin['rtotalbuy'] -= (averageprice*self.sel_amount)
                
                if selectcoin.coin['rtotalbuy'] <= 0:
                    selectcoin.coin['own'] = False
                    selectcoin.coin['rtotalamount'] = 0
                    selectcoin.coin['rtotalbuy'] = 0
                selectcoin.accepted = True
                selectcoin.coin['sellchecker'] = True
        self.accept()