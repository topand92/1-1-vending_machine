from basic import *

class Drink:
    # constructor(생성자)
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    # setter(설정자) - name
    def set_name(self, value):
        self.__name = value
    
    # setter(설정자) - price
    def set_price(self, value):
        self.__price = value
    
    # setter(설정자) - quantity
    def set_quantity(self, value):
        self.__quantity = value
    
    def info_drink(self, cash=None, admin=False):
        OUT_OF_STOCK = str_color("재고 없음", 'R')
        AVAILABLE = str_color("구매 가능", 'G')
        CASH_SHORTAGE = str_color("잔액 부족", 'R')
        
        if self.__quantity == 0:
            state = OUT_OF_STOCK
        elif cash is None:
            state = AVAILABLE
        else:
            if self.__price <= cash:
                state = AVAILABLE
            else:
                state = CASH_SHORTAGE
        
        if admin == False:
            return f"{state}\t{self.__price}원\t{self.__name}" # f-string
        else:
            return f"{state}\t{self.__quantity}개\t{self.__price}원\t{self.__name}"