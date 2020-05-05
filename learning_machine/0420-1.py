import pandas as pd
#file1 = "practice1.npy"
#with open(file1,'rb')as f:
#    a1 = np.load(f)
#a1[a1==-99] =0
#a1[a1 % 3 == 0] = a1[a1 %3==0]/3 #如果是true則%3
#print(a1)
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([1,2,3,4,5],
               index=['a','b','c','d','e'])
data={'a':1,'b':2,'c':3}
s3= pd.Series(data)
print(s2)
dict = {'a':1,'b':2,'c':3}
s4 = pd.Series(data,index=['a','b','d'])
print(s2[0])
print(s2['a'])
print(s2[[1,2,4]])
s4.index =['Eric','Lisa','Amber']
print(s4.sort_valuer())
print(s4 =s4.sort_index(ascending=false))
print(s4 =s4.sort_values(ascending=false,na_positon='first'))

