# Super Simple stocks assignment
import time

# Class Super will hold all the functions
class Super:
    def __init__(self, ssymbol, stype, last_div, fixed_div, parval ):
        self.ssymbol = ssymbol
        self.stype = stype
        self.last_div = last_div
        self.fixed_div = fixed_div
        self.parval = parval
        self.trades = []
    
    def calcDivYield(self,market_price):
        if self.stype == 'Common':
            div_yield = self.last_div/market_price
        elif self.stype == 'Preferred': 
            div_yield = (self.fixed_div*self.parval)/market_price
        return div_yield

    def calcPERatio(self,market_price):
        dividend = s.calcDivYield(market_price)
        if dividend == 0:
            pe_ratio = 0
        else:    
            pe_ratio = market_price/dividend
        return pe_ratio
    
    def addTrade(self,symbol, timestamp, quantity, buySell, price):
        trade = {"symbol":symbol,"timestamp": timestamp,"quantity": quantity, "buySell":buySell, "price":price}
        self.trades.append(trade)
        print(trade)   

    def getVWStockPrice(self):
        ctime = int(time.time()) - 15
        trades_15 = list(filter(lambda x:x['timestamp'] > ctime, self.trades))
        print(trades_15)
        total_price = sum(map(lambda x: x['price']*x['quantity'],trades_15))
        total = sum(map(lambda x:  x['quantity'],trades_15))
        if total == 0:
            vw_stock_price = 0
        else:    
            vw_stock_price = total_price/total
        return vw_stock_price
    
    def getmeanStockPrice(self):
        total_price = sum(map(lambda x: x['price']*x['quantity'],self.trades))
        total = sum(map(lambda x: x['quantity'],self.trades))
        if total == 0:
           mean_stock_price = 0
        else:   
           mean_stock_price = total_price/total
        return mean_stock_price

# stocks and dict_trades contain test data
stocks = [{"symbol": 'TEA', "stype": 'Common', "last_div": 0, "fixed_div": 0.0, "par_value": 100},
          {"symbol": 'POP', "sype": 'Common', "last_div": 8, "fixed_div": 0.0, "par_value": 100},
          {"symbol": 'ALE', "stype": 'Common', "last_div": 23, "fixed_div": 0.0, "par_value": 60},
          {"symbol": 'GIN', "stype": 'Preferred', "last_div": 8, "fixed_div": 0.02, "par_value": 100},
          {"symbol": 'JOE', "stype": 'Common', "last_div": 13, "fixed_div": 0.0, "par_value": 250}]

dict_trades = [{"symbol":"TEA","timestamp": int(time.time()),"quantity": 20, "buySell":"Buy", "price":10},
           {"symbol":"TEA","timestamp": int(time.time()),"quantity": 30, "buySell":"Buy", "price":20},
           {"symbol":"POP","timestamp": int(time.time()),"quantity": 10, "buySell":"Buy", "price":40},
           {"symbol":"POP","timestamp": int(time.time()),"quantity": 40, "buySell":"Buy", "price":30},
           {"symbol":"ALE","timestamp": int(time.time()),"quantity": 50, "buySell":"Buy", "price":10},
           {"symbol":"ALE","timestamp": int(time.time()),"quantity": 80, "buySell":"Buy", "price":40},
           {"symbol":"GIN","timestamp": int(time.time()),"quantity": 10, "buySell":"Buy", "price":50},
           {"symbol":"JOE","timestamp": int(time.time()),"quantity": 30, "buySell":"Buy", "price":60}]

# Create right list to hold correct values of symbol
right_list = ['TEA','POP','ALE','GIN','JOE']
len(stocks)

# market price will have market prices for symbols in the following order:
# TEA,POP,ALE,GIN,JOE

market_price = [100, 50, 200, 300, 20]

# Main code that will call the class and functions
sum_total = 0
count = 0
all_share_index = 0
for i in range(0,len(stocks)):
    list_1 = list(dict.values(stocks[i]))
    if list_1[0] in right_list:
        count = count + 1
        s = Super(list_1[0],list_1[1],list_1[2],list_1[3],list_1[4])
        print("Div yield of {} is {}".format(list_1[0],s.calcDivYield(market_price[i])))
        print("PE ratio of {} is {}".format(list_1[0],s.calcPERatio(market_price[i])))
        trades = []
        for j in range(0,len(dict_trades)):
            list_2 = list(dict.values(dict_trades[j]))
            if list_1[0] == list_2[0] and list_2[0] in right_list:
                s.addTrade(list_2[0],list_2[1],list_2[2],list_2[3],list_2[4])
            
        print("VWStockPrice of {} is {}".format(list_1[0],s.getVWStockPrice()))
        print(s.getmeanStockPrice())    
        sum_total = sum_total + s.getmeanStockPrice()
        print(len(trades))

if count > 0:
     all_share_index = sum_total/count 
print("GBCE All Share Index is {}".format(all_share_index))

         
            