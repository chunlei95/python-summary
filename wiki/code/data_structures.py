lists = [1, 2, 3]
# list.append(x)
print(lists)
lists[len(lists):] = [4]
print(lists)
# list.extend(iterable)
extend_list = [5, 6]
lists.extend(extend_list)
print(lists)
lists.extend([7, 8])
print(lists)
# list.insert(i, x)
lists.insert(len(lists), 9)
print(lists)
# list.remove(x)
lists.remove(9)
print(lists)
# 如果要删除的向不存在则报错
# lists.remove(9)
# print(lists)

# list.pop([i])
lists.pop(0)
print(lists)
lists.pop()
print(lists)

# list.clear()
lists.clear()
print(lists)

lists = [1, 2, 3, 4]
# list.index(i[, start[, end])
print(lists.index(2))
print(lists.index(2, 1))
print(lists.index(3, 2, len(lists)))

# list.count(x)
print(lists.count(2))
print(lists.count(5))

lists = [2, 1, 4, 3]
# list.sort(key=None, reverse=False)
# lists.sort(key=None, reverse=False)
# lists.sort()
# lists.sort(key=None, reverse=True)
lists.sort(reverse=True)
print(lists)

lists = [1, 2, 3, 4]
# list.reverse()
lists.reverse()
print(lists)
# list.copy
copy = lists.copy()
print(copy)

# del语句
del lists[1:2]
print(lists)
del lists[0]
print(lists)
# del lists
# print(lists)
del lists[:]
print(lists)

# tuple
my_tuple = ()
print(my_tuple)
my_tuple = (1, 2, "string")
print(my_tuple)
my_tuple = 1, 2, "hello"
print(my_tuple)