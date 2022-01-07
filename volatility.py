import pyupbit


def get_target_price(ticker, k):   ## 변동성 돌파전략의 매수지점 target을 반환하는 매서드
    df = pyupbit.get_ohlcv(ticker, interval = "day", count = 2)  # 모든 날짜의 캔들값(시가, 고가, 저가, 종가, 거래량, 거래대금)을 바인딩
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    ## 거래 시작 시간 조회
    df = pyupbit.get_ohlcv(ticker, interval = "day", count = 1) # get_ohlcv를 일봉으로 조회하면 09:00시로 얻어옴
    start_time = df.index[0]
    return start_time

def get_ma5(ticker):
    # 5일 이동 평균선 조회
    df = pyupbit.get_ohlcv(ticker, interval="day", count=6)
    ma5 = df['close'].rolling(5).mean().iloc[-2]
    return ma5