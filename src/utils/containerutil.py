# -*- coding=utf-8 -*-
# !/usr/bin/python

'''
容器工具类
主要 3 类容器：序列 & 映射 & 集合(set)
1、序列：如列表 & 元组 & 字符串
    1.1 列表 VS. 元组：最大区别是列表可以修改，元组不能
    1.2 字符串是由字符组成的序列
    1.3 列表常见方法:
        1) len() & max() & min()
        2) append(): 末尾追加元素
        3) count(): 统计元素在列表中出现次数
        4) extend(): 在列表 a 末尾追加列表 b 中的多个值。ps: 跟拼接不一样，extend 是直接修改扩展列表 a，而不是重新构造新的列表
        5) index(): 找出第一个匹配项的索引位置
        6) insert(): 将对象插入到列表
        7) pop(): 从列表中移除一个元素(默认最后一个)，并返回该值
        8) remove(): 从列表中移除某个值的第一个匹配项
        9) reverse(); 列表逆序. ps: 修改原始列表
        10) sort(): 列表排序，默认升序. ps: 修改原始列表。参数有 cmp, key, reverse。reverse 为 True，则反向排序
        11) sorted(): 列表排序，默认升序. ps: 返回副本
        12) list(seq): 序列转成列表
        13) cmp(x, y): 比较两个值
    1.4 元组常见方法:
        1) tuple(seq): 序列转成元组
2、映射：如字典
3、集合：set，既不是序列，也不是映射
'''
import logging as logger


SEQ_TYPE = [list, tuple, str]


def is_sequence(value):
    '''
    判断是否是序列
    :param value:
    :return:
    '''
    return type(value) in SEQ_TYPE


#################################
# 序列
#################################
def get(sequence, index):
    '''
    获取序列中 index 位置的元素值
    :param sequence: 序列类型值
    :param index:    索引位置
    :return:
    '''
    if not is_sequence(sequence):
        logger.error("The input params is invalid, sequence supported {}".format(repr(SEQ_TYPE)))
        return None

    return sequence[index]


def split(sequence, start=0, end=0, step=0):
    '''
    切片
    :param sequence: 序列值
    :param start:    开始位置
    :param end:      结束位置
    :param step      步长
    :return:
    '''
    if not is_sequence(sequence):
        logger.error("The input params is invalid, sequence supported {}".format(repr(SEQ_TYPE)))
        return None

    if start < end:
        logger.error("The input param is invalid, start must equals or getter than end")
        return None

    if start == end == 0:
        return sequence[::step]

    return sequence[start:end:step]


def concatenate(seq_x, seq_y):
    '''
    序列拼接
    :param seq_x:
    :param seq_y:
    :return:
    '''
    if not is_sequence(seq_x) or not is_sequence(seq_y):
        logger.error("The input params is invalid, sequence supported {}".format(repr(SEQ_TYPE)))
        return None

    if type(seq_x) != type(seq_y):
        logger.error("The input params is invalid, only the same sequence type can connect")
        return None

    return seq_x + seq_y


def repeat(sequence, time):
    '''
    重复，序列乘法
    :param sequence:
    :param time:
    :return:
    '''
    if not is_sequence(sequence):
        logger.error("The input params is invalid, sequence supported {}".format(repr(SEQ_TYPE)))
        return None

    return sequence * time


def is_exist(sequence, element):
    '''
    判断元素是否存在序列中
    :param sequence:
    :param element:
    :return:
    '''
    if not is_sequence(sequence):
        logger.error("The input params is invalid, sequence supported {}".format(repr(SEQ_TYPE)))
        return False

    return element in sequence


def length(sequence):
    return len(sequence)


def delete(li, index):
    if type(li) != list:
        logger.error("The input param is invalid, li only support list type")
        return

    del li[index]

#################################
#
#################################