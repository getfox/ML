# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 15:28
@ FileName: merge_sort.py
'''
def mergearray(L, first, mid, last, temp):
    i, j, k = first, mid+1, 0
    while (i <= mid) and (j <= last):
        if L[i] <= L[j]:
            temp[k] = L[i]
            i += 1
            k += 1
        else:
            temp[k] = L[j]
            j += 1
            k += 1
    while (i <= mid):
        temp[k] = L[i]
        i += 1
        k += 1

    while (j <= last):
        temp[k] = L[j]
        j += 1
        k += 1
    for i in range(0, k):
        L[first + i] = temp[i]


def merge_sort(L, first, last, temp):
    if first < last:
        mid = (int)((last + first)/2)
        merge_sort(L, first, mid, temp)
        merge_sort(L, mid+1, last, temp)
        mergearray(L, first, mid, last, temp)

def merge_sort_method(L):
    tmp = len(L)*[None]
    merge_sort(L, 0, len(L)-1, tmp)

L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5 ]
merge_sort_method(L)
print("merge sort:", L)