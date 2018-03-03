# encoding: utf-8
'''
@ Author: Getfox
@ Date & Time: 2018/3/3 09:57
@ FileName: Insert_shell.py
'''

def insert_shell(L):
    gap = (int)(len(L)/2)
    while(gap>=1):
        for x in range(gap, len(L)):
            for i in range(x-gap, -1, -gap):
                if L[i] > L[i+gap]:
                    tmp = L[i+gap]
                    L[i+gap] = L[i]
                    L[i] = tmp
        gap = (int)(gap/2)



L = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5 ]
insert_shell(L)
print(L)