# -*- coding:utf-8 -*-
"""
    题目一：实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素
    要求：
        1.pop、push、getMin操作的时间复杂度都是O(1)
        2.设计的栈类型可以使用现成的栈结构
"""


class MyStack(object):
    """
        解法二：基本栈进出操作的同时，选择性进出最小栈
            入栈基本元素的同时，如果基本元素小于等于最小栈的栈顶元素，则同时入栈当前元素到最小栈
            出栈基本元素的同时，如果基本元素等于（不会小于）最小栈的栈顶元素，则同时从最小栈出栈当前元素
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
            选择性的入栈：
            入栈基本元素的同时，如果基本元素小于等于最小栈的栈顶元素，则同时入栈当前元素到最小栈
        """

        # 元素小于等于最小栈的栈顶元素
        if not self._stk_min or item <= self._peek(self._stk_min):
            self._stk_min.append(item)

        self._stack.append(item)

    def pop(self):
        """
            选择性的出栈：
            出栈基本元素的同时，如果基本元素等于最小栈的栈顶元素，则同时从最小栈出栈当前元素
        """
        if self.is_empty():
            raise IndexError

        item = self._stack.pop()
        if item == self._peek(self._stk_min):
            self._stk_min.pop()
        return item

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
    $ python q1_stack_getMin_1.py

    [33] --> [33] --> 33
    [33, 76] --> [33] --> 33
    [33, 76, 29] --> [33, 29] --> 29
    [33, 76, 29, 75] --> [33, 29] --> 29
    [33, 76, 29, 75, 75] --> [33, 29] --> 29
    [33, 76, 29, 75, 75, 48] --> [33, 29] --> 29
    [33, 76, 29, 75, 75, 48, 51] --> [33, 29] --> 29
    [33, 76, 29, 75, 75, 48, 51, 3] --> [33, 29, 3] --> 3
    [33, 76, 29, 75, 75, 48, 51, 3, 25] --> [33, 29, 3] --> 3
    [33, 76, 29, 75, 75, 48, 51, 3, 25, 78] --> [33, 29, 3] --> 3
    [33, 76, 29, 75, 75, 48, 51, 3, 25] --> [33, 29, 3] --> 3
    [33, 76, 29, 75, 75, 48, 51, 3] --> [33, 29, 3] --> 3
    [33, 76, 29, 75, 75, 48, 51] --> [33, 29] --> 29
    [33, 76, 29, 75, 75, 48] --> [33, 29] --> 29
    [33, 76, 29, 75, 75] --> [33, 29] --> 29
    [33, 76, 29, 75] --> [33, 29] --> 29
    [33, 76, 29] --> [33, 29] --> 29
    [33, 76] --> [33] --> 33
    [33] --> [33] --> 33
    """
    import random

    s = MyStack()

    for i in range(10):
        s.push(random.randint(0, 100))
        s.print_stack()

    while not s.is_empty():
        s.pop()
        s.print_stack()
