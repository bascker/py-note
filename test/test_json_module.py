# -*- coding: utf-8 -*-
import json
'''
json 标准模块
1.dumps(): 把一个Python对象(非自定义类)编码转换成Json字符串
2.loads(): 把一个Json串转为Python对象
'''


class Person:

    def __init__(self, name, age, sex="man"):
        self.name = name
        self.age = age
        self.sex = sex

    def toString(self):
        '''
        转 json
        :return: Map 形式字符串
        '''
        map = {
            "name": self.name,
            "age": self.age,
            "sex": self.sex
        }

        return json.dumps(map, indent=4)


def main():
    person = Person("bascker", 25)
    jsonStr = person.toString()
    print(jsonStr)

    p2 = json.loads(jsonStr)
    print(type(p2))


if __name__ == '__main__':
    main()