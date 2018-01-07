# -*- coding: utf-8 -*-
"""
    题目：一个栈中的元素为整数，现在要对栈内数据从大到小排序（从栈顶到栈底）
    要求：
        1.只能申请一个栈，可以申请新的变量，但是不能申请额外的数据结构
    思路：
        对栈A排序，申请栈B做中转
        从栈A弹出元素，放到栈B，确保栈B从顶到底保持从小到大的顺序
            B为空或者元素小于等于B的栈顶元素，则直接推入
            若元素大于B的栈顶元素，则将栈B的元素推入栈A直到满足上述条件，然后推入元素
"""


# Python中列表即栈
class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self.__getitem__(-1)

    def is_empty(self):
        return self.__len__() == 0

    def pop_all(self):
        while not self.is_empty():
            print self.pop()


def sort_stack(s):
    """
    栈排序，从顶到底，从大到小
    """

    # 中转栈，排序后中转栈的元素从栈顶到栈底排序为从小到大（形象看来就像摞盘子，汉诺塔？）
    _s = Stack()
    while not s.is_empty():
        item = s.pop()

        # 等价写法一
        # if _s.is_empty() or _s.peek() >= item:
        #     _s.push(item)
        # else:
        #     # 将栈_s的元素推入栈s直到_s的栈顶大于等于item或者_s为空
        #     while not _s.is_empty() and _s.peek() < item:
        #         s.push(_s.pop())
        #     _s.push(item)

        # 等价写法二
        # 将栈_s的元素推入栈s直到_s的栈顶大于等于item或者_s为空
        while not _s.is_empty() and _s.peek() < item:
            s.push(_s.pop())
        _s.push(item)

    # 把中转栈的内容"倒灌"回原始栈中
    while not _s.is_empty():
        s.push(_s.pop())


if __name__ == '__main__':
    """
    $ python 3.用一个栈实现另个一栈的排序.py
    [72, 74, 40, 100, 58, 28, 31, 19, 82, 90]
    100
    90
    82
    74
    72
    58
    40
    31
    28
    19
    """
    import random

    s = Stack()
    for i in range(10):
        s.push(random.randint(0, 100))

    print s
    sort_stack(s)
    s.pop_all()
