#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    '''

    primes: list of prime numbers
    test: int

    Generator function that returns a prime number when called.
    '''


    primes = []
    test = 2
    while True:
        prime_num = True
        if test < 2:
            prime_num = False
            pass
        elif test == 2:
            primes.append(2)
        else:
            for num in primes:
                if test % num == 0:
                    prime_num = False
        if prime_num:
            primes.append(test)
            yield test
        test += 1


a = genPrimes()
for i in range(10):
    print(a.__next__())