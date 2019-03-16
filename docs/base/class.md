# 类
## 一、多重继承
python 支持多重继承的语法
```
class Human():
    def toString(self):
        print("I am a human")

class Person():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        
    def toString(self):
        print({"name": self.name, "sex": self.sex})
        
class Student(Person, Human):
    pass
```
多重继承时，一定要注意超类继承顺序。**若超类存在同名方法，则按照继承顺序，顺序在前的方法会重写后面超类的方法**。
如此处 Student.toString() 使用的会是 Person.toString()
```
>>> s = Student("bascker", "man")
>>>
>>> s.toString()
{'name': 'bascker', 'sex': 'man'}
```