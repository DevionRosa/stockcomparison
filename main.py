from crypto import Crypto
from forex import Forex
from stock import Stock

def get_inputs():
    
    stock_name = input("What stock do you want to compare? (EX: AAPL) ")
    stock_name = stock_name.upper()
    
    forex_currency = input("What forex market do you want to check? (EX: EURUSD) ")
    forex_currency = forex_currency.upper()
    
    coin_name = input("What cryptocurrency and currency do you want to check? (EX: BTCUSD) ")
    coin_name = coin_name.upper()
    
    return stock_name, forex_currency, coin_name

def get_reponses(stock_name, forex_name, crypto_name):
    
    #get stock info
    stock = Stock(stock_name)
    stock_info = stock.get()
 
    if stock_info == None:
        print("Can't find that stock.")
    
    #gets forex info
    forex = Forex(forex_name)
    forex_info = forex.get()
    
    if forex_info == None:
        print("Can't find that forex exchange.")

    #get crypto info
       
    crypto = Crypto(crypto_name)
    crypto_info = crypto.get()
    
    if crypto_info == None:
        print("Can't find that coin.")
        
    return stock, forex, crypto

def daily_stock_change(open, close):
    
    percent_change = (close - open)/open *100
    change = round(percent_change, 1)
    
    return change

def compare_prices(stock, forex, coin):
    
    change_list = [stock, forex, coin]
    most_profit = max(change_list)
    print(most_profit)
    return most_profit

def main():
    
    # main information
    stock_name, forex_name, coin_name = get_inputs()
    stock, forex, crypto = get_reponses(stock_name, forex_name, coin_name)
    crypto_open = crypto.open
    crypto_close = crypto.close
    crypto_change = daily_stock_change(crypto_open, crypto_close)

    # # stock infomation
    stock_open = stock.open
    stock_close = stock.close
    stock_change = daily_stock_change(stock_open, stock_close)
    
    # # forex information
    forex_open = forex.open
    forex_close = forex.close
    forex_change = daily_stock_change(forex_open, forex_close)
    
    most_profit = compare_prices(stock_change, forex_change, crypto_change)
    
    if most_profit == crypto_change:
        print(f"{coin_name} would yeild the most profit.")
    elif most_profit == stock_change:
        print(f"{stock_name} would yeild the most profit.")
    elif most_profit == forex_change:
        print(f"{forex_name} would yeild the most profit.")
    
main()
    