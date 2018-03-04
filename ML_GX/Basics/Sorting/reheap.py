# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/4 09:47
@ FileName: reheap.py
'''
def LEFT(i):
    return (i * 2 + 1)

def RIGHT(i):
    return (i * 2 + 2)


def adjust_max_heap(L, length, x):
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
            continue
        else:
            break


def build_max_heap(L):
    length = len(L)

    for i in range((int)((length - 1)/2), -1, -1):
        adjust_max_heap(L, length, i)


def heap_sort(L):
    build_max_heap(L)
    i = len(L)
    while i>0:
        tmp = L[i - 1]
        L[i - 1] = L[0]
        L[0] = tmp
        i -= 1
        adjust_max_heap(L, i, 0)


L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
heap_sort(L)
print("heap sort:", L)