# 数据结构
## list相关方法
#### `list.append(x)`
>将项添加到列表的末尾。相当于`lists[len(a):] = [x]`,右边的值是一个可迭代的列表
#### `list.extend(iterable)`
>通过附加iterable(一个可迭代的列表或序列)中的所有项来扩展列表,相当于`lists[len(a):] = iterable`
#### `list.insert(i, x)`
>在给定位置插入项目。第一个参数是要插入的元素的索引，因此`a.insert(0,x)`插入列表的前面，而`a.insert(len(a),x)`等同于`a.append(x)`
#### `list.remove(x)`
>从列表中删除值为x的第一项。如果没有这样的一项则报错。
#### `list.pop([i])`(方括号表示是可选的)
>* 删除列表中给定位置的项，然后将其返回;
>* 如果未指定索引，则`a.pop()`将删除并返回列表中的最后一项
#### `list.clear()`
>从列表中删除所有项。相当于`del a[:]`
#### `list.index(x[, start[, end]])`
>* 返回值为x的项在列表中的索引，索引从0开始
>* 可选参数用于指定一个区间，并在这个区间中查找值为x的项，但是返回的索引值依然是相对于整个列表的
>* 如果在整个列表或者start和end决定的列表中没有找到值为x的项，则报错ValueError
#### `list.count(x)`
>获取值为x的项在列表中出现的次数
#### `list.sort(key=None, reverse=False)`
>对列表中的项进行排序,参数可用于自定义排序规则
#### `list.reverse()`
>反转列表中的元素
#### `list.copy()`
>返回列表的浅表副本。相当于a[:]
## 使用列表作为堆栈
>* list方法可以很容易地将列表用作堆栈，其中添加的最后一个元素是检索到的第一个元素（“last-in，first-out”）
>* 要将项添加到堆栈顶部，请使用append()。要从堆栈顶部检索项目，请使用不带显式索引的pop()
## 使用列表作为队列
>* 也可以使用列表作为队列，其中添加的第一个元素是检索的第一个元素（“先进先出”）
>* 但是，列表不能用于此目的。虽然列表末尾的追加和弹出很快，但是从列表的开头进行插入或弹出是很慢的（因为所有其他元素都必须移动一个）
>* 要实现队列，请使用`collections.deque`，它设计为具有快速追加和两端弹出
## [list列表推导](https://docs.python.org/3.6/tutorial/datastructures.html#list-comprehensions)
## del语句
>* del语句可以用来删除列表中的一项或者一个切片来执行删除操作，例如:
```markdown
        del lists[0]  # 删除列表中索引为0的项
        del lists[0:2]  # 删除列表中索引为0, 1的两项
        del lists[:]  # 清空整个列表
```
>* del语句也可以用来直接删除变量：`del lists`,此时，列表变量`lists`已经不存在了，任何对它的引用都会报错:NameError
## 元组和序列
>* 目前python中的序列数据类型包括:string(字符串), list(列表), tuple(元组), range(范围)
>* 元组是由逗号分割的多个值组成，创建是可以使用小括号括起来，也可以不使用，通常建议使用(易于区分)
>* 元组可以嵌套，嵌套的元组使用小括号"()"括起来
>* 元组是不可变的，但是元组可以包含可变对象
## set
>* set是无序的，并且没有重复元素
>* 基本用途包括成员资格测试(判断一个元素是否是其成员:通过`a in sets`形式, `not in`在python中也是一个关键字)和消除重复条目。set对象还支持数学运算，如并集，交集，差集和对称差异
>* 创建一个set可以使用{}或者set()函数，但是需要注意的是:当创建一个空set集合时，必须使用set()函数来创建，因为一个空的{}表示创建一个字典(dict)类型
>* set支持以下操作:
```markdown
        # a和b都是一个set
        a - b  # 获取a中有而b中没有的元素的集合
        a | b  # 获取a中有或者b中有的元素的集合
        a & b  # 获取a中有并且b中也有的元素的集合
        a ^ b  # 获取不是同时在a和b中都有的元素的集合
```
>* set集合也支持推导语法,例如：
`a = {x for x in 'abracadabra' if x not in 'abc'}`(not in也是一个关键字操作符)
## dict(字典)
>* key:value对的形式，{}用于创建一个空的dict，也可以使用`dict()`构造函数直接从键值对序列构建字典
>* dict中的项是无序的且唯一的，任何不可变对象都可以作为dict的key
>* 可以通过del语句删除指定key的dict项:`del dicts[key]`
>* 可以使用in关键字判断一个key是否在dict中:`key in dicts.keys()`,`dicts.keys()`获取字典中的所有的键
>* dict也支持推导,例如:`{x: x**2 for x in (2, 4, 6)}`
### 遍历字典
>遍历字典可以使用item()方法，同时检索键和对应的值，例如:
```markdown
        knights = {'gallahad': 'the pure', 'robin': 'the brave'}
        for k, v in knights.items():
            print(k, v)
```