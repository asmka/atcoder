class MemorizedFactorial:
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
            if m < 0:
                raise ValueError(f'Require m >= 0, m: {m}')

        # List of n! mod m
        factv = [1] * (n_max+1)
        for i in range(2, n_max+1):
            if m:
                factv[i] = factv[i-1] * i % m
            else:
                factv[i] = factv[i-1] * i

        self._n_max = n_max
        self._m = m
        self._factv = factv

    # Return n! or n! mod m
    def factorial(self, n: int) -> int:
        if n > self._n_max:
            raise ValueError(f'n is larger than n_max, n: {n}, n_max: {self._n_max}')

        return self._factv[n]
