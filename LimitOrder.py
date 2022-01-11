import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import pyupbit
import selectcoin

import time


class LimitOrder(QDialog):     ## 지정가 매수 다이얼로그

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.show()

    def setupUI(self):
        self.setGeometry(800, 400, 300, 270)
        self.setWindowTitle('지정가 매수')
        self.setWindowIcon(QIcon("resource/doge.png"))
        self.ticker = selectcoin.mainticker
        self.cp = pyupbit.get_current_price(self.ticker)
        
        
        
        self.totalprice = 0
        self.buy_amount = 0
        
   
        self.amount_label = QLabel(f"주문가능(잔고) : {selectcoin.user_money:,.2f} KRW", self)
        self.amount_label.move(10, 30)
        
        
        self.buyprice_label = QLabel("매수가격(KRW) :", self)
        
        self.buyprice_label.move(10, 60)
        
        self.buyprice_line = QLineEdit(self)
        self.buyprice_line.setAlignment(Qt.AlignRight)
        self.buyprice_line.setText(str(self.cp))
        self.buyprice_line.move(140, 55)
        self.buyprice_line.resize(150, 25)
        self.buyprice_line.textChanged.connect(self.buyprice_line_changed)
        
        self.order_amount_label = QLabel(f"주문수량({self.ticker}) :", self)
        self.order_amount_label.move(10, 90)
        
        self.order_amount_label2 = QLabel(self)
        self.order_amount_label2.move(150, 85)
        self.order_amount_label2.resize(100,25)
       
        self.button10 = QPushButton(self)
        self.button10.move(15, 120)
        self.button10.resize(60, 30)
        self.button10.setText('10%')
        self.button10.clicked.connect(self.button10_clicked)
        
        self.button25 = QPushButton(self)
        self.button25.move(85, 120)
        self.button25.resize(60, 30)
        self.button25.setText('25%')
        self.button25.clicked.connect(self.button25_clicked)
        
        self.button50 = QPushButton(self)
        self.button50.move(155, 120)
        self.button50.resize(60, 30)
        self.button50.setText('50%')
        self.button50.clicked.connect(self.button50_clicked)
        
        self.button_all = QPushButton(self)
        self.button_all.move(225, 120)
        self.button_all.resize(60, 30)
        self.button_all.setText('최대')
        self.button_all.clicked.connect(self.button_all_clicked)
        
        self.order_totalbuy_label = QLabel(f"주문총액(KRW) :", self)
        self.order_totalbuy_label.move(10, 170)
        
        if selectcoin.mainticker == "KRW-XLM" or selectcoin.mainticker == "KRW-ETH" or selectcoin.mainticker == "KRW-BTC" or selectcoin.mainticker == "KRW-ADA" or selectcoin.mainticker == "KRW-EOS" or selectcoin.mainticker == "KRW-SNT" or selectcoin.mainticker == "KRW-BCH" or selectcoin.mainticker == "KRW-XEM": 
            self.fee_label = QLabel(f"최소 주문금액 : 5000KRW   수수료 : 0.05%", self)
        else: 
            self.fee_label = QLabel(f"최소 주문금액 : 1000KRW   수수료 : 0.05%", self)
        self.fee_label.move(10, 205)
        
        self.order_totalbuy_line = QLineEdit(self)
        self.order_totalbuy_line.setAlignment(Qt.AlignRight)
        self.order_totalbuy_line.move(140, 165)
        self.order_totalbuy_line.resize(150, 25)
        self.order_totalbuy_line.textChanged.connect(self.order_totalbuy_line_changed)
        
        self.button = QPushButton(self)
        self.button.move(10, 230)
        self.button.resize(280, 30)
        self.button.setText('매수')
        self.button.clicked.connect(self.button_clicked)
        
        
        
    def button10_clicked(self):
        self.buy_amount_source = float(selectcoin.user_money) / float(self.buyprice_line.text())
        self.buy_amount = round(self.buy_amount_source * 0.1 , 8)
        self.order_amount_label2.setText(str(float(self.buy_amount)))
        
        buyprice = float(self.buyprice_line.text())
        multifly = round(self.buy_amount * buyprice, 2)
        self.order_totalbuy_line.setText(str(int(float(multifly))))
        
    def button25_clicked(self):
        self.buy_amount_source = float(selectcoin.user_money) / float(self.buyprice_line.text())
        self.buy_amount = round(self.buy_amount_source * 0.25 , 8)
        self.order_amount_label2.setText(str(float(self.buy_amount)))
        
        buyprice = float(self.buyprice_line.text())
        multifly = round(self.buy_amount * buyprice, 2)
        self.order_totalbuy_line.setText(str(int(float(multifly))))
        
    def button50_clicked(self):
        self.buy_amount_source = float(selectcoin.user_money) / float(self.buyprice_line.text())
        self.buy_amount = round(self.buy_amount_source * 0.5 , 8)
        self.order_amount_label2.setText(str(float(self.buy_amount)))
        
        buyprice = float(self.buyprice_line.text())
        multifly = round(self.buy_amount * buyprice, 2)
        self.order_totalbuy_line.setText(str(int(float(multifly))))
    
    def button_all_clicked(self):
        self.buy_amount_source = float(selectcoin.user_money) / float(self.buyprice_line.text())
        self.buy_amount = round(self.buy_amount_source, 8)
        self.order_amount_label2.setText(str(float(self.buy_amount)))
        
        buyprice = float(self.buyprice_line.text())
        multifly = round(self.buy_amount * buyprice, 2)
        self.order_totalbuy_line.setText(str(int(float(multifly))))
        
    def buyprice_line_changed(self):
        try:
            buyprice = float(self.buyprice_line.text())
            amount = float(self.order_amount_label2.text())
            totalorder = round(buyprice*amount ,2)
            self.order_totalbuy_line.setText(str(float(totalorder)))
        except:
            self.buyprice_line.setText(f'{self.cp}')

        
    def order_totalbuy_line_changed(self):  
        try:
            val = int(float(self.order_totalbuy_line.text()))
            val2 = float(self.buyprice_line.text())
            rval = round(val / val2, 8)
            self.order_amount_label2.setText(str(float(rval)))
        except:
            self.buyprice_line.setText('0')

        
    def button_clicked(self, event):
        jumper = False
        buyprice = round(float(self.buyprice_line.text()), 2)
        amount = round(float(self.order_amount_label2.text()),8)
        totalorder = round(buyprice*amount)
        
        tick = self.tick_checker()
        
        
        msg = QMessageBox()
        msg.setGeometry(850, 500, 300, 300)
        msg.setWindowTitle('WARNING')
        if buyprice % tick != 0:
            buyprice = round(round((buyprice / tick)) * tick, 2)
            msg.setText(f'해당 코인의 경우 최소 단위를 {tick}원으로 주문할 수 있으므로 자동으로 단위에 맞게 매수가격을 설정했습니다.\n매수가격 : {buyprice:,}  주문수량 : {amount:,}\n주문총액 : {totalorder:,.2f} 원에 매수합니까?')
        else :
            msg.setText(f'매수가격 : {buyprice:,}  주문수량 : {amount:,}\n주문총액 : {totalorder:,.2f} 원에 매수합니까?.')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        result = msg.exec()
        if result == QMessageBox.Ok:
            if selectcoin.mainticker == "KRW-XLM" or selectcoin.mainticker == "KRW-ETH" or selectcoin.mainticker == "KRW-BTC" or selectcoin.mainticker == "KRW-ADA" or selectcoin.mainticker == "KRW-EOS" or selectcoin.mainticker == "KRW-SNT" or selectcoin.mainticker == "KRW-BCH" or selectcoin.mainticker == "KRW-XEM": 
                if int(float(self.order_totalbuy_line.text())) < 5000:
                    msg2 = QMessageBox()     
                    msg2.setWindowTitle('WARNING')
                    msg2.setText("해당 코인의 경우 최소 5000원 이상 주문만 가능합니다.")
                    result2 = msg2.exec()
                    if result2 == QMessageBox.Ok:
                        self.close
                        jumper = True
      
            else : 
                if int(float(self.order_totalbuy_line.text())) < 1000:
                    msg2 = QMessageBox()     
                    msg2.setWindowTitle('WARNING')
                    msg2.setText("해당 코인의 경우 최소 5000원 이상 주문만 가능합니다.")
                    result2 = msg2.exec()
                    if result2 == QMessageBox.Ok:
                        self.close
                        jumper = True

            
            if jumper != True:    
                for selectcoin.coin in selectcoin.coin_dict: 
                    # 코인의 각 항목에 접근해서 구매한 코인의 own을 True, buyprice라는 새 항목을 만들어 매수가격 추가
                    if selectcoin.mainticker == selectcoin.coin['ticker']:
                        if buyprice <= self.cp:
                            selectcoin.coin['lowerbuy'] = True
                        selectcoin.coin['wait'] = True
                        #selectcoin.coin['fee'] = buyprice*amount*0.05
                        selectcoin.coin['buyprice'] = buyprice       # 매수금액(평단)
                        selectcoin.coin['totalbuy'] = buyprice*amount     # 매수 취소시 증가한만큼 빼야함
                        selectcoin.coin['buyamount'] = amount
                        selectcoin.coin['totalamount'] = amount     # 매수 취소시 증가한만큼 빼야함
                        selectcoin.coin['buychecker'] = True
            jumper = False
            # buyprice : 매수가격    amount: 매수수량
        self.accept()    
            
            # 매수코인 이름, 매수가격, 주문 수량에 대한 정보를 selectcoin 전역변수로 보낸다.
            
    def tick_checker(self):
        if self.cp < 10:
            return 0.01
        elif 10<= self.cp < 100:
            return 0.1
        elif 100<= self.cp < 1000:
            return 1
        elif 1000<= self.cp < 10000:
            return 5
        elif 10000<= self.cp < 100000:
            return 10
        elif 100000<= self.cp < 500000:
            return 50
        elif 500000<= self.cp < 1000000:
            return 100
        elif 1000000<= self.cp < 2000000:
            return 500
        elif 2000000<= self.cp:
            return 1000
        
    def closeEvent(self, event):
        quit_msg = "해당 코인의 경우 최소 5000원 이상 주문만 가능합니다."
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes)
                                                    
        if reply == QMessageBox.Yes:
                    
            self.close()
            event.accept()