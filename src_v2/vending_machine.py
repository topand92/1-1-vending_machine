from basic import *
from drink import *
from cash import *

class VendingMachine:
    def __init__(self, init_drink, init_cash): # constructor(생성자)
        # dictionary comprehension(딕셔너리 컴프리헨션), 언패킹 연산자 사용
        self.__drink_dic = {key: Drink(*values) for key, values in init_drink.items()}
        self.__change_dic = {key: Cash(*values) for key, values in init_cash.items()}
    
    def print_drink(self, cash=None, admin=False):
        print("< 판매 중인 상품의 목록 >")
        print_line()

        for key, drink in self.__drink_dic.items():
            print(f"[{key}번]\t{drink.info_drink(cash, admin)}") # f-string
        print_line()
    
    def print_change(self):
        for cash in self.__change_dic.values():
            if cash.get_quantity() < 10:
                print_color("> 현재 거스름돈이 부족합니다. 상품을 판매할 수 없습니다.", 'R')
                print_line()
                return False
        
        print_color("> 현재 거스름돈이 충분합니다. 상품을 구매할 수 있습니다.", 'G')
        print_line()
    
    def input_cash(self):
        amount = 0
        
        for cash in self.__change_dic.values():
            face_value = cash.get_face_value()
            input_count = input_range(f"투입할 {face_value}원의 개수", start=0, end=10)
            amount += face_value * input_count
            cash.set_quantity(cash.get_quantity()+input_count)

        print_color(f"> 투입된 금액: {amount}원", 'B')
        print_line()

        return amount