# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 12:23
@ FileName: heap_sort.py
'''

L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5 ]

def LEFT(i):
    return(2 * i + 1)

def RIGHT(i):
    return(2 * i + 2)


def adjust_max_heap(L, length, x):
    # largest = x
    while(1):
        left, right = LEFT(x), RIGHT(x)
        if (left < length) and (L[left] > L[x]):
            largest = left
        else:
            largest = x

        if (right < length) and (L[right] > L[largest]):
            largest = right

        if (largest != x):
            tmp = L[x]
            L[x] = L[largest]
            L[largest] = tmp
            x = largest
            # print(largest)
            continue
        else:
            break

def build_max_heap(L):
    length = len(L)
    for x in range((int)((length - 1) / 2), -1, -1):
        adjust_max_heap(L, length, x)

def heap_sort(L):
    build_max_heap(L)

    i = len(L)
    while (i > 0):
        tmp = L[i - 1]
        L[i - 1] = L[0]
        L[0] = tmp
        i-=1
        adjust_max_heap(L, i, 0)

heap_sort(L)
print("heap_sort:", L)
