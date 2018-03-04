# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/4 10:36
@ FileName: requick.py
'''

def quick_sort(L, start, end):

    if start < end:
        i, j, pivot = start, end, L[start]
        while i<j:
            while (i<j) and L[j] > pivot:
                j -= 1
            if i<j:
                L[i] = L[j]
                i += 1
            while (i<j) and L[i] < pivot:
                i += 1
            if i<j:
                L[j] = L[i]
                j -= 1
        L[i] = pivot

        quick_sort(L, start, i-1)
        quick_sort(L, i+1, end)

L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
quick_sort(L, 0, 9)
print("quick sort:", L)