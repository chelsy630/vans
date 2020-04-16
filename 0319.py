flag =True
balance =0
drinks = [
    {'name': '可樂','price' : 20},
    {'name': '雪碧','price' : 10},
    {'name': 'tea','price' : 40},
    {'name': '果汁', 'price' : 270},
    {'name': '牛奶', 'price' : 290},
    {'name': '水',  'price' : 30}
]
def deposit():
    global  balance
    value = eval(input('儲值金額:'))
    while value < 1:
        # 若使用者輸入數字小於零,需要重新輸入
        print('=======儲值金額大於0====')
        value = eval(input('儲值金額:'))
    balance += value
    print(f'儲值後金額為{balance}元')
def buy():
    global balance,drinks
    print('\n請選擇商品')
    for i in range(len(drinks)):
        print(f'({i + 1})\t{drinks[i]["name"]}\t{drinks[i]["price"]}元')  # 注意編號 因為編號從1開始
    choose = eval(input('請選擇:'))
    while choose < 1 or choose > 6:
        print('請輸入1~6之間')
        choose = eval(input('請選擇:'))
        buy_drink = drinks[choose - 1]
        if balance < buy_drink['price']:
            print('======餘額不足,需要儲值嗎?========')
            want_deposit =input('y/n?')
        if  want_deposit == 'y' :
            deposit()
        elif want_deposit == 'n':
                break
        else:
            print('====請重新輸入========')
        #儲值後餘額大於商品
    if balance >= buy_drink['price']:
        print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
        balance -= buy_drink["price"]
        print(f'購買後餘額為{balance}元')
while flag:
    print('\n=====================')
    select = eval(input('1.儲值\n 2.購買\n 3.查詢餘額\n 4.離開\n請選擇:'))
    if select ==1: #儲值
        deposit()
    elif select == 2:#購買
        buy()
    elif select == 3:
        print(f"目前餘額是{balance}元")
    elif select == 4:
        print('多謝惠顧')
        flag = false
        break
    else: #重新輸入
        print('=====請輸入1~4之間======')
        continue

weight = 100
weight = 80

def add_weight(w1,w2=1):
    result =w1+ w2
    return

def calculate (x,y):
    return x+y,x-y,x*y,x/y
num1 = 2
num2 = 5
import 0319-2 as calculate():

def acc:
    """

    :return:
    """
