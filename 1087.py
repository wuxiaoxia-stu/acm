#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy

# 计数问题 https://www.cnblogs.com/ECJTUACM-873284962/p/7744886.html

def calc(num):
    list[0] = 1
    list[1] = 1
    for index in range(2,num+1):
        #print('index is',index)
        list[index] = list[index-1]
        #print(list[index])
        if index % 2 == 0:
            #print('index//2',index//2)
            list[index] += list[index//2]

if __name__ == '__main__':
    num = int(input())
    list = numpy.empty(1001, dtype=object) #初始化空数组
    calc(num)
    print(list[num])

