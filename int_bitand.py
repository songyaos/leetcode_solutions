# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 22:45:04 2015

@author: songyaoshanzhang
"""

def bitand(M,N):#assume N>=M
    nbin = bin(N)
    clist=['0' for _ in nbin]
    clist[1]='b'
    index=1
    for element in nbin[2:]:
        print element
        index = index +  1
        if element =='0':
            clist[index]='0'
        else:
            temp = [i for i in nbin]
            temp[index]='0'
            for i in range(index+1,len(nbin)):
                temp[i]='1'
            print int(''.join(temp),2)
            if int(''.join(temp),2) >= M:
                clist[index] ='0'
            else:
                clist[index] ='1'
    
    return int(''.join(clist),2)
    
print bitand(12,100)
            