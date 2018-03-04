# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/4 11:05
@ FileName: remerge.py
'''


def mergeArray(L, start, mid, end, tmp):
    i, j, k = start, mid+1, 0
    while (i<=mid) and (j<=end):

        if L[i] <= L[j]:
            tmp[k] = L[i]
            i += 1
            k += 1

        else:
            tmp[k] = L[j]
            j += 1
            k += 1
    while (i <= mid):
        tmp[k] = L[i]
        i += 1
        k += 1
    while (j <= end):
        tmp[k] = L[j]
        j += 1
        k += 1
    for i in range(k):
        L[start + i] = tmp[i]

def merge_sort(L, start, end, tmp):
    if start < end:
        mid = (int)((start + end)/2)
        merge_sort(L, start, mid, tmp)
        merge_sort(L, mid+1, end, tmp)
        mergeArray(L, start, mid, end, tmp)


def merge_sort_method(L):
    tmp = len(L) * [None]
    merge_sort(L, 0, len(L)-1, tmp)


L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5 ]
merge_sort_method(L)
print("merge sort:", L)