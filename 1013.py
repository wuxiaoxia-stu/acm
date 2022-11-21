#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 【排序】数据排序

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
    n = num[0] # 第一个元素作为数组个数
    num1 = num[1:]
    bubbleSort(num1) # 调用函数进行排序

    #print ("排序后的数组:")
    for i in range(len(num1)):
        if i == len(num1)-1:
            print(num1[i])
        else:
            print(num1[i],"", end="")
