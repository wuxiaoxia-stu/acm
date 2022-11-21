#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 【排序】简单排序

def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

while True:
    arr = input("")
    num = [int(n) for n in arr.split()]  # 将输入每个数以空格键隔开做成数组
    bubbleSort(num) # 调用函数进行排序

    #print ("排序后的数组:")
    for i in range(len(num)):
        if i == len(num)-1:
            print(num[i])
        else:
            print(num[i],"", end="")
