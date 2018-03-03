# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 13:18
@ FileName: quick_sort.py
'''

def quick_sort(L, start, end):
    if start < end:
        i, j, pivot = start, end, L[start]
        while i < j:
            while (i < j) and L[j] > pivot:
                j -= 1
            L[i] = L[j]
            while (i < j) and L[i] < pivot:
                i += 1
            L[j] = L[i]
            # if L[i] == L[j]:
            #     j -= 1
        L[i] = pivot
        quick_sort(L, start, j)
        quick_sort(L, j+1, end)

L = [5, 1, 2, 9, 7, 4, 8, 6, 3, 10 ]
quick_sort(L, 0, 9)
print("quick sort:", L)
