mathScores = [60, 70, 10, 20, 81, 63]
print(mathScores)
mathScores2 = []
mathScores2.append(60)
print(mathScores2)
mathScores2.insert(2, 30)
print(mathScores2)
mathScores2.remove(30)
print(mathScores2)
print(mathScores2)
print(33 in mathScores2)
print(mathScores2 + mathScores)
print(sorted(mathScores, reverse=True))
ls = [[1, 2, 3], [4, 5, 600]]
print(ls[1][1])
grade = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
# 平均
grade[0][1] = 20
print(grade)
print(sum(grade[0]) / len(grade[0]))
print(sum(grade[1]) / len(grade[1]))
print(sum(grade[2]) / len(grade[2]))
print([])
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 3, 4, 5, 6)
print(tuple1)
print(sorted(tuple1, reverse=True))
tuple1 = (88, 12, 20)
x, y, z = tuple1
print(x)

gradestuple = ((5, 14, 7), (23, 36, 28), (88, 80, 92))
print(gradestuple[1])
print(sum(grade[0]) / len(grade[0]))
print(sum(grade[1]) / len(grade[1]))
print(sum(grade[2]) / len(grade[2]))

family = {'dad': 'Hoer', 'mom': 'Marge', 'son': 'Bart', 'daughter': 'Lisa'}
print(family["dad"])
print(family.get("dog"))
print("dog" in family)
print(family.keys())
for item in family.items():
    print(item)
family.update({'uncle': 'Martin', 'aunt': 'May'})
# 刪除 uncle
del family['uncle']
print(family)

print(family)
gradeDict = {'chinese': [5, 14, 7], 'english': [23, 36, 28], 'math': [88, 80, 92]}

print(sum(gradeDict['chinese']) / len(gradeDict['chinese']))
print(sum(gradeDict['english']) / len(gradeDict['english']))
print(sum(gradeDict['math']) / len(gradeDict['math']))

gradeDict.update({'science': [94, 90, 96]})
print(gradeDict)

# set
fruits = {'apple', 'banana', 'guava'}
fruits.add('watermelon')
print(fruits)
