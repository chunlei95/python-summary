def add(a, b):
    """求两个数字的和"""
    return a + b


def add_new(a, b):
    return 10


print(add(3, 5))
print(add_new(3, 5))


# *args形式的参数
def add_multi(a, *args):
    if len(args) > 0:
        for arg in args:
            a = a + arg
    return a


print(add_multi(1, 2, 3, 4, 5, 6))


# **kwargs形式的參數
def append_string(a, **kwargs):
    if len(kwargs) > 0:
        for arg in kwargs:
            a = a + arg
    return a


print(append_string("a", b="b", c="c"))
se = {"b": "b", "c": "c"}
print(append_string("a", **se))


def lambda_test(a):
    """定义一个函数，该函数返回一个(lambda)函数"""
    return lambda b: b + a  # 返回一个函数，该函数的参数为b, 函数体为 `return b + a`,其中，
# 在返回时，a已经被确定了，因为在调用lambda_test函数时，a必须会被指定


f = lambda_test(10)  # 此时，f就代表一个函数，函数体为 `return b + 10`
print(f(1))
print(f(10))


print(lambda_test.__doc__)