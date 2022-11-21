#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 统计字符

while True:
    upperLetter = 0
    lowerLetter = 0
    digit = 0
    other = 0
    str = input()  # 输入一行字符串
    if len(str) < 96:
        for ch in str:
            if ch.isupper():
                upperLetter += 1
            elif ch.islower():
                lowerLetter += 1
            elif ch.isdigit():
                digit += 1
            else:
                other += 1
        #输出个数，每个输出占一行
        print(upperLetter)
        print(lowerLetter)
        print(digit)
        print(other)
    else:
        #print("一行字符最多不超过95个")
        pass







