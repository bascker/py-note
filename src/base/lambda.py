# -*- coding: utf-8 -*-

def repeat_print(n):
    '''
    重复打印 str, n 次, str 是匿名参数
    :param n: 重复次数
    :return:
    '''
    return lambda str: str * n


def main():
    pow_x_y = lambda x, y: pow(x, y)

    print("2^3 = ", pow_x_y(2, 3))

    repeat_print_2 = repeat_print(2)
    print(repeat_print_2("hi~ "))


if __name__ == '__main__':
    main()