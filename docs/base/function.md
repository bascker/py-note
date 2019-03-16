# 函数
## 一、参数收集
```
def func(x, y, *params, **keypair):
    print("x = {}, y = {}".format(x, y))
    print("params: {}".format(params))
    print("keypair: {}".format(keypair))
    
>>> func(1, 2, 3, 4, 5, name="bascker", sex="man")
x = 1, y = 2
params: (3, 4, 5)
keypair: {'name': 'bascker', 'sex': 'man'}
```
一个星号，收集到的参数类型就是元组，两个星号，收集到的参数类型就是字典。

## 二、私有化
在方法或者属性前使用两个下划线"__"，就可以让方法或者属性变成私有（外界无法访问）。因为在 python 中，以"__"开始的名称，
都会被解释为类名。
```
class Person:
    def __default(self):
        print(__msg)
        
>>> p = Person()
>>> p.__default()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__default'
```