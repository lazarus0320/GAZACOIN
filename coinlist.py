import json
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
import pyupbit 
from pyupbit import WebSocketManager
import time

tickers = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-LTC', 
            'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES', 'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 
            'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-REP']

class CoinlistWorker(QThread):    ## 쓰레드 사용을 위한 클래스 선언
    dataSent = pyqtSignal(dict)
   
    def __init__(self):     # ticker는 코인의 약어
        super().__init__()
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림

    def run(self):
        while self.alive:
            #data = {}

            wm = WebSocketManager("ticker", tickers)
            data = wm.get()
            print(data)
            # for ticker in tickers:
            #     data[ticker] = pyupbit.get_current_price(ticker)
            self.dataSent.emit(data)
            self.msleep(500)
           
    def close(self):
        self.alive = False  # self.alive가 False전환되면 스레드 종료

class CoinlistWidget(QWidget): ## 위젯 받아와서 UI를 띄우는 클래스
    def __init__(self):  # 새창으로 BTC에 대한 호가창 위젯을 띄움
        super().__init__()
        uic.loadUi("C:/Coingame/resource/coinlist.ui", self)
        self.cl = CoinlistWorker() # 스레드의 객체 cl 선언
        self.cl.dataSent.connect(self.updateData)
        self.cl.start() # updateData에 data값을 넘겨주고 실행시킴
        self.cointable.cellClicked.connect(self.cell_clicked)
           
        for i in range(self.cointable.rowCount()):
            item_0 = QTableWidgetItem(str(""))  # 테이블 1열에 문자열 객체 생성
            item_0.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)    # 셀을 오른쪽으로 정렬함. 셀 정렬 :객체.setTextAlignment(Qt.Align방향) | Qt.AlignVCenter)
            self.cointable.setItem(i, 0, item_0) # 테이블 객체.setItem(행번호,열번호,위젯 객체) : 셀에 값을 입력하는 법. 화면에 그려냄

            item_1 = QTableWidgetItem(str(""))
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cointable.setItem(i, 1, item_1)
           
            item_2 = QTableWidgetItem(str(""))
            item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cointable.setItem(i, 2, item_2)
           
            item_3 = QTableWidgetItem(str(""))
            item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cointable.setItem(i, 3, item_3)

    @pyqtSlot(dict)
    def updateData(self, data):     ## 데이터를 받아서 화면에 업데이트
        # coin_ticker_list = list(data.keys())
        # coin_valuse_list = list(data.values())
        # print(coin_ticker_list)
        pass
   
    def cell_clicked(self, row, column): # row : 가로행 column : 세로행
        print(row)
   
    def closeEvent(self, event):    # 스레드 종료를 위해 QWidget의 메서드를 오버라이딩, 메인 위젯 종료시 closeEvent 메서드 실행
        self.cl.close()
       
       
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cl = CoinlistWidget()
    cl.show()
    exit(app.exec_())