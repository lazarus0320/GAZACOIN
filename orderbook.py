import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QProgressBar
from PyQt5.QtCore import QThread, Qt, pyqtSignal
import pyupbit, time
import math
import selectcoin

class OrderbookWorker(QThread):    ## 쓰레드 사용을 위한 클래스 선언
    data_seed = pyqtSignal(dict) # 딕셔너리 형태로 데이터를 전달할 시그널 정의
    
    def __init__(self, ticker):     # ticker는 코인의 약어
        super(OrderbookWorker, self).__init__()
        self.ticker = ticker
        self.alive = True   # self.alive가 True인 동안에 스레드를 계속 돌림

    def run(self):
        while self.alive:
            self.ticker = selectcoin.mainticker
            data = pyupbit.get_orderbook(self.ticker) # 업비트 호가창을 매수/매도 각각 15개씩만 얻어옴 (딕셔너리형태)
            time.sleep(0.5)    # 초당 20번 수행
            self.data_seed.emit(data)    # 딕셔너리 형태 호가 정보를 슬롯으로 전달
    
    def close(self):
        self.alive = False  # self.alive가 False전환되면 스레드 종료
        self.quit()
        self.wait(3000)

class OrderbookWidget(QWidget): ## 위젯 받아와서 UI를 띄우는 클래스
    def __init__(self, parent=None):  # 새창으로 BTC에 대한 호가창 위젯을 띄움
        super().__init__(parent)
        uic.loadUi("resource/orderbook.ui", self)
        self.ow = OrderbookWorker(selectcoin.mainticker) # 스레드의 객체 ow 선언
        self.ow.data_seed.connect(self.updateData)   # 시그널에게 data를 받으면 updateData메서드에 data인자를 넘겨주도록 설계
        self.ow.start() # updateData에 data값을 넘겨주고 실행시킴
        
        ##  매수호가   Qtdesigner에서 매수호가 테이블의 객체 이름은 tableBids, 매도호가  Qtdesigner에서 매도호가 테이블의 객체 이름은 tableAsks
        
        for i in range(self.tableBids.rowCount()):  # 테이블의 모든 행을 돈다 row = 가로 column = 세로
            ### 매도호가  Qtdesigner에서 매도호가 객체 이름은 tableAsks
            ## 1열 가격
            item_0 = QTableWidgetItem(str(""))  # 테이블 1열에 문자열 객체 생성
            item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)    # 셀을 오른쪽으로 정렬함. 셀 정렬 :객체.setTextAlignment(Qt.Align방향) | Qt.AlignVCenter) 
            self.tableAsks.setItem(i, 0, item_0) # 테이블 객체.setItem(행번호,열번호,위젯 객체) : 셀에 값을 입력하는 법. 화면에 그려냄
            ## 2열 규모(코인의 총 수량)
            item_1 = QTableWidgetItem(str(""))
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tableAsks.setItem(i, 1, item_1)
            ## 3열 총액(코인 총 수량x코인 시세)
            item_2 = QProgressBar(self.tableAsks)
            item_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_2.setStyleSheet("""
                QProgressBar {background-color : rgba(0,0,0,0%);border : 1}
                QProgressBar::Chunk {background-color : rgba(0,0,255,50%);border : 1 }
                """)    # CSS로 셀 배경색을 흰색, ProgressBar 게이지를 파란색으로 지정
            self.tableAsks.setCellWidget(i, 2, item_2)  # 셀의 설정 값대로 화면에 그려냄 테이블 객체.setCellWidget(행, 열, 위젯 객체)
            
            ## 매수호가   Qtdesigner에서 매수호가 객체 이름은 tableBids
            ## 1열 가격
            item_0 = QTableWidgetItem(str(""))
            item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tableBids.setItem(i, 0, item_0)
            ## 2열 규모
            item_1 = QTableWidgetItem(str(""))
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tableBids.setItem(i, 1, item_1)
            ## 3열 총액
            item_2 = QProgressBar(self.tableBids)
            item_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_2.setStyleSheet("""
                QProgressBar {background-color : rgba(0,0,0,0%);border : 1}
                QProgressBar::Chunk {background-color : rgba(255,0,0,50%);border : 1 }
                """)    # CSS로 셀 배경색을 흰색, ProgressBar 게이지를 빨간색으로 지정
            self.tableBids.setCellWidget(i, 2, item_2)   # 셀의 설정 값대로 화면에 그려냄 테이블 객체.setCellWidget(행, 열, 위젯 객체)
            
    def updateData(self, data):     ## 데이터를 받아서 화면에 업데이트
        sum_Bid_Price_List = []     # 각 매수 호가의 총합을 담을 리스트
        sum_Ask_Price = []          # 각 매도 호가의 총합을 담을 리스트
        bid_Price_List = []         # 각 매수 호가의 가격을 담을 리스트
        bid_Size_List = []          # 각 매수 호가의 코인 수량을 담을 리스트
        ask_Price_List = []         # 각 매도 호가의 가격을 담을 리스트
        ask_Size_List = []          # 각 매도 호가의 코인 수량을 담을 리스트
        
        for i in range(0,15):   # api로 얻어온 호가창 개수는 매수, 매도 각각 15개
            multiply_Bid = data['orderbook_units'][i]['bid_price'] * data['orderbook_units'][i]['bid_size'] # 각 호가창의 가격*수량을 담음(총액)
            sum_Bid_Price_List.append(math.ceil(multiply_Bid))     # 각 호가창의 총액을 소수점 첫째 자리에서 반올림 하고 sum_Bid_Price_List에 바인딩
            bid_Price_List.append(data['orderbook_units'][i]['bid_price']) # 각 호가창의 매수 호가 가격들을 바인딩
            bid_Size_List.append(data['orderbook_units'][i]['bid_size'])    # 각 호가창의 매수 호가 코인 수량을 바인딩
        
            multiply_Ask = data['orderbook_units'][i]['ask_price'] * data['orderbook_units'][i]['ask_size']
            sum_Ask_Price.append(math.ceil(multiply_Ask))
            ask_Price_List.append(data['orderbook_units'][i]['ask_price'])
            ask_Size_List.append(data['orderbook_units'][i]['ask_size'])
            
        sum_Ask_Price = sum_Ask_Price[::-1]     # 위쪽 호가창에 배치될 매도 호가창은 가격을 내림차순으로 배열하므로 리스트를 역순으로 재배치함
        ask_Size_List = ask_Size_List[::-1]     # ,,
        ask_Price_List = ask_Price_List[::-1]   # ,,
        max_Trade_Price = max(sum_Bid_Price_List + sum_Ask_Price)  # 전체 매도+매수금 총액의 최댓값 바인딩


        for i, v in enumerate(ask_Price_List):   #  enumerate -> 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환 따라서 i는 인덱스번호, v는 그 값이 된다.
            item_0 = self.tableAsks.item(i, 0)  # 매도 호가 테이블 객체 tableAsks의 i행 0열을 item_0에 바인딩
            item_0.setText(str(v))   # 호가 출력. 000,000,000형태로 포멧팅.
                
            item_2 = self.tableAsks.cellWidget(i, 2)    # 3번째 열의 모든 셀들에 대해 item_2가 바인딩
            ## item_2가 바인딩하는 tableBids객체의 QProgressBar위젯은 setRange, setFormat, setValue함수를 따로 지정해 주어야 함
            item_2.setRange(0, max_Trade_Price/1000000) #   3번째 열의 모든 셀들의 범위를 0~전체 매도+매수금 총액의 최댓값으로 지정. 따라서 100%는 전체 매도+매수금의 총액
            item_2.setFormat(f"{sum_Ask_Price[i]:,}")   # 매도 총액을 000,000,000형태로 포멧팅.
            # 각 호가번호의 매도 금액 총액을 어떻게 표시할건지를 정함. 여기서는 숫자에 ,을 삽입
            item_2.setValue(sum_Ask_Price[i]/1000000)    # setValue() : 진행표시줄의 진행 상태를 특정 값으로 설정. 매도 총액을 출력.
            
        for i, v in enumerate(ask_Size_List):   # 매도 호가창 2번째 열에 매도 코인의 수량을 출력함
            item_1 = self.tableAsks.item(i, 1)
            item_1.setText(str(v))
            
        for i, v in enumerate(bid_Price_List):   #  처음부터 끝까지 1칸 간격으로. enumerate -> 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환 따라서 i는 인덱스번호, v는 그 값이 된다.
            item_0 = self.tableBids.item(i, 0)  # 매도호가 테이블 tableAsks의 i행 0열을 item_0에 바인딩
            item_0.setText(str(v))   # 매수 호가 출력
                # 수량 출력
            item_2 = self.tableBids.cellWidget(i, 2)    # 3번째 열의 모든 셀들에 대해 item_2가 바인딩
            ## item_2가 바인딩하는 tableBids객체의 QProgressBar위젯은 setRange, setFormat, setValue함수를 따로 지정해 주어야 함
            item_2.setRange(0, max_Trade_Price/1000000) #   3번째 열의 모든 셀들의 범위를 0~전체 매도+매수금 총액의 최댓값으로 지정. 따라서 100%는 전체 매도+매수금의 총액
            item_2.setFormat(f"{sum_Bid_Price_List[i]:,}")  # 매수 총액을 000,000,000 형태로 포멧팅
            item_2.setValue(sum_Bid_Price_List[i]/1000000)   # setValue() : 진행표시줄의 진행 상태를 특정 값으로 설정. 매수 총액을 출력
            
        for i, v in enumerate(bid_Size_List):   # 매도 호가창 2번째 열에 매수 코인의 수량을 출력함
            item_1 = self.tableBids.item(i, 1)
            item_1.setText(str(v))
    
    def closeEvent(self, event):    # 스레드 종료를 위해 QWidget의 메서드를 오버라이딩, 메인 위젯 종료시 closeEvent 메서드 실행
        self.ow.close()

        
        
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ow = OrderbookWidget()
    ow.show()
    exit(app.exec_())