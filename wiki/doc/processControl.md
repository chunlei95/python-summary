# python中的流程控制语句
## if语句
#### 语句使用格式
* 形式1:
```markdown
if 条件:
    代码块
```
* 形式2:
```markdown
if 条件:
    代码块
elif 条件:
    代码块
elif ...
    ...
else:
    代码块
```
>其中else可以不要.注意冒号
## while语句
```markdown
while 条件:
    代码块
```
## for循环
```markdown
for item in sequnes:
    代码块
```
>使用"in"关键字
## break语句
>跳出当前for或者while循环
## continue语句
>跳出本次循环，执行下一次循环
## 循环(或try)后跟else字句
>1. python中循环语句可以有else字句，语法如下:
```markdown
for item in sequence
    代码块
    break
else:
    代码块
```
>2. 注意：else字句属于for语句，这一点不同于其他编程语言<br/>
>3. 一个循环的else子句在没有发生中断时运行<br/>
>4. 当`item in sequence`条件不满足时，会执行else字句<br/>
>5. 一个try语句的else子句在没有异常发生时会运行
## pass语句
>* pass语句什么都不作
