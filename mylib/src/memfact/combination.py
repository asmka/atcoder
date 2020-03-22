from . import factorial
MemorizedFactorial = factorial.MemorizedFactorial

# WARN: Require mod number m is prime number
class MemorizedCombination:
    def __init__(self, n_max: int, *mv: (int)):
        # Check usage
        if len(mv) > 1:
            raise ValueError(f'Usage {self.__class__.__name__}(n_max[, m])')

        # Check arg value
        if n_max < 0:
            raise ValueError(f'Required n_max >= 0, n_max: {n_max}')
        m = None
        if len(mv) == 1:
            m = mv[0]
            if m < 2:
                raise ValueError(f'Require m >= 2, m: {m}')

        mem_fact = None
        mod_inv_factv = None
        if m:
            mem_fact = MemorizedFactorial(n_max, m)
            # List of inverse r! mod m
            mod_inv_factv = [1] * (n_max+1)
            mod_inv_factv[n_max] = pow(mem_fact.factorial(n_max), m-2, m)
            for i in range(n_max-1, 1, -1):
                mod_inv_factv[i] = mod_inv_factv[i+1] * (i+1) % m
        else:
            mem_fact = MemorizedFactorial(n_max)

        self._n_max = n_max
        self._m = m
        self._mem_fact = mem_fact
        self._mod_inv_factv = mod_inv_factv

    # Return nCr or nCr mod m
    def combination(self, n: int, r: int) -> int:
        # Check arg value
        if not (0 <= n and n <= self._n_max):
            raise Exception(f'Required 0 <= n <= n_max, n: {n}, n_max: {self._n_max}')
        if not (0 <= r and r <= n):
            raise Exception(f'Required 0 <= r <= n, r: {r}, n: {n}')

        m = self._m
        mem_fact = self._mem_fact
        mod_inv_factv = self._mod_inv_factv
        comb = None
        if m:
            comb = mem_fact.factorial(n) * mod_inv_factv[r] * mod_inv_factv[n-r] % m
        else:
            comb = mem_fact.factorial(n) // mem_fact.factorial(n-r) // mem_fact.factorial(r)

        return comb
