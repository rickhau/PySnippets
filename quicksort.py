#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This code snippet is to do a quicksort

def qsort(L):
    if L == []:
        return L
    pivot = L[0]
    less = [ x for x in L[1:] if x <= pivot ]
    great = [ x for x in L[1:] if x > pivot ]
    return qsort(less) + [pivot] + qsort(great)

if __name__ == "__main__":
    toSort = [100, 7, 1, -3, 0, 10]
    print "Before QuickSort: ", toSort
    print " After QuickSort: ", qsort(toSort)