# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 12:14
@ FileName: select_sort.py
'''
L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5 ]

def select_sort(L):
    for i in range(1, len(L)):
        for j in range(i):
            if L[j] > L[i]:
                tmp = L[i]
                L[i] = L[j]
                L[j] = tmp

select_sort(L)
print(L)