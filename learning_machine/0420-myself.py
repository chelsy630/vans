import numpy as np
list1 =[1,2,3,4]
list2 =[5,6,7,8]

array1 =np.array(list1,dtype=int)#指定型態
array2 =np.array(list2)
print(type(array1))
print(array1.ndim,array1.shape,array1.dtype) #幾維陣列,矩陣,
array1 = array1.reshape([2,2]) #變成別的形狀的矩陣
print(array1)
array3= np.zeros((2,3),int) #指定成int 型態
print(array3)
array4 =np.ones((3,4))
print(array4)
array5= np.arange(1,10,2) #1頭,10尾,2間隔
print(array5)
array6 =np.full((3,4),10)
print(array6)
array7 = np.zeros_like(array6)
print(array7)
print(np.random.random((2,3)))
print(np.random.randint(0,10,size=(3,3)))
np.random.seed(45962)
a1= np.random.randint(0,10,size=(3,3))
print(a1)
array1 = array1.reshape([2,2])
array2 = array2.reshape([2,2])
print(array1)
print(array2)
array8=np.append(array1,array2)
print(array8)
array9 =np.concatenate((array1,array2),axis=0)
array10 =np.concatenate((array1,array2),axis=1)
print(array9)
print(array10)
print(array9.mean(axis=0))
print(array10.mean(axis=1))
a10 = np.delete(array5,[2,])
print(a10)
array11= np.array([[1,2,3,4],
                  [5,6,7,8],
                   [9,10,11,12]])
print(np.delete(array11,[2,4],axis=0))
print(np.delete(array11,[2,4],axis=1))
array12 = np.full((3,4),10)
print(array12)
#array13 = np.zero_like(array12)
array14 = np.ones_like(array12)
import pandas as pd
#file1 = "practice1.npy"
#with open(file1,'rb')as f:
#    a1 = np.load(f)
#a1[a1==-99] =0
#a1[a1 % 3 == 0] = a1[a1 %3==0]/3 #如果是true則%3
#print(a1)
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([1,2,3,4,5],
               index=['a','b','c','e'])
data={'a':1,'b':2,'c':3}
s3= pd.Series(data)
print(s2)
dict = {'a':1,'b':2,'c':3}
s3 = pd.Series(data,index=['a','b','d'])
print(s2[0])
print(s2['a'])
print(s2[[1,2,4]])

s2[0]=s2[5]
s2.mean[[1,2,4]]
print(s4)
print(s4.fillna(100))
print(s4.fillna(method='ffill'))
print(s4.dropna())
s4 =()
s5 = pd.Series([6,-3,8,5,2,0,7,6,7])
print(s5.rank(pct=true))
s5.rank(method='average')
print(s5.rank(method='average'))
print(s5)
str1 ='台北市中正','台南市東區','台中市西區'
str1 =str1.replace('台','臺')
print(str1)
