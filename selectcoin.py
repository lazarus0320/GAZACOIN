global mainticker
mainticker = "KRW-BTC"
global user_money
user_money = 10000000
global buychecker
buychecker = False

global coin_dict
coin_dict =[{'id':0, 'ticker':'KRW-BTC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':1, 'ticker':'KRW-ETH', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':2, 'ticker':'KRW-NEO', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':3, 'ticker':'KRW-MTL', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':4, 'ticker':'KRW-LTC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':5, 'ticker':'KRW-XRP', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':6, 'ticker':'KRW-ETC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':7, 'ticker':'KRW-OMG', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':8, 'ticker':'KRW-SNT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':9, 'ticker':'KRW-WAVES', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':10, 'ticker':'KRW-XEM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':11, 'ticker':'KRW-QTUM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':12, 'ticker':'KRW-LSK', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':13, 'ticker':'KRW-STEEM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':14, 'ticker':'KRW-XLM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':15, 'ticker':'KRW-ARDR', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':16, 'ticker':'KRW-ARK', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':17, 'ticker':'KRW-STORJ', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':18, 'ticker':'KRW-GRS', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':19, 'ticker':'KRW-REP', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':20, 'ticker':'KRW-ADA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':21, 'ticker':'KRW-SBD', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':22, 'ticker':'KRW-POWR', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':23, 'ticker':'KRW-BTG', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':24, 'ticker':'KRW-ICX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':25, 'ticker':'KRW-EOS', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':26, 'ticker':'KRW-TRX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':27, 'ticker':'KRW-SC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':28, 'ticker':'KRW-ONT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':29, 'ticker':'KRW-ZIL', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':30, 'ticker':'KRW-POLY', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':31, 'ticker':'KRW-ZRX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':32, 'ticker':'KRW-LOOM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':33, 'ticker':'KRW-BCH', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':34, 'ticker':'KRW-BAT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':35, 'ticker':'KRW-IOST', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':36, 'ticker':'KRW-RFR', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':37, 'ticker':'KRW-CVC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':38, 'ticker':'KRW-IQ', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':39, 'ticker':'KRW-IOTA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':40, 'ticker':'KRW-MFT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':41, 'ticker':'KRW-ONG', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':42, 'ticker':'KRW-GAS', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':43, 'ticker':'KRW-UPP', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':44, 'ticker':'KRW-ELF', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':45, 'ticker':'KRW-KNC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':46, 'ticker':'KRW-BSV', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':47, 'ticker':'KRW-THETA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':48, 'ticker':'KRW-QKC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':49, 'ticker':'KRW-BTT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':50, 'ticker':'KRW-MOC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':51, 'ticker':'KRW-ENJ', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':52, 'ticker':'KRW-TFUEL', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':53, 'ticker':'KRW-MANA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':54, 'ticker':'KRW-ANKR', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':55, 'ticker':'KRW-AERGO', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':56, 'ticker':'KRW-ATOM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':57, 'ticker':'KRW-TT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':58, 'ticker':'KRW-CRE', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':59, 'ticker':'KRW-MBL', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':60, 'ticker':'KRW-WAXP', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':61, 'ticker':'KRW-HBAR', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':62, 'ticker':'KRW-MED', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':63, 'ticker':'KRW-MLK', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':64, 'ticker':'KRW-STPT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':65, 'ticker':'KRW-ORBS', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':66, 'ticker':'KRW-VET', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':67, 'ticker':'KRW-CHZ', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':68, 'ticker':'KRW-STMX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':69, 'ticker':'KRW-DKA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':70, 'ticker':'KRW-HIVE', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':71, 'ticker':'KRW-KAVA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':72, 'ticker':'KRW-AHT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':73, 'ticker':'KRW-LINK', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':74, 'ticker':'KRW-XTZ', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':75, 'ticker':'KRW-BORA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':76, 'ticker':'KRW-JST', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':77, 'ticker':'KRW-CRO', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':78, 'ticker':'KRW-TON', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':79, 'ticker':'KRW-SXP', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':80, 'ticker':'KRW-HUNT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':81, 'ticker':'KRW-PLA', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':82, 'ticker':'KRW-DOT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':83, 'ticker':'KRW-SRM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':84, 'ticker':'KRW-MVL', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':85, 'ticker':'KRW-STRAX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':86, 'ticker':'KRW-AQT', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':87, 'ticker':'KRW-GLM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':88, 'ticker':'KRW-SSX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':89, 'ticker':'KRW-META', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':90, 'ticker':'KRW-FCT2', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':91, 'ticker':'KRW-CBK', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':92, 'ticker':'KRW-SAND', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':93, 'ticker':'KRW-HUM', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':94, 'ticker':'KRW-DOGE', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':95, 'ticker':'KRW-STRK', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':96, 'ticker':'KRW-PUNDIX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':97, 'ticker':'KRW-FLOW', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':98, 'ticker':'KRW-DAWN', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':99, 'ticker':'KRW-AXS', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':100, 'ticker':'KRW-STX', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':101, 'ticker':'KRW-XEC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':102, 'ticker':'KRW-SOL', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':103, 'ticker':'KRW-MATIC', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':104, 'ticker':'KRW-NU', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':105, 'ticker':'KRW-AAVE', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':106, 'ticker':'KRW-1INCH', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':107, 'ticker':'KRW-ALGO', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0},
            {'id':108, 'ticker':'KRW-NEAR', 'own': False, 'wait': False, 'buyprice' : 0, 'buyamount' : 0, 'lowerbuy' : False, 'totalbuy' : 0, 'totalamount' : 0, 'rtotalbuy' : 0, 'rtotalamount' : 0, 'fee' : 0, 'rfee' : 0}]
'''
'own' : 코인 매수 여부
'wait' : 매수 코인 주문 대기
'buyprice' : 매수 주문 코인의 매수 가격
'buyamount' : 매수 주문 코인의 매수 수량
'lowerbuy' : 현재가보다 낮은 금액으로 주문했을 경우 판단
'totalbuy' : 매수 주문내에서의 총 주문 금액
'totalamount' : buyamount의 복사본
'rtotalbuy' : 총 누적 매수금액
'rtotalamount' : 총 누적 매수량
rtotalbuy / rtotalamount = 평단가
코인 지정가 매수 주문의 경우
1. wait = True전환, buyprice, buyamount, lowerbuy여부, totalbuy, totalamount값을 boxstudy모듈에서 결정
2. 구매 완료시 wait = False전환, own = True, buyprice, buyamount, lowerbuy여부, totalbuy, totalamount값을 초기화. rtotalbuy, rtotalamount에 값 누적시킴.
3. 구매 취소시 wait = False전환, own = False, buyprice, buyamount, lowerbuy여부, totalbuy, totalamount값을 초기화

코인 지정가 매도 주문의 경우
1. wait = True로 전환(wait가 false인 경우에만 가능하게 함), own = True 검사, buyprice, buyamount, lowerbuy여부, totalbuy, totalamount값을 모듈에서 설정
2. 매도 완료시 wait = False, own = False, buyprice, buyamount, lowerbuy여부, totalbuy, totalamount값을 초기화. rtotalbuy, rtotalamount에서 totalbuy, totalamount값을 차감.
3. 매도 취소시 wait = False전환, own = True유지, buyprice, buyamount, lowerbuy여부, totalbuy, totalamount값을 초기화

'''
# for coin in coin_dict:      # 코인의 각 항목에 접근해서 구매한 코인의 own을 True, buyprice라는 새 항목을 만들어 매수가격 추가
#     if mainticker == coin['ticker']:
#         coin['own'] = True
#         coin['buyprice'] = 2000
        

# for coin in coin_dict:      # 매도할때 다시 코인의 각 항목에 접근해서 구매한 코인을 뽑아 그 코인의 매수가격을 조회
#     if coin['own'] == True:
#         print(coin['buyprice'])

## 매수한 코인 열람