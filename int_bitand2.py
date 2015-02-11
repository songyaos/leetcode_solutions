# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 23:20:39 2015

@author: songyaoshanzhang
"""

def bitand2(M,N):
    mbin = bin(M)
    nbin = bin(N)
    cbin=[]
    if len(mbin) != len(nbin):
        return 0
    else:
        flag = 1
        for (e1,e2) in zip([i for i in mbin],[j for j in nbin]):
            if e1==e2 and flag==1:
                cbin.append(e1)
            else:
                flag=0
                cbin.append('0')
    return int(''.join(cbin),2)
            
print bitand2(5,9)