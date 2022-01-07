import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import pyupbit
import selectcoin
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtCore import QCoreApplication
import time

class ListbuyWorker(QThread):    ## 쓰레드 사용을 위한 클래스 선언
    data_seed = pyqtSignal(float) # 딕셔너리 형태로 데이터를 전달할 시그널 정의
    
    def __init__(self, ticker):     # ticker는 코인의 약어
        super().__init__()
        self.ticker = ticker
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림

    def run(self):
        while self.alive:
            self.ticker = 'KRW-NEAR'
            data = pyupbit.get_current_price(self.ticker) # 업비트 호가창을 매수/매도 각각 15개씩만 얻어옴 (딕셔너리형태)
            time.sleep(0.05)    # 초당 20번 수행
            self.data_seed.emit(data)    # 딕셔너리 형태 호가 정보를 슬롯으로 전달
    
    def close(self):
        self.alive = False  # self.alive가 False전환되면 스레드 종료
        
class ListbuyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lw = ListbuyWorker('KRW-NEAR') # 스레드의 객체 ow 선언
        self.lw.data_seed.connect(self.Listbuywait)   # 시그널에게 data를 받으면 updateData메서드에 data인자를 넘겨주도록 설계
        self.lw.start()
    
    def Listbuywait(self, data):
        if data >= 20850:
            print("구매완료~~~~!!!!!")
        else :
            print("구매 대기중...")
            
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    lw = ListbuyWidget()
    lw.show()
    exit(app.exec_())