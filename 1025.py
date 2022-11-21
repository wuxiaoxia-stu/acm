#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 【数组】逆序输出

while True:
    arr = input("")
    num = [int(n) for n in arr.split()]  # 将输入每个数以空格键隔开做成数组
    n = len(num)
    if n < 21:
        for i in range(n // 2):
            num[i], num[n - i - 1] = num[n - i - 1], num[i] # 用第一个与最后一个交换。
        for i in range(n):
            if i == n -1:
                print(num[i])
            else:
                print(num[i],"",end="")
    else:
        pass