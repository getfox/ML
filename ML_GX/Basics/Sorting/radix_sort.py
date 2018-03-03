# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 16:54
@ FileName: radix_sort.py
'''

def radix_sort_nums(L):
    max = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
    num = 0
    while max > 0:
        max = (int)(max/10)
        num +=1
    return num


def get_pos(num, pos):
    return((int)(num/10**(pos-1))%10)


def radix_sort(L):

    count = 10*[None]
    bucket = len(L)*[None]
    for pos in range(1, radix_sort_nums(L)+1):
        for x in range(0, 10):
            count[x] = 0
        for i in range(0, len(L)):
            numOfPose = get_pos(int(L[i]), pos)
            count[numOfPose] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for x in range(len(L)-1, -1, -1):
            j = get_pos(L[x], pos)
            bucket[count[j]-1] = L[x]
            count[j] = count[j]-1
        for x in range(0, len(L)):
            L[x] = bucket[x]


L = [9, 1, 22, 56, 37, 114, 238, 186, 833, 15, 336, 116]
radix_sort(L)
print("radix_sort:", L)