#Write an iterative function iterPower(base, exp) that calculates the exponential  by simply using successive multiplication. For example, iterPower(base, exp) should compute  by multiplying base times itself exp times. Write such a function below.

#This function should take in two values - base can be a float or an integer; exp will be an integer  0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

def iterPower(base, exp):
    if exp == 0:
        return 1
    result = base
    for i in range(exp - 1):
        result *= base
    return result

print(iterPower(2, 3))