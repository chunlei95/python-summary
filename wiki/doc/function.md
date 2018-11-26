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