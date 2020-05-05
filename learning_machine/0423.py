#很重要
str1='台北市中正區、台南市東區、台中市西屯區、彰化縣花壇市'
str2 =str1.replace('台','臺')
print(str1)
ls1 = str1.split('、')
print(ls1)
str2 = 'aaa'.join(ls1)
print(str2)

s6 = pd.Series([str2])
print(s6)
s6=s6.str.replace('臺','台')
print(s6)
s6=s6.str[3:]
print('s6')
data = {
    'Course':['Calculs','Python','Data Mining'],
    'score' :['80','87','92'],
    'name':['Eric','Lisa','Amber']}
df =pd.DataFrame(data)
df =pd.DataFrame(data,index=data['Name'],columns=['Course','Score'])
df['score']
print(df.iloc[:,1])

