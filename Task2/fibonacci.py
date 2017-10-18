#!/usr/local/bin/python3
'''
    * Author: Taha Magdy
    * Date: 18th Oct, 2017


    * Task2
    =======
    * Optimzed version of febonacci() using `memo-ization technique`.
'''


# Memo-ization
# * Here I save febonacci's in a dictiotnary
# * So that I dont need to re-compute what I've already computed

def fib2(n, memorizedFibo={0: 0, 1: 1}):

    # If n is not memo-ized, make a memo for it.
    if n not in memorizedFibo:
        memorizedFibo[n] = fib2(n-1, memorizedFibo) + fib2(n-2, memorizedFibo)

    # return the memo of n
    return memorizedFibo[n]


'''
    * Yes, here we optimized the standard version of fib()
      but it's still not that good becuase of
      the overhead of the recureive calls.

'''
