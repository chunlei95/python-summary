# python中的函数
## 定义函数
>* 使用关键字“def”来定义一个函数，且“def”后面需要定义函数名以及小括号包含的参数列表
>* 函数体的第一条语句可以选择为一个字符串文字，该字符串文字被表示为函数的说明文档
>* 所有没有return语句的函数都有一个返回值为“None”
### 指定默认参数值
>* python中函数的参数可以指定默认值，使用形式是直接在方法的定义中给参数设置值，该值就是参数的默认值，<br/>
调用时如果没有传值，则会使用默认值
>* 如果默认值是一个可变对象，则多次调用函数时可能会产生差异，因为默认值可能会被改变，如果想禁止这种状况<br/>
可以使用以下形式(参考的是用法，不是说就这样用):<br/>
   ```markdown
        def f(a, L=None):
           if L is None:
               L = []
           L.append(a)
           return L
   ```
### 调用函数时参数使用关键字
定义以下函数:
```markdown
    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", type)
        print("-- It's", state, "!")
```
则在调用函数时可以使用以下形式:
```markdown
    parrot(1000)                                          # 1 positional argument
    parrot(voltage=1000)                                  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```
通过给定“参数名称 = 值“的参数形式给函数中指定名称的参数赋值
>注意项:<br/>
>* 非关键字参数不能在关键字参数后面，例如，如下调用方式是错误的:<br/>
`parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument`<br/>
>* 如果使用了关键字参数，则参数传递的顺序就不重要了
## <strong>**kwargs</strong>形式的参数
>也叫关键字参数，函数调用时，该参数需要使用关键字的形式传递
>如果在定义函数的时候定义了`**kwargs`形式的参数，则表示该参数接受一个字典(dict)类型,dict类型类似与java中的Map,<br/>
>在传递该参数时，可以传递任意key/value对(多个使用逗号隔开，"="前后不要有空格)，但是key不能同函数定义时其他参数的<br/>
名称相同
## <strong>*args</strong>(定义任意参数列表)
>* `*args`表示定义了一个可变参数列表
>* 通常情况下，可变参数列表的定义要在函数参数列表的最后一个定义，但是有一种例外情况就是若存在`**kwargs`形式的参数<br/>
则`*args`需要在`**kwargs`前面定义 
## 解压缩参数列表
>在给可变参数列表传递参数时，如果要传递的参数已经在一个列表或者序列中定义好了，则在传递的时候需要加上"*"符号，具体如下:
```markdown
        def add(a, *args):
            """定义了一个可变参数列表*args"""
            if len(args) > 0:
                a = a + arg
            return a
            
            
        lists = [1, 2, 3, 4]  # 定义一个列表，列表中元素就是要传递给上面定义的方法中*args参数的
        print(add(0, lists))  # 如果这样传递lists，程序将会报错
        print(add(0, *lists))  # 正确的传递lists的形式应该时这样
```
>在给关键字参数(**kwargs)传递参数时，情况同`*args`形式，例如：
```markdown
        def append(a, **kwargs):
            """定义了一个关键字参数**kwargs"""
            if len(kwargs) > 0:
                for arg in kwargs:
                    a = a + arg
            return a
            
         
        s = {"b": "b", "c": "c", "d": "d"}  # 定义一个dict，里面的元素就是要传递给上面定义的方法中**kwargs参数的
        print(append("a", s))  # 错误的传递方式
        print(append("a", **s))  # 正确的传递方式
```
## lambda表达式
>* 可以使用lambda关键字创建小的匿名函数
>* 另一个用途是传递一个小函数作为参数
>* Lambda函数可以在需要函数对象的任何地方使用
>* 它们在语法上限于单个表达式

>举例说明：
```markdown
        def lambda_test(a):
            """定义一个函数，该函数返回一个(lambda)函数"""
            return lambda b: b + a  # 返回一个函数，该函数的参数为b, 函数体为 `return b + a`,其中，
        # 在返回时，a已经被确定了，因为在调用lambda_test函数时，a必须会被指定


        f = lambda_test(10)  # 此时，f就代表一个函数，函数体为 `return b + 10`
        print(f(1))  # 结果为11
        print(f(10))  # 结果为20
```