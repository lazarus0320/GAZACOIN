import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
import selectcoin
import pyupbit
from PyQt5.QtCore import *
from LimitOrder import LimitOrder
from MarketOrder import *
from MarketSell import *
from LimitSell import LimitSell
from overview import *
import pygame
import os
pygame.init()

buyCoinList = []
tickers = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-LTC', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES', 'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-REP', 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-EOS', 'KRW-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL', 'KRW-POLY', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT', 'KRW-IOST', 'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA', 'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-THETA', 'KRW-QKC', 'KRW-BTT', 'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MED', 'KRW-MLK', 'KRW-STPT', 'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA', 'KRW-HIVE', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-HUNT', 'KRW-PLA', 'KRW-DOT', 'KRW-SRM', 'KRW-MVL', 'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META', 'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM', 'KRW-DOGE', 'KRW-STRK', 'KRW-PUNDIX', 'KRW-FLOW', 'KRW-DAWN', 'KRW-AXS', 'KRW-STX', 'KRW-XEC', 'KRW-SOL', 'KRW-MATIC', 'KRW-NU', 'KRW-AAVE', 'KRW-1INCH', 'KRW-ALGO', 'KRW-NEAR']
buySound = pygame.mixer.Sound("resource/buy.mp3")
sellSound = pygame.mixer.Sound("resource/sell.mp3")
form_class = uic.loadUiType("resource/gazacoin.ui")[0]
# chart.py의 ChartWidget 클래스
# graph.py의 QChartView 클래스
# overview.py의 OverviewWidget 클래스
# orderbook.py의 OrderbookWidget 클래스를 Qt Designer에서 메인으로 승격시키도록 했음.

class ListbuyWorker(QThread):    ## 쓰레드 사용을 위한 클래스 선언
    data_seed = pyqtSignal(list, list) # 딕셔너리 형태로 데이터를 전달할 시그널 정의

    def __init__(self):     # ticker는 코인의 약어
        super(ListbuyWorker, self).__init__()
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림
    def run(self):
        while self.alive:
            buycurr = []
            sellcurr = []
            for selectcoin.coin in selectcoin.coin_dict:
                if selectcoin.coin['wait'] == True and selectcoin.coin['buychecker'] == True:
                    try:
                        buycurr.append(pyupbit.get_current_price(selectcoin.coin['ticker']))
                    except:
                        continue
                if selectcoin.coin['wait'] == True and selectcoin.coin['sellchecker'] == True:
                    try:
                        sellcurr.append(pyupbit.get_current_price(selectcoin.coin['ticker']))
                    except:
                        continue
            self.data_seed.emit(buycurr, sellcurr)

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

        #self.nonContractcount = 0
        
        self.textEdit.append("가즈아 온라인 모의투자 ver 0.1")
        
        with open("C:/Coingame/resource/savekey.txt", 'r') as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            if apikey == "NONE" and seckey == "NONE":
                self.textEdit.append("\n저장된 데이터가 없습니다. 새로운 데이터를 구성합니다.")
                
                self.textEdit.append("시작하기 전에 도움말을 참고하세요.")
    
            f.close()
        
        
            
   
    def Listordernow(self, buycurr, sellcurr):        ### 지정가 매수 접수 , 지정가 매도 접수 실시간 감지
        
        coincount = 1
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['wait'] == True and selectcoin.coin['buychecker'] == True:
                if selectcoin.coin['buyprice'] >= buycurr[coincount-1] and selectcoin.coin['lowerbuy'] == True:
                    ticker = selectcoin.coin['ticker']
                    buyprice = selectcoin.coin['buyprice'] 
                    total_price = selectcoin.coin['totalbuy']
                    selectcoin.user_money -= (total_price*1.0005)
                    selectcoin.coin['own'] = True
                    selectcoin.coin['wait'] = False
                    selectcoin.coin['lowerbuy'] = False
                    selectcoin.coin['rtotalbuy'] += selectcoin.coin['totalbuy']
                    selectcoin.coin['rtotalamount'] += selectcoin.coin['totalamount']
                    #selectcoin.coin['rfee'] += selectcoin.coin['fee']
                    selectcoin.coin['totalbuy'] = 0
                    #selectcoin.coin['fee'] = 0
                    selectcoin.coin['totalamount'] = 0
                    selectcoin.coin['buyprice'] = 0
                    selectcoin.coin['buyamount'] = 0
                    curr = buycurr[coincount-1]
                    selectcoin.coin['buychecker'] = False
                    self.textEdit.append(f"\n{ticker} 를 평단가 {buyprice:,.2f} 원에 {total_price:,.2f} 원만큼 매수했습니다. 코인 현재가 {curr} 하향구매")
                    buySound.play()
                    
                    
                    
                    averagePrice = round(selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount'], 2)
                    totalbuyAmount = selectcoin.coin['rtotalamount']
                    totalbuyPrice = selectcoin.coin['rtotalbuy']
                    # 이 코인을 구매한 적이 없다면 id값을 부여하고, 행을 새로 추가.
                    # 구매한 적이 있다면 해당 코인에 부여했던 id값이 위치한 행에다 값을 업데이트.
                    # 전량 매도가 된 경우 id값 -1로 초기화, 표에서 제거.
                    
                    if selectcoin.coin['id'] == -1:
                        # 표에 있는 값들을 확인하고 맨 마지막에 해당 id를 부여
                        #id = self.buyTable.rowCount()
                        row = self.buyTable.rowCount()
                        self.buyTable.insertRow(row)
                        buyCoinList.append(selectcoin.coin['ticker'])
                        selectcoin.coin['id'] = buyCoinList.index(selectcoin.coin['ticker'])
                        id = selectcoin.coin['id']
                        self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                        self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                        self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                        self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                        self.myCoin_Update()
                    
                    else:
                        id = selectcoin.coin['id']
                        self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                        self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                        self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                        self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                        self.myCoin_Update()
                    
                    if len(buycurr) == (coincount):
                        break
                    coincount += 1  # 현재가와 같으므로 카운트 업
                    
                    
                elif selectcoin.coin['buyprice'] <= buycurr[coincount-1] and selectcoin.coin['lowerbuy'] == False:
                    ticker = selectcoin.coin['ticker']
                    buyprice = selectcoin.coin['buyprice']
                    total_price = selectcoin.coin['totalbuy']
                    selectcoin.user_money -= (total_price*1.0005)
                    selectcoin.coin['own'] = True
                    selectcoin.coin['wait'] = False
                    selectcoin.coin['rtotalbuy'] += selectcoin.coin['totalbuy']
                    selectcoin.coin['rtotalamount'] += selectcoin.coin['totalamount']
                    #selectcoin.coin['rfee'] += selectcoin.coin['fee']
                    #selectcoin.coin['fee'] = 0
                    selectcoin.coin['totalbuy'] = 0
                    selectcoin.coin['totalamount'] = 0
                    selectcoin.coin['buyprice'] = 0
                    selectcoin.coin['buyamount'] = 0
                    curr = buycurr[coincount-1]
                    selectcoin.coin['buychecker'] = False
                    self.textEdit.append(f"\n{ticker} 를 평단가 {buyprice:,.2f} 원에 {total_price:,.2f} 원만큼 매수했습니다. 코인 현재가 {curr}")
                    buySound.play()
                    
                    
                    averagePrice = round(selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount'], 2)
                    totalbuyAmount = selectcoin.coin['rtotalamount']
                    totalbuyPrice = selectcoin.coin['rtotalbuy']
                    # 이 코인을 구매한 적이 없다면 id값을 부여하고, 행을 새로 추가.
                    # 구매한 적이 있다면 해당 코인에 부여했던 id값이 위치한 행에다 값을 업데이트.
                    # 전량 매도가 된 경우 id값 -1로 초기화, 표에서 제거.
                    
                    if selectcoin.coin['id'] == -1:
                        # 표에 있는 값들을 확인하고 맨 마지막에 해당 id를 부여
                        #id = self.buyTable.rowCount()
                        row = self.buyTable.rowCount()
                        self.buyTable.insertRow(row)
                        buyCoinList.append(selectcoin.coin['ticker'])
                        selectcoin.coin['id'] = buyCoinList.index(selectcoin.coin['ticker'])
                        id = selectcoin.coin['id']
                        self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                        self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                        self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                        self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                        self.myCoin_Update()
                    
                    else:
                        id = selectcoin.coin['id']
                        self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                        self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                        self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                        self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                        self.myCoin_Update()
                    
                    
                    if len(buycurr) == (coincount):
                        break
                    coincount += 1  # 현재가와 같으므로 카운트 업
                    
                    
                else : 
                    coincount += 1    # 현재가와 다르지만 검사 했으므로 카운트 업
                    if len(buycurr) == (coincount):
                        break

        
        ### 지정가 매도 접수 완료
   
        sellcounter = 1
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['wait'] == True and selectcoin.coin['sellchecker'] == True and selectcoin.coin['own'] == True:
                if selectcoin.coin['buyprice'] >= sellcurr[sellcounter-1] and selectcoin.coin['lowerbuy'] == True:
                    averageprice = selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount']
                    ticker = selectcoin.coin['ticker']
                    sellprice = selectcoin.coin['buyprice'] 
                    total_price = selectcoin.coin['totalbuy']
                    amount = selectcoin.coin['buyamount']
                    selectcoin.user_money += (total_price*0.9995)
                    

                    selectcoin.coin['wait'] = False
                    selectcoin.coin['lowerbuy'] = False
                    selectcoin.coin['rtotalbuy'] -= (averageprice*amount)
                    selectcoin.coin['rtotalamount'] -= amount
                    
                    if selectcoin.coin['rtotalbuy'] < 1:
                        selectcoin.coin['own'] = False
                        selectcoin.coin['rtotalamount'] = 0
                        selectcoin.coin['rtotalbuy'] = 0
                        
                    selectcoin.coin['totalbuy'] = 0
                    selectcoin.coin['totalamount'] = 0
                    selectcoin.coin['buyprice'] = 0
                    selectcoin.coin['buyamount'] = 0
                    
                    curr = sellcurr[sellcounter-1]
                    selectcoin.coin['sellchecker'] = False
                    self.textEdit.append(f"\n{ticker} 를 매도가 {sellprice:,.2f} 원에 {total_price:,.2f} 원만큼 매도했습니다. 코인 현재가 {curr} 하향매도")
                    sellSound.play()
                    
                    
                    totalbuyPrice = selectcoin.coin['rtotalbuy']
                        
                    id = selectcoin.coin['id']
                    if totalbuyPrice < 1:
                        selectcoin.coin['id'] = -1
                        self.buyTable.removeRow(id)
                        buyCoinList.remove(selectcoin.coin['ticker'])
                        self.myCoin_Update()
                        #5개의 코인을 샀다고 가정했을때 3번째 코인의 행을 지워버리면 4번째, 5번째 행의 코인들은 3번째, 4번째 행으로 옮겨져야하고 id값도 그에 맞게 바뀌어야 한다.
                        #수익률 때문에 나중에 따로 모듈 만들어서 실시간으로 표에 정보를 표시하게 하고, 여기서는 행과 id값만 지정해주는 방법으로 업데이트 예정.
                        #그냥 코인 구매한 목록들을 리스트로 담아서 관리
                        #코인 행 하나 리무브 시키면 구매한 코인들에 대한 바뀐 id값들을 갱신해야함. for문을 돌려서 buyCoinList와 selectcoin.coin['ticker']와 같은 티커의 아이디 값을 거래를 할때마다 최신화 시킨다.
                    else:
                        totalbuyPrice = selectcoin.coin['rtotalbuy']
                        averagePrice = round(selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount'], 2)    # ZeroDivisionError: division by zero
                        totalbuyAmount = selectcoin.coin['rtotalamount']
                        self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                        self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                        self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                        self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                        self.myCoin_Update()
                    
                    if len(sellcurr) == (sellcounter):
                        break
                    sellcounter += 1  # 현재가와 같으므로 카운트 업
                    
                elif selectcoin.coin['buyprice'] <= sellcurr[sellcounter-1] and selectcoin.coin['lowerbuy'] == False and selectcoin.coin['sellchecker'] == True:
                    averageprice = selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount']
                    ticker = selectcoin.coin['ticker']
                    sellprice = selectcoin.coin['buyprice'] 
                    total_price = selectcoin.coin['totalbuy']
                    amount = selectcoin.coin['buyamount']
                    selectcoin.user_money += (total_price*0.9995)
                    
                    selectcoin.coin['wait'] = False
                    selectcoin.coin['lowerbuy'] = False
                    selectcoin.coin['rtotalbuy'] -= (averageprice*amount)
                    selectcoin.coin['rtotalamount'] -= amount
                    
                    if selectcoin.coin['rtotalbuy'] < 1:
                        selectcoin.coin['own'] = False
                        selectcoin.coin['rtotalamount'] = 0
                        selectcoin.coin['rtotalbuy'] = 0
                    
                    selectcoin.coin['totalbuy'] = 0
                    selectcoin.coin['totalamount'] = 0
                    selectcoin.coin['buyprice'] = 0
                    selectcoin.coin['buyamount'] = 0
                    
                    selectcoin.coin['sellchecker'] = False
                    curr = sellcurr[sellcounter-1]
                    self.textEdit.append(f"\n{ticker} 를 매도가 {sellprice:,.2f} 원에 {total_price:,.2f} 원만큼 매도했습니다. 코인 현재가 {curr}")
                    sellSound.play()
                    
                    totalbuyPrice = selectcoin.coin['rtotalbuy']
                        
                    id = selectcoin.coin['id']
                    if totalbuyPrice < 1:
                        selectcoin.coin['id'] = -1
                        self.buyTable.removeRow(id)
                        buyCoinList.remove(selectcoin.coin['ticker'])
                        self.myCoin_Update()
                        #5개의 코인을 샀다고 가정했을때 3번째 코인의 행을 지워버리면 4번째, 5번째 행의 코인들은 3번째, 4번째 행으로 옮겨져야하고 id값도 그에 맞게 바뀌어야 한다.
                        #수익률 때문에 나중에 따로 모듈 만들어서 실시간으로 표에 정보를 표시하게 하고, 여기서는 행과 id값만 지정해주는 방법으로 업데이트 예정.
                        #그냥 코인 구매한 목록들을 리스트로 담아서 관리
                        #코인 행 하나 리무브 시키면 구매한 코인들에 대한 바뀐 id값들을 갱신해야함. for문을 돌려서 buyCoinList와 selectcoin.coin['ticker']와 같은 티커의 아이디 값을 거래를 할때마다 최신화 시킨다.
                    else:
                        totalbuyPrice = selectcoin.coin['rtotalbuy']
                        averagePrice = round(selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount'], 2)    # ZeroDivisionError: division by zero
                        totalbuyAmount = selectcoin.coin['rtotalamount']
                        self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                        self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                        self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                        self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                        self.myCoin_Update()
                    
                    
                    if len(sellcurr) == (sellcounter):
                        break
                    sellcounter += 1  # 현재가와 같으므로 카운트 업
                else : 
                    sellcounter += 1    # 현재가와 다르지만 검사 했으므로 카운트 업
                    if len(sellcurr) == (sellcounter):
                        break
    
    def click_LimitOrder_Btn(self): # 지정가 매수 주문
        
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['ticker'] == selectcoin.mainticker:
                if selectcoin.coin['wait'] == True:
                    self.textEdit.append("\n해당 코인의 미체결 주문이 있습니다.")
                    break
                else:
                    limitorder = LimitOrder()
                    limitorder.exec_()      # 다른 모듈의 다이얼로그를 실행시킨다.
                    if selectcoin.accepted == True:
                        self.textEdit.append("\n매수 주문이 완료되었습니다.")
                        selectcoin.accepted = False
                    break
    
    def click_LimitSell_Btn(self):  # 지정가 매도
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['ticker'] == selectcoin.mainticker:
                if selectcoin.coin['wait'] == True:
                    self.textEdit.append("\n해당 코인의 미체결 주문이 있습니다.")
                    break
                else:
                    limitsell = LimitSell()
                    limitsell.exec_()
                    if selectcoin.accepted == True:
                        self.textEdit.append("\n매도 주문이 완료되었습니다.")
                        selectcoin.accepted = False
                    break
    
    def click_MarketOrder_Btn(self):    # 시장가 매수
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['ticker'] == selectcoin.mainticker:
                if selectcoin.coin['wait'] == True:
                    self.textEdit.append("\n해당 코인의 미체결 주문이 있습니다.")
                    
                else:
                    marketorder = MarketOrder()
                    marketorder.exec_()
                    if selectcoin.accepted == True:
                        ticker = selectcoin.mainticker
                        for selectcoin.coin in selectcoin.coin_dict:
                            if selectcoin.coin['ticker'] == ticker:
                                buyprice = selectcoin.coin['buyprice']
                                buyamount = selectcoin.coin['buyamount']
                                multifly = buyprice*buyamount
                                break
                            
                        self.textEdit.append(f"\n{ticker} 를 {buyprice:,.2f} 원에 {buyamount:,.8f} 개 매수했습니다. 매수액 {multifly:,.2f} (수수료 0.05%차감)")
                        buySound.play()
                        
                        
                        
                        averagePrice = round(selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount'], 2)
                        totalbuyAmount = selectcoin.coin['rtotalamount']
                        totalbuyPrice = selectcoin.coin['rtotalbuy']
                        # 이 코인을 구매한 적이 없다면 id값을 부여하고, 행을 새로 추가.
                        # 구매한 적이 있다면 해당 코인에 부여했던 id값이 위치한 행에다 값을 업데이트.
                        # 전량 매도가 된 경우 id값 -1로 초기화, 표에서 제거.
                        
                        if selectcoin.coin['id'] == -1:
                            # 표에 있는 값들을 확인하고 맨 마지막에 해당 id를 부여
                            #id = self.buyTable.rowCount()
                            row = self.buyTable.rowCount()
                            self.buyTable.insertRow(row)
                            buyCoinList.append(selectcoin.coin['ticker'])
                            selectcoin.coin['id'] = buyCoinList.index(selectcoin.coin['ticker'])
                            id = selectcoin.coin['id']
                            self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                            self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                            self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                            self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                            self.myCoin_Update()
                        
                        else:
                            id = selectcoin.coin['id']
                            self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                            self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                            self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                            self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                            self.myCoin_Update()
                        
                        selectcoin.coin['buyprice'] = 0
                        selectcoin.coin['buyamount'] = 0
                        selectcoin.accepted = False
        
    
    def click_MarketSell_Btn(self):     # 시장가 매도
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['ticker'] == selectcoin.mainticker:
                if selectcoin.coin['wait'] == True:
                    self.textEdit.append("\n해당 코인의 미체결 주문이 있습니다.")
                else:
                    marketsell = MarketSell()
                    marketsell.exec_()
                    if selectcoin.accepted == True:
                        ticker = selectcoin.mainticker
                        for selectcoin.coin in selectcoin.coin_dict:
                            if selectcoin.coin['ticker'] == ticker:
                                buyamount = selectcoin.coin['buyamount']
                                buyprice = selectcoin.coin['buyprice']
                                multifly = buyprice*buyamount
                                break
                        self.textEdit.append(f"\n{ticker} 를 {buyprice:,.2f} 원에 {buyamount:,.8f} 개 매도했습니다. 매도액 {multifly:,.2f} (수수료 0.05%차감)")
                        sellSound.play()
                        
                        totalbuyPrice = selectcoin.coin['rtotalbuy']
                        
                        id = selectcoin.coin['id']
                        if totalbuyPrice < 1:
                            selectcoin.coin['id'] = -1
                            self.buyTable.removeRow(id)
                            buyCoinList.remove(selectcoin.coin['ticker'])
                            self.myCoin_Update()
                            #5개의 코인을 샀다고 가정했을때 3번째 코인의 행을 지워버리면 4번째, 5번째 행의 코인들은 3번째, 4번째 행으로 옮겨져야하고 id값도 그에 맞게 바뀌어야 한다.
                            #수익률 때문에 나중에 따로 모듈 만들어서 실시간으로 표에 정보를 표시하게 하고, 여기서는 행과 id값만 지정해주는 방법으로 업데이트 예정.
                            #그냥 코인 구매한 목록들을 리스트로 담아서 관리
                            #코인 행 하나 리무브 시키면 구매한 코인들에 대한 바뀐 id값들을 갱신해야함. for문을 돌려서 buyCoinList와 selectcoin.coin['ticker']와 같은 티커의 아이디 값을 거래를 할때마다 최신화 시킨다.
                        else:
                            totalbuyPrice = selectcoin.coin['rtotalbuy']
                            averagePrice = round(selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount'], 2)    # ZeroDivisionError: division by zero
                            totalbuyAmount = selectcoin.coin['rtotalamount']
                            self.buyTable.setItem(id, 0, QTableWidgetItem(ticker))
                            self.buyTable.setItem(id, 1, QTableWidgetItem(f'{averagePrice:,}'))
                            self.buyTable.setItem(id, 2, QTableWidgetItem(str(totalbuyAmount)))
                            self.buyTable.setItem(id, 3, QTableWidgetItem(f'{totalbuyPrice:,}'))
                            self.myCoin_Update()
                        
                        selectcoin.coin['buyamount'] = 0
                        selectcoin.coin['buyprice'] = 0
                        selectcoin.accepted = False
            
    def  click_myCoin_Btn(self):        ### 거래내역조회
        mycoincount = 0
        self.textEdit.append("\n거래내역 조회")
        self.textEdit.append(f'현재 잔고 : {selectcoin.user_money:,.2f} 원')
        for selectcoin.coin in selectcoin.coin_dict:      # 코인의 각 항목에 접근해서 구매한 코인의 own을 True, buyprice라는 새 항목을 만들어 매수가격 추가
            if selectcoin.coin['own'] == True:
                mycoincount += 1
                ticker = selectcoin.coin['ticker']
                buyprice = selectcoin.coin['rtotalbuy'] / selectcoin.coin['rtotalamount']
                buyamount = selectcoin.coin['rtotalamount']
                #fee = selectcoin.coin['rfee']
                totalbuyprice = selectcoin.coin['rtotalbuy']
                self.textEdit.append(f"{mycoincount}.  코인이름 : {ticker}  평단 : {buyprice:,.2f}  수량 : {buyamount:,.8f}  총 매수액 : {totalbuyprice:,.2f}")
                
        if mycoincount == 0:
            self.textEdit.append("\n보유한 코인이 없습니다.")

    def click_nonContract_Btn(self):        ### 미체결 조회
        coint = 0
        self.textEdit.append("\n미체결 조회")
        for selectcoin.coin in selectcoin.coin_dict:
            if selectcoin.coin['wait'] == True:
                
                coint += 1
                ticker = selectcoin.coin['ticker']
                buyprice = selectcoin.coin['buyprice']
                buyamount = selectcoin.coin['buyamount']
                #fee = selectcoin.coin['fee']
                if selectcoin.coin['buychecker'] == True:
                    self.textEdit.append(f"{coint}. {ticker} 매수 대기  거래수량 : {buyamount:,.8f}  거래단가 : {buyprice:,.2f}  거래금액 : {buyamount*buyprice:,.2f}")
                else:
                    self.textEdit.append(f"{coint}. {ticker} 매도 대기  거래수량 : {buyamount:,.8f}  거래단가 : {buyprice:,.2f}  거래금액 : {buyamount*buyprice:,.2f}")
        self.textEdit.append("미체결 코인의 번호를 입력하면 거래 취소가 가능합니다.")        
        #self.nonContractcount = cointcounter
        if coint == 0:
            self.textEdit.append("미체결 거래가 없습니다.")
        
            
    def search_coin(self):      ### 코인 선택
        self.textEdit.append(self.lineEdit.text())
        if "KRW-" in self.lineEdit.text():
            for ticker in tickers:
                if self.lineEdit.text() == ticker:
                    self.textEdit.append(f'{ticker} 정보를 불러왔습니다.')             
                    selectcoin.mainticker = ticker
                    break
                
        if "cancel-" in self.lineEdit.text():   #미체결 매수 취소
            for selectcoin.coin in selectcoin.coin_dict:
                if selectcoin.coin['ticker'] in self.lineEdit.text():
                    selectcoin.coin['wait'] = False
                    selectcoin.coin['buyprice'] = 0
                    selectcoin.coin['buyamount'] = 0
                    selectcoin.coin['totalbuy'] = 0
                    selectcoin.coin['totalamount'] = 0
                    selectcoin.coin['lowerbuy'] = False
                    #selectcoin.coin['fee'] = 0
                    
                    ticker = selectcoin.coin['ticker']
                    self.textEdit.append(f'{ticker}의 주문이 취소되었습니다.')
                    
                
        self.lineEdit.clear()
        
    def clickBtn_help(self):    ## 도움말
        self.textEdit.append("\n\n가즈아 온라인 모의투자는 업비트 가상화폐 거래소의 실시간 데이터를 바탕으로 하는 모의 투자 게임입니다.\n거래는 현재 업비트 원화시장에 등록된 코인에 한에서만 가능합니다.")
        self.textEdit.append("대부분의 기능은 업비트를 모방에서 만들었으나 기술적인 이유로 구현되지 못하거나 다른 부분이 있을 수 있습니다. 버그나 불만 사항에 대해서는 010-8248-5327로 문의 바랍니다.")
        self.textEdit.append("개발자 후원하기 : 112-2148-6918-01 부산은행")
        self.textEdit.append("\n코인 거래시 주의사항")
        self.textEdit.append("모든 코인의 최소 주문금액은 5000원입니다. 코인마다 매수가격의 단위가 다르게 설정되어 있습니다. 자세한 것은 매수창에서 확인 가능합니다. 추후 업비트의 기준에 따라 변경될 예정입니다.")
        self.textEdit.append("미체결 상태로 매수/매도 대기중인 코인에 대해서는 주문을 취소하거나 거래가 이루어지기 전까지는 추가 주문이 불가능합니다.")
        self.textEdit.append("현재 조회되는 코인에 대해서만 매수/매도 주문이 가능합니다. 먼저 거래할 코인의 정보를 조회하고, 매수/매도 주문을 진행하면 되겠습니다.")
        self.textEdit.append("모든 매수와 매도는 업비트의 정책에 따라 0.05%의 수수료가 부과됩니다. 매수 금액의 0.05%가 잔고에서 더 빠져나가고, 매도 금액의 0.05%가 제외된 값이 잔고에 들어옵니다.")
        self.textEdit.append("따라서 5000원 이상으로 주문을 했더라도 수수료를 포함한 금액을 지불할 수 없다면 거래가 제한됩니다.")
        self.textEdit.append("\n명령어 리스트")
        self.textEdit.append("기술 구현 능력 미숙으로 몇몇 기능들은 명령어로 작동합니다.")
        self.textEdit.append("코인 정보 조회 방법 : KRW-코인 티커명  ex) 비트코인 조회 : KRW-BTC. 리플코인 조회 : KRW-XRP"  )
        self.textEdit.append("미체결 주문 취소 방법 : cancel-KRW-코인 티커명  ex) 샌드박스 코인 미체결 매도주문 취소하기 : cancel-KRW-SAND")

    def myCoin_Update(self):
        for i in range(len(buyCoinList)):
            for selectcoin.coin in selectcoin.coin_dict:
                if selectcoin.coin['ticker'] == buyCoinList[i]:
                    selectcoin.coin['id'] = i
                
    def closeEvent(self, event):
        quit_msg = "그만할래요?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            #pygame.mixer.music.stop()
            self.lw.close()
            event.accept()
          
            
            
        else:
            event.ignore()
            os.system("pause")


 
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
    