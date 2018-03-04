# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/4 09:38
@ FileName: reshell.py
'''

def shell_sort(L):
    gap = (int)(len(L) / 2)
    while(gap>=1):
        for i in range(gap, len(L)):
            for j in range(i - gap, -1, -gap):
                if L[j] > L[gap + j]:
                    tmp = L[gap + j]
                    L[gap + j] = L[j]
                    L[j] = tmp

        gap = (int)(gap/2)


L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
shell_sort(L)
print("shell sort:", L)