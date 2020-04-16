
print("-----------------------------------------------------")
score =53
if score >= 60:
    print("及格了")
    if score >= 90:
        print("你最棒!!!")
elif 55<= score <60:
    print('教授拜託調分吧')
else :
    print("被當了")
print("Hello")
print("helle\nword")

print("----------------------------------------------------")
x = 150
print(f"value of x is {x}")
mathScores = [60, 70, 10, 20, 81, 63,4]
firstitem = f"first item in mathscores is {mathScores[0]}"
print(firstitem)
#取長度
firstitem = f"first item in mathscores is {len(mathScores)} items"

for i in range(0,10):
    print(i,end="")
for s in range (10):
    print(s,end="")
print(i)
family = {'dad': 'Hoer', 'mom': 'Marge', 'son': 'Bart', 'daughter': 'Lisa'}
for member in family.items():
    print(member)
for key,value in family.items():
    print(f"my {key} is {value}")

import math
mathScores = [60, 70, 10, 20, 81, 63,4]
for t in mathScores:
    print (math.sqrt(t)*10)
#簡化
[print(math.sqrt(item)*10) for item in mathScores]
count = 0
while count <10:
    print(count)
    count+=1
else :
    print("loop end")
for score in mathScores:
    if score >80 :
        break
    print(score)
for score in mathScores:
    if score >80:
        continue
    print(score)
import random
i = random.randint(1,3)
x = eval(input('How many rows:'))
print(type(x))

for p in range(1,10):
    for j in range(1,10):
        print(f'{p}*{j}={p*j}',end = "")
while count<51:
    print('你好',end='')
    count +=1
else:
    print('我說完了拉')

num = eval(input('Enter a number:'))
for i in range (1,num+1):
    if i %2 == 1:
        print(i)
import math
ls =[]
#先給一個空集合
rows= eval(input("how many row:"))
columns = eval(input("how many columns"))
for i in range(rows):
    ls.append([])
    for j in range(columns):
        num = random.randint(1,100)
        ls[i]
        score[i][j]=random.randint(0,101)
total =0
for i in range(rows):
    row_total = 0
    for j in range(columns):
        row_total +=
#print()換行

x = 123
print(x)
