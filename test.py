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

