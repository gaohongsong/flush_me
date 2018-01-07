# -*- coding: utf-8 -*-
"""
    题目：编写一个类，用两个栈实现队列，支持队列的基本操作：add(put)/poll(get and remove)/peek(get first only)
    要求：
        1.只能用两个栈来实现一个队列
    思路：
        从A栈进入，从B栈弹出，B栈的为A栈的倒置
        仅当B栈为空时，才可以一次性将A栈倒置灌入
"""


# Python中列表即栈
class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self.__getitem__(-1)

    def is_empty(self):
        return self.__len__() == 0


class Queue(object):
    """
        用两个栈来模拟队列的功能
    """

    def __init__(self):
        self._stk_in, self._stk_out = Stack(), Stack()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self._stk_to_list)

    def __len__(self):
        return len(self._stk_to_list)

    @property
    def _stk_to_list(self):
        return self._stk_out[::-1] + self._stk_in

    def _raise_empty(self):
        # 队列为空，抛出异常
        if not self._stk_in and not self._stk_out:
            raise IndexError

    def _fill_stk_out(self):
        # 出队列为空，则先从入队列灌入
        if not self._stk_out:
            while not self._stk_in.is_empty():
                self._stk_out.push(self._stk_in.pop())

    def add(self, item):
        """
        向队尾追加一个元素
        """
        self._stk_in.push(item)

    def poll(self):
        """
        从队头取一个元素
        """
        self._raise_empty()

        # 一次性灌入
        self._fill_stk_out()

        return self._stk_out.pop()

    def peek(self):
        """
        仅获取队首元素的值
        """
        self._raise_empty()
        self._fill_stk_out()
        print '_stk_out: %s' % self._stk_out
        return self._stk_out.peek()

    def eq_list(self, the_list):
        """
        仅获取队首元素的值
        """
        return self._stk_to_list == the_list


if __name__ == '__main__':
    """
    $ python 2.由两个栈组成的队列.py
        
    [9] [9]
    [9, 18] [9, 18]
    [9, 18, 10] [9, 18, 10]
    [9, 18, 10, 14] [9, 18, 10, 14]
    [9, 18, 10, 14, 11] [9, 18, 10, 14, 11]
    =======================================
    [9, 18, 10, 14, 11] [9, 18, 10, 14, 11]
    poll: 9
    _stk_out: [11, 14, 10, 18]
    peek: 18
    [18, 10, 14, 11] [18, 10, 14, 11]
    =======================================
    [18, 10, 14, 11, 5] [18, 10, 14, 11, 5]
    [18, 10, 14, 11, 5, 10] [18, 10, 14, 11, 5, 10]
    [18, 10, 14, 11, 5, 10, 5] [18, 10, 14, 11, 5, 10, 5]
    [18, 10, 14, 11, 5, 10, 5, 19] [18, 10, 14, 11, 5, 10, 5, 19]
    [18, 10, 14, 11, 5, 10, 5, 19, 6] [18, 10, 14, 11, 5, 10, 5, 19, 6]
    =======================================
    [18, 10, 14, 11, 5, 10, 5, 19, 6] [18, 10, 14, 11, 5, 10, 5, 19, 6]
    poll: 18
    [10, 14, 11, 5, 10, 5, 19, 6] [10, 14, 11, 5, 10, 5, 19, 6]
    _stk_out: [11, 14, 10]
    peek: 10
    =======================================
    10
    14
    11
    5
    10
    5
    19
    6
        
    """
    import random

    # 双栈模拟队列
    q = Queue()

    # 跟踪队列
    _q = []

    # put
    for i in range(5):
        num = random.randint(0, 20)
        q.add(num)
        _q.append(num)
        print q, _q
        assert q.eq_list(_q), 'not equal'

    print '======================================='
    print q, _q
    print 'poll: %s' % q.poll()
    _q = _q[1:]
    print 'peek: %s' % q.peek()
    print q, _q
    print '======================================='

    # put
    for i in range(5):
        num = random.randint(0, 20)
        q.add(num)
        _q.append(num)
        print q, _q
        assert q.eq_list(_q), 'not equal'

    print '======================================='
    print q, _q
    print 'poll: %s' % q.poll()
    _q = _q[1:]
    print q, _q
    print 'peek: %s' % q.peek()
    assert q.eq_list(_q), 'not equal'
    print '======================================='

    # get
    for i in range(len(q)):
        print q.poll()
