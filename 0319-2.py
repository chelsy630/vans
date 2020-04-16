weight = 100
weight1 = 80

def add_weight(w1=3,w2=4):
    result =w1+ w2
    result1 = w1/w2
    return result,result1
x,y = add_weight()
print(x,y)
def calculate (x,y):
    return x+y,x-y,x*y,x/y
num1 = 2
num2 = 5
result2 = calculate(num1,num2)
print(result2)

r1,r2,r3,r4 =calculate(num1,num2)
print(r1,r2,r3,r4)
