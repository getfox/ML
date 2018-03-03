# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 13:13
@ FileName: bubble_sort.py
'''

def bubble_sort(L):
    for x in range(1, len(L)):
        for y in range(x):
            if L[y] > L[x]:
                tmp = L[x]
                L[x] = L[y]
                L[y] = tmp

L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5 ]
bubble_sort(L)
print("bubbl_sort", L)