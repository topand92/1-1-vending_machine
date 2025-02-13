from vending_machine import *

INIT_DRINK = { # { key: [name, price, quantity] }
    1:  ["레쓰비 마일드 커피", 600, 10],
    2:  ["게토레이 레몬", 800, 10],
    3:  ["밀키스", 800, 10],
    4:  ["립톤 아이스티 복숭아", 1000, 10],
    5:  ["칠성사이다", 1000, 10],
    6:  ["트레비 라임", 1000, 10],
    7:  ["트로피카나 스파클링 사과", 1000, 10],
    8:  ["옥수수수염차", 1300, 10],
    9:  ["데일리-C 레몬워터 비타민C 1000", 1500, 10],
    10: ["칸타타 콘트라베이스 콜드브루 블랙", 2000, 0]
}

INIT_CASH = { # { key: [face_value, quantity] }
    1: [ 100, 100],
    2: [ 500, 100],
    3: [1000, 100]
}

vm = VendingMachine(INIT_DRINK, INIT_CASH)

while True:
    vm.print_drink()
    if vm.print_change() == False:
        break
    amount = vm.input_cash()
    break