# -*- coding:utf-8 -*-
"""
    题目一：实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素
    要求：
        1.pop、push、getMin操作的时间复杂度都是O(1)
        2.设计的栈类型可以使用现成的栈结构
"""


class MyStack(object):
    """
        解法一：双栈同入同出，浪费空间，但是思路简明直接
        备注：这里使用的python列表具有栈的功能，支持pop操作
    """

    def __init__(self):
        self._stack = []
        self._stk_min = []

    def _peek(self, stk_list):
        """获取栈顶元素，也就是列表最后一个元素"""
        return stk_list[len(stk_list) - 1]

    def peek(self):
        """返回栈顶元素"""
        return self._peek(self._stack)

    def push(self, item):
        """
            双栈同入
            入栈基本元素的同时，负责维护最小栈
        """
        # 栈为空，直接入栈当前元素
        _item_min = item if self._stk_min == [] else self._peek(self._stk_min)
        item_min = min(_item_min, item)
        # print 'min({}, {}) = {}'.format(_item_min, item, item_min)

        self._stk_min.append(item_min)
        self._stack.append(item)

    def pop(self):
        """
            双栈同出
        """
        if self.is_empty():
            raise IndexError

        self._stk_min.pop()
        return self._stack.pop()

    def min(self):
        """
            获取栈内最小值
        """
        if self.is_empty():
            raise IndexError

        return self._peek(self._stk_min)

    def size(self):
        """
            栈大小
        """
        return len(self._stack)

    def is_empty(self):
        """
            栈判空
        """
        # 这是个坑~
        # return self._stack is []
        return self._stack == []

    def print_stack(self):
        """
            打印栈
        """
        try:
            print '{} --> {} --> {}'.format(self._stack, self._stk_min, self.min())
        except IndexError:
            pass


if __name__ == '__main__':
    """
    $ python q1_stack_getMin.py
    
    [84] --> [84] --> 84
    [84, 93] --> [84, 84] --> 84
    [84, 93, 87] --> [84, 84, 84] --> 84
    [84, 93, 87, 79] --> [84, 84, 84, 79] --> 79
    [84, 93, 87, 79, 65] --> [84, 84, 84, 79, 65] --> 65
    [84, 93, 87, 79, 65, 15] --> [84, 84, 84, 79, 65, 15] --> 15
    [84, 93, 87, 79, 65, 15, 67] --> [84, 84, 84, 79, 65, 15, 15] --> 15
    [84, 93, 87, 79, 65, 15, 67, 1] --> [84, 84, 84, 79, 65, 15, 15, 1] --> 1
    [84, 93, 87, 79, 65, 15, 67, 1, 54] --> [84, 84, 84, 79, 65, 15, 15, 1, 1] --> 1
    [84, 93, 87, 79, 65, 15, 67, 1, 54, 64] --> [84, 84, 84, 79, 65, 15, 15, 1, 1, 1] --> 1
    [84, 93, 87, 79, 65, 15, 67, 1, 54] --> [84, 84, 84, 79, 65, 15, 15, 1, 1] --> 1
    [84, 93, 87, 79, 65, 15, 67, 1] --> [84, 84, 84, 79, 65, 15, 15, 1] --> 1
    [84, 93, 87, 79, 65, 15, 67] --> [84, 84, 84, 79, 65, 15, 15] --> 15
    [84, 93, 87, 79, 65, 15] --> [84, 84, 84, 79, 65, 15] --> 15
    [84, 93, 87, 79, 65] --> [84, 84, 84, 79, 65] --> 65
    [84, 93, 87, 79] --> [84, 84, 84, 79] --> 79
    [84, 93, 87] --> [84, 84, 84] --> 84
    [84, 93] --> [84, 84] --> 84
    [84] --> [84] --> 84   
    """
    import random

    s = MyStack()

    for i in range(10):
        s.push(random.randint(0, 100))
        s.print_stack()

    while not s.is_empty():
        s.pop()
        s.print_stack()
