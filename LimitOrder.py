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
        self.setGeometry(800, 400, 300, 330)
        self.setWindowTitle('지정가 매도')
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
        
        self.order_totalbuy_line = QLineEdit(self)
        self.order_totalbuy_line.setAlignment(Qt.AlignRight)
        self.order_totalbuy_line.move(140, 165)
        self.order_totalbuy_line.resize(150, 25)
        self.order_totalbuy_line.textChanged.connect(self.order_totalbuy_line_changed)
        
        self.button = QPushButton(self)
        self.button.move(10, 210)
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

        
    def button_clicked(self):
        buyprice = buyprice = float(self.buyprice_line.text())
        amount = float(self.order_amount_label2.text())
        totalorder = round(buyprice*amount ,2)
        
        msg = QMessageBox()
        msg.setGeometry(850, 500, 300, 300)
        msg.setWindowTitle('WARNING')
        msg.setText(f'매수가격 : {buyprice:,}  주문수량 : {amount:,}\n주문총액 : {totalorder:,.2f} 원에 매수합니다.')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        result = msg.exec()
        if result == QMessageBox.Ok:
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

            # buyprice : 매수가격    amount: 매수수량
        self.accept()    
            
            # 매수코인 이름, 매수가격, 주문 수량에 대한 정보를 selectcoin 전역변수로 보낸다.