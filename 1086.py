#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2的n次方

def calc(n):
    if n == 1:
        print('2(0)', end="")
    elif n == 2:
        print('2', end="")
    else:
        p = 1
        s = 0
        while p <= n :
            p = p * 2
            s += 1

        s = s -1
        if  p // 2 == n:
            print('2(',end="")
            calc(s)
            print(')')
        else:
            if p//2 == 2:
                print('2+',end="")
                calc(n - p // 2)
            else:
                print('2(',end="")
                calc(s)
                print(')+',end="")
                calc(n-p//2)

if __name__ == '__main__':
    #print('请输入1个正整数:')
    num = int(input())
    calc(num)


