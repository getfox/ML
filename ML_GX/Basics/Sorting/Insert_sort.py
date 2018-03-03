# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 09:39
@ FileName: Insert_sort.py
'''

L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5 ]

def Insert_sort(L):
    for i in range(1, len(L)):
        for j in range(i-1, -1, -1):
            if L[j] > L[j+1]:
                tmp = L[j+1]
                L[j+1] = L[j]
                L[j] = tmp
    return L

List = Insert_sort(L)
print(List)


