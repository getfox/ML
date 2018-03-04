# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/4 11:22
@ FileName: reradix.py
'''
def get_num_pos(num, pos):
    return((int)(num/10**(pos-1))%10)


def get_max_digit(L):
    max = L[0]
    for i in range(len(L)):
        if L[i] > max: max = L[i]
    digit = 0
    while max > 0:
        max = (int)(max/10)
        digit += 1
    return digit


def radix_sort(L):
    count = 10 * [None]
    bucket = len(L) * [None]

    for pos in range(1, get_max_digit(L)+1):

        for i in range(0, 10):
            count[i] = 0

        for i in range(0, len(L)):
            j = get_num_pos(L[i], pos)
            count[j] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(L)-1, -1, -1):
            j = get_num_pos(L[i], pos)
            bucket[count[j] - 1] = L[i]
            count[j] -= 1

        for i in range(0, len(L)):
            L[i] = bucket[i]


L = [9, 1, 22, 56, 37, 114, 238, 186, 833, 15, 336, 116]
radix_sort(L)
print("radix sort:", L)