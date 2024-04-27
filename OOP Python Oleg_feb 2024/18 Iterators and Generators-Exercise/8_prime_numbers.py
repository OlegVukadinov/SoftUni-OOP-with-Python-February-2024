def get_primes(integers: list):
    for i in integers:
        if i > 1:
            prime = True
            for n in range(2, i):
                if i % n == 0:
                    prime = False
                    break
            if prime:
                yield i

#test code
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

#print(list(get_primes([-2, 0, 0, 1, 1, 0])))