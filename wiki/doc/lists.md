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





















