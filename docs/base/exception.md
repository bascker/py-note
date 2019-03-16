# 异常
## 一、raise 语句
raise 语句用于抛出异常
```
>>> raise Exception("It is a exception")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: It is a exception
```

## 二、try-except-else-finally 语句
try-except 语句用于捕获异常, 其中 else 字句只有在没有发生异常的场景下才会执行。
```
def getexception():
    raise Exception("It is a exception")
    
try:
    print("run getexception")
    getexception()
except (Exception) as e:
    print("catch a exception, {}".format(e))
else:
    print("try-except-else")
finally:
    print("try-except-else-finally")
    
>>>
run getexception
catch a exception, It is a exception
try-except-else-finally
```