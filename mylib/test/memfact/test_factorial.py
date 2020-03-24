import memfact
MemorizedFactorial = memfact.MemorizedFactorial

def test_factorial():
    mf = memfact.MemorizedFactorial(10)
    assert mf.factorial(0) == 1
    assert mf.factorial(5) == 120
    assert mf.factorial(10) == 3628800

def test_mod_factorial():
    mf = memfact.MemorizedFactorial(10, 7)
    assert mf.factorial(0) == 1
    assert mf.factorial(5) == 120%7
    assert mf.factorial(10) == 3628800%7
