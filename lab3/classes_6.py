class Filter:
    def __init__(self, num):
        self.num = num

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def primes(self):
        return list(filter(lambda x: self.is_prime(x), self.num))

num = [1, 2, 3, 4, 5, 6]
prime_filter = Filter(num)
prime_numbers = prime_filter.primes()

print("Prime numbers:", prime_numbers)