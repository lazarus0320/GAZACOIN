import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
import selectcoin
import pyupbit
from PyQt5.QtCore import *
from boxstudy import Buycoin

waitCurrPrice=[]

class ListbuyWorker(QThread):    ## 쓰레드 사용을 위한 클래스 선언
    #data_seed = pyqtSignal(list) # 딕셔너리 형태로 데이터를 전달할 시그널 정의
    
    def __init__(self):     # ticker는 코인의 약어
        super().__init__()
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림
    def run(self):
        while self.alive:
            for selectcoin.coin in selectcoin.coin_dict:
                if selectcoin.coin['wait'] == True:
                    selectcoin.coin['buyamount'] = pyupbit.get_current_price(selectcoin.coin['ticker'])
            

             # 업비트 호가창을 매수/매도 각각 15개씩만 얻어옴 (딕셔너리형태)
            time.sleep(0.5)    # 초당 20번 수행
            #self.data_seed.emit(waitCurrPrice)    # 딕셔너리 형태 호가 정보를 슬롯으로 전달
    
    def close(self):
        self.alive = False
        
        
class Listmain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lw = ListbuyWorker()
        #self.lw.data_seed.connect(self.Listordernow)
        self.lw.start()
        
    for selectcoin.coin in selectcoin.coin_dict:
        if selectcoin.coin['wait'] == True:
            if selectcoin.coin['buyprice'] == selectcoin.coin['buyamount']:
                print("개같이 매수 성공~~~~!!!!끼요오옷!!!")

        
    # @pyqtSlot(list)
    # def Listordernow(self, data):
    #     for i, selectcoin.coin in enumerate(selectcoin.coin_dict):
    #         if selectcoin.coin['wait'] == True:
    #             if data[i] == selectcoin.coin['buyprice']:
    #                 selectcoin.coin['wait'] == False
    #                 selectcoin.coin['own'] == True
    #                 coinname = selectcoin.coin['ticker']
    #                 coinprice = selectcoin.coin['buyprice']
    #                 print(f"{coinname} {coinprice}원에 매수 성공!!")
    #         else :
    #             break
        
            

app = QApplication(sys.argv)
mywindow = Listmain()
mywindow.show()
app.exec_()