#!/usr/bin/env python
import sys
import math
import random
import time
import numpy as np

def fuc_l(dim):
    a_l=[]
    b_l=[]
    start=time.clock()
    # Generate a and b. (List)
    for i in range(dim):
        a_l.append(random.random())
        b_l.append(random.random())

    # Calculate dot product for 1000 times.
    for i in range(1000):
        np.dot(a_l,b_l)
    end=time.clock()
    print "List cost",end-start,"second(s) with",dim,"dim."

def fuc_a(dim):
    a_a=np.empty(dim)
    b_a=np.empty(dim)
    dot_product=0
    start=time.clock()
    # Generate a and b. (array in numpy)
    for i in range(dim):
        a_a[i]=random.random()
        b_a[i]=random.random()

    # Calculate dot product for 1000 times.
    for i in range(1000):
        np.dot(a_a,b_a)

    end=time.clock()
    print "Arary cost",end-start,"second(s) with",dim,"dim."


if __name__=="__main__":
    dim=10000000
    fuc_l(dim)
    fuc_a(dim)

    dim=100
    fuc_l(dim)
    fuc_a(dim)
    
