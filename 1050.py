#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 【函数】奇偶性

def is_even(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

if __name__ == '__main__':
    #print('请输入要检测数字的个数：')
    n = int(input())
    #print('请输入{}个待检测的整数：'.format(n))
    l = []
    for i in range(n):
        l.append(int(input()))
    for num in l:
        is_even(num)

