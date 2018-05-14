#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n
    print(sum)
# calc(*[1,2,3,4,5,6])

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# person('Lmango', 24, (1,2,3), city='beijing', job='front-end')

def fact(n):
    if n is None:
        return 0
    if n == 1:
        return 1
    return n * fact(n - 1)
# print(fact())

# trim 去除首尾多余的空格 
def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return (trim(s[1:]))
    elif s[-1] == ' ':
        return (trim(s[:-1]))
    else:
        return s

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L is None:
        L = []
    if len(L) == 0:
        return (None, None)
    min = max = L[0]
    for v in L:
        if v > max:
            max = v
        elif v < min:
            min = v
    return (min, max)
# print(findMinAndMax())

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
# fib(6)

# 杨辉三角
def triangles(num):
    x, sult = 0, [1]
    while x < num:
        print(sult)
        sult = [1] + [v + sult[i + 1] for i, v in enumerate(sult) if i <= len(sult) - 2] + [1]
        x = x + 1
# triangles(10)

# 利用map跟reduce编写一个str2float函数
from functools import reduce
def str2float(s):
    L = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
    def a(x):
        return L[x]
    r = s.split('.')
    r1 = list(map(a, r[0]))
    r2 = list(map(a, r[1]))
    return reduce(lambda x, y:x * 10 + y, r1) + reduce(lambda x, y:x * 10 +y, r2) / 10**len(r2)
# print(str2float('123123.2212'))

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    LL = str(n)
    y = len(LL) // 2
    if len(LL) == 1:
        return n
    elif LL[:y] == LL[-y:]:
        return n
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))