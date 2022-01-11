import pyupbit
ticker = "KRW-BTC"
wop = pyupbit.get_current_price(ticker)
print(wop)