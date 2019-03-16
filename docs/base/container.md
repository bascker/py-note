# 容器
## 一、列表推导式
列表推导式即利用其它列表创建新列表的一种方法。
```
$ [(x, y) for x in range(10) for y in range(10, 20) if x * 2 == y ]
[(5, 10), (6, 12), (7, 14), (8, 16), (9, 18)]
```
等价于下面 for 循环
```
result = []
for x in range(10):
    for y in range(10, 20):
        if x * 2 == y:
            result.append((x, y))
```