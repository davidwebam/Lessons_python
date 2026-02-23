class Computation:
    def __init__(self):
        pass

    def factorial(self, n):
        if n < 0:
            raise ValueError("Error")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def sum(self, n):
        if n < 0:
            raise ValueError("Error")
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_is_prime(self, n):
        primes = []
        for i in range(2, n + 1):
            if self.is_prime(i):
                primes.append(i)
        return primes

    def table_mult(self, n):
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

    def all_tables_mult(self):
        for n in range(1, 11):
            print("\nAxyusaky", n)
            self.table_mult(n)


comp = Computation()

print(comp.factorial(5))
print(comp.sum(10))
print(comp.is_prime(7))
print(comp.all_is_prime(20))
comp.table_mult(5)
comp.all_tables_mult()