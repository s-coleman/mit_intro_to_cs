#Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test
#value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach
#a case where the test divides both a and b without remainder, or you reach 1.

def gcdIter(a, b):
    '''
    a, b: positive integers
    test: postive integer

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = max(a, b)
    for i in range(test, 1, -1):
        if a % test == 0 and b % test == 0:
            return test
        else:
            test -= 1
    return 1

print(gcdIter(20, 22))