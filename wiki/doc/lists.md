# python中的list
1. python中的list可以包含不同的类型，但是通常其中的数据都是同一类型
1. 创建一个list：
`lists = [1, 2, 3 ,4]`,
各个元素之间使用逗号隔开
## 索引
* lists[index],index从0开始
* index可以为负数,表示从右边开始取数据

## 切片(获取子集)
* lists[start:end]
* 使用方式同string类型[(string类型切片操作)](https://github.com/xzmeasy/python-summary/blob/master/wiki/summary.md#%E8%8E%B7%E5%8F%96%E4%B8%80%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2strstartend)
## list连接
>可以使用“+”连接两个list,例如:
```
    lists = [1, 2, 3]
    newList = lists + [4, 5, 6, 7]
```
>则newList中的元素为[1, 2, 3, 4, 5, 6, 7]
## 常用方法操作
>添加元素(末尾):list.append(),此方法比“+”效率要高<br/>
>添加元素(指定位置):list.insert(index, data)<br/>
>获取list中元素个数:len(list)<br/>
>创建一个list:list(object),从一个可迭代的对象创建一个list<br/>

## 修改list中元素
>*. `lists[start:end] = [...]` 将指定位置的元素替换<br/>
>*. `lists[start:end] = []` 将指定位置的元素清空<br/>
>*. `lists[:] = []` 清空lists<br/>
>*. `lists[index] = x` 修改指定索引处的元素 
## 遍历列表
>遍历列表可以使用`enumerate()`函数，可以同时检索索引和对应的值，例如:
```markdown
        for i, v in enumerate(['tic', 'tac', 'toe']):
            print(i, v)  # i表示列表中元素的索引,v表示索引对应的元素的值
```
## 序列的遍历使用
#### 要同时遍历多个序列,可以使用`zip()`函数，例如:
```markdown
        questions = ['name', 'quest', 'favorite color']
        answers = ['lancelot', 'the holy grail', 'blue']
        for q, a in zip(questions, answers):  # q表示questions中的元素,a表示answers中的元素
            print(q, a)
```
#### 反向循环序列,可以使用reversed()函数
```markdown
        for i in reversed(range(1, 10, 2)):
            print(i)
```
#### 按排序顺序循环序列，可以使用sorted()函数
>sorted()函数返回新的排序列表，同时保持源不变
```markdown
        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        for f in sorted(set(basket)):
            print(f)
```
>注意：在python中`is`和`not is`和`and`, `or`, `not`也是操作符





















