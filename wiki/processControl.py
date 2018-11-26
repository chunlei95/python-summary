a = 10
# if 语句
if a < 10:
    print("a < 10")
elif a == 10:
    print("a = 10")
else:
    print("a > 10")
# while 语句
while a == 10:
    a = 0
    print("while a = 10:")
# for循环语句
myList = ['bob', 'jane', 'tom']
for item in myList:
    print(item, len(item))

for item in myList:
    if len(item) > 3:
        myList[myList.index(item)] = item[0:3]
    print(item)
print(myList)

# list.insert
myList.insert(0, 'xzmeasy')
print(myList)