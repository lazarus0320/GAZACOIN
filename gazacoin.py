import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
import selectcoin
import pyupbit
from PyQt5.QtCore import *
from boxstudy import Buycoin
from MarketOrder import MarketOrder
import pygame



tickers = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-LTC', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES', 'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-REP', 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-EOS', 'KRW-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL', 'KRW-POLY', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT', 'KRW-IOST', 'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA', 'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-THETA', 'KRW-QKC', 'KRW-BTT', 'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MED', 'KRW-MLK', 'KRW-STPT', 'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA', 'KRW-HIVE', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-HUNT', 'KRW-PLA', 'KRW-DOT', 'KRW-SRM', 'KRW-MVL', 'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META', 'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM', 'KRW-DOGE', 'KRW-STRK', 'KRW-PUNDIX', 'KRW-FLOW', 'KRW-DAWN', 'KRW-AXS', 'KRW-STX', 'KRW-XEC', 'KRW-SOL', 'KRW-MATIC', 'KRW-NU', 'KRW-AAVE', 'KRW-1INCH', 'KRW-ALGO', 'KRW-NEAR']

form_class = uic.loadUiType("resource/gazacoin.ui")[0]
# chart.py의 ChartWidget 클래스
# graph.py의 QChartView 클래스
# overview.py의 OverviewWidget 클래스
# orderbook.py의 OrderbookWidget 클래스를 Qt Designer에서 메인으로 승격시키도록 했음.

class ListbuyWorker(QThread):    ## 쓰레드 사용을 위한 클래스 선언
    data_seed = pyqtSignal(list) # 딕셔너리 형태로 데이터를 전달할 시그널 정의
    
    def __init__(self):     # ticker는 코인의 약어
        super().__init__()
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림
    def run(self):
        while self.alive:
            buycurr = []
            for selectcoin.coin in selectcoin.coin_dict:
                if selectcoin.coin['wait'] == True:
                    buycurr.append(pyupbit.get_current_price(selectcoin.coin['ticker']))
            self.data_seed.emit(buycurr)

             # 업비트 호가창을 매수/매도 각각 15개씩만 얻어옴 (딕셔너리형태)
            time.sleep(0.5)    # 초당 20번 수행
            #self.data_seed.emit(waitCurrPrice)    # 딕셔너리 형태 호가 정보를 슬롯으로 전달
    
    def close(self):
        self.alive = False


class Userdata():
    
    def __init__(self):
        super().__init__()

        
class MainWindow(QMainWindow, form_class, Userdata):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        
        self.lw = ListbuyWorker()
        self.lw.data_seed.connect(self.Listordernow)
        self.lw.start()
        # pygame.mixer.init()
        # pygame.mixer.music.load("resource/hawaii.mp3")
        # pygame.mixer.music.set_volume(0.3)
        # pygame.mixer.music.play(-1)
        self.setupUi(self)
        self.LimitOrder_Btn.clicked.connect(self.click_LimitOrder_Btn)
        self.LimitSell_Btn.clicked.connect(self.click_LimitSell_Btn)
        self.MarketOrder_Btn.clicked.connect(self.click_MarketOrder_Btn)
        self.MarketSell_Btn.clicked.connect(self.click_MarketSell_Btn)
        self.button_help.clicked.connect(self.clickBtn_help)
        self.myCoin_Btn.clicked.connect(self.click_myCoin_Btn)
        self.nonContract_Btn.clicked.connect(self.click_nonContract_Btn)
        
        self.lineEdit.returnPressed.connect(self.search_coin)
        self.setWindowTitle("가즈아 온라인 모의투자 ver 0.1")
        self.setWindowIcon(QIcon("resource/doge.png"))

        self.nonContractcount = 0
        
        self.textEdit.append("가즈아 온라인 모의투자 ver 0.1")
        
        with open("C:/Coingame/resource/savekey.txt", 'r') as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            if apikey == "NONE" and seckey == "NONE":
                self.textEdit.append("저장된 데이터가 없습니다. 새로운 데이터를 구성합니다.")
                
                self.textEdit.append("시작하기 전에 도움말을 참고하세요.")
    
            f.close()
        
        
            
    @pyqtSlot(list) 
    def Listordernow(self, buycurr):        ### 지정가 매수
        
        coincount = 1
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['wait'] == True:
                if selectcoin.coin['buyprice'] >= buycurr[coincount-1] and selectcoin.coin['lowerbuy'] == True:
                    ticker = selectcoin.coin['ticker']
                    buyprice = selectcoin.coin['buyprice']
                    total_price = selectcoin.coin['buyprice'] * selectcoin.coin['buyamount']
                    selectcoin.coin['own'] = True
                    selectcoin.coin['wait'] = False
                    selectcoin.coin['lowerbuy'] == False
                    selectcoin.coin['rtotalbuy'] += selectcoin.coin['totalbuy']
                    selectcoin.coin['rtotalamount'] += selectcoin.coin['totalamount']
                    selectcoin.coin['totalbuy'] = 0
                    selectcoin.coin['totalamount'] = 0
                    curr = buycurr[coincount-1]
                    self.textEdit.append(f"{ticker} 를 평단가 {buyprice:,.2f} 원에 {total_price:,.2f} 원만큼 매수했습니다. 코인 현재가 {curr} 하향구매")
                    if len(buycurr) == (coincount):
                        break;
                    coincount += 1  # 현재가와 같으므로 카운트 업
                elif selectcoin.coin['buyprice'] <= buycurr[coincount-1] and selectcoin.coin['lowerbuy'] == False:
                    ticker = selectcoin.coin['ticker']
                    buyprice = selectcoin.coin['buyprice']
                    total_price = selectcoin.coin['buyprice'] * selectcoin.coin['buyamount']
                    selectcoin.coin['own'] = True
                    selectcoin.coin['wait'] = False
                    selectcoin.coin['rtotalbuy'] += selectcoin.coin['totalbuy']
                    selectcoin.coin['rtotalamount'] += selectcoin.coin['totalamount']
                    selectcoin.coin['rfee'] += selectcoin.coin['fee']
                    selectcoin.coin['fee'] = 0
                    selectcoin.coin['totalbuy'] = 0
                    selectcoin.coin['totalamount'] = 0
                    curr = buycurr[coincount-1]
                    self.textEdit.append(f"{ticker} 를 평단가 {buyprice:,.2f} 원에 {total_price:,.2f} 원만큼 매수했습니다. 코인 현재가 {curr}")
                    if len(buycurr) == (coincount):
                        break;
                    coincount += 1  # 현재가와 같으므로 카운트 업
                else : 
                    coincount += 1    # 현재가와 다르지만 검사 했으므로 카운트 업
    
    def click_LimitOrder_Btn(self):
        limitorder = Buycoin()
        limitorder.exec_()      # 다른 모듈의 다이얼로그를 실행시킨다.
        if selectcoin.buychecker == True:
            self.textEdit.append("매수 주문이 완료되었습니다.")
            selectcoin.buychecker = False
    
    def click_LimitSell_Btn(self):
        pass
    
    def click_MarketOrder_Btn(self):
        marketorder = MarketOrder()
        marketorder.exec_()
        if selectcoin.buychecker == True:
            self.textEdit.append("매수 주문이 완료되었습니다.")
            selectcoin.buychecker = False
    
    def click_MarketSell_Btn(self):
        pass
            
    def  click_myCoin_Btn(self):        ### 거래내역조회
        coincount = 0
        self.textEdit.append(f'현재 잔고 : {selectcoin.user_money:,.2f} 원')
        for selectcoin.coin in selectcoin.coin_dict:      # 코인의 각 항목에 접근해서 구매한 코인의 own을 True, buyprice라는 새 항목을 만들어 매수가격 추가
            if selectcoin.coin['own'] == True:
                coincount += 1
                ticker = selectcoin.coin['ticker']
                buyprice = selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount']
                buyamount = selectcoin.coin['rtotalamount']
                fee = selectcoin.coin['rfee']
                totalbuyprice = buyprice * buyamount
                self.textEdit.append(f"{coincount}.  코인이름 : {ticker}  평단 : {buyprice:,.2f}  수량 : {buyamount:,.2f}  매수 채결액 : {totalbuyprice:,.2f}   수수료 : {fee:,.2f}")
                
        if coincount == 0:
            self.textEdit.append("보유한 코인이 없습니다.")

    def click_nonContract_Btn(self):        ### 미체결 조회
        cointcounter = 0
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['wait'] == True:
                self.textEdit.append("미체결 코인의 번호를 입력하면 거래 취소가 가능합니다.")
                cointcounter += 1
                ticker = selectcoin.coin['ticker']
                buyprice = selectcoin.coin['buyprice']
                buyamount = selectcoin.coin['buyamount']
                fee = selectcoin.coin['fee']
                self.textEdit.append(f"{cointcounter}. {ticker} 거래수량 : {buyamount:,.2f}  거래단가 : {buyprice:,.2f}  거래금액 : {buyamount*buyprice:,.2f}   수수료: {fee:,.2f}")
                
        self.nonContractcount = cointcounter
        if cointcounter == 0:
            self.textEdit.append("미체결 거래가 없습니다.")
        
            
    def search_coin(self):      ### 코인 선택
        self.textEdit.append(self.lineEdit.text())
        if "KRW-" in self.lineEdit.text():
            for ticker in tickers:
                if self.lineEdit.text() == ticker:
                    self.textEdit.append(f'{ticker}정보를 불러옵니다.')             
                    selectcoin.mainticker = ticker
                    break; 
                
        if "cancel-" in self.lineEdit.text():   #미체결 매수 취소
            for selectcoin.coin in selectcoin.coin_dict:
                if selectcoin.coin['ticker'] in self.lineEdit.text():
                    selectcoin.user_money += (selectcoin.coin['totalbuy'] + selectcoin.coin['fee'])  # 돈 반환
                    selectcoin.coin['wait'] = False
                    selectcoin.coin['buyprice'] = 0
                    selectcoin.coin['buyamount'] = 0
                    selectcoin.coin['totalbuy'] = 0
                    selectcoin.coin['totalamount'] = 0
                    selectcoin.coin['lowerbuy'] = False
                    selectcoin.coin['fee'] = 0
                    
                    ticker = selectcoin.coin['ticker']
                    self.textEdit.append(f'{ticker}의 주문이 취소되었습니다.')
                    
                
        self.lineEdit.clear()
        
    def clickBtn_help(self):
        self.textEdit.append("가즈아 온라인 모의투자는 업비트 가상화폐 거래소의 실시간 데이터를 바탕으로 모의 투자를 체험하는 게임입니다. 매매 시작을 누르면 거래를 시작할 수 있습니다. 매매 중단 버튼을 누르면 데이터가 저장됩니다. 게임을 종료하기 전에 반드시 매매 중단 버튼을 눌러주세요.")
        
        

                
    def closeEvent(self, event):
        quit_msg = "그만할래요?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            #pygame.mixer.music.stop()
            event.accept()
          
            
            
        else:
            event.ignore()


 
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())