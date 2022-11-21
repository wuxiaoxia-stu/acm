#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 【数组】成绩统计
while True:
    # python输入一维数组,每个数之间使用空格隔开
    arr = input("")
    num = [int(n) for n in arr.split()] # 将输入每个数以空格键隔开做成数组
    L = len(num)
    #print(num) # 打印数组
    if L < 20:
        # 求平均数
        avge = sum(num)/L
        #print(L)
        # 输出结果
        ans_str = ""
        for n in num:
            if n < avge:
                ans_str += str(n) + " "
            else:
                pass
        print(ans_str[:-1])
    else:
        pass



