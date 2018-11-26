lists = [1, 2, 3, 4]
print(lists)
print(str(lists))
print(lists[2])
print(lists[0:3])
# 使用“+”连接两个list
newLists = lists + [5, 6, 7, 8]
print(newLists)
newLists = newLists + lists
print(newLists)
# 修改指定索引处的元素
lists[0] = 2
print(lists)
lists[0:2] = [2, 2]
print(lists)
lists[0:2] = []
print(lists)
# lists[:] = []
# print(lists)
print(len(lists))