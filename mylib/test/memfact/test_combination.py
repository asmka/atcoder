import memfact
MemorizedCombination = memfact.MemorizedCombination

def test_combination():
    mc = MemorizedCombination(10)
    assert mc.combination(0, 0) == 1
    assert mc.combination(10, 10) == 1
    assert mc.combination(5, 2) == 10
    assert mc.combination(5, 3) == 10

def test_mod_combination():
    mc = MemorizedCombination(10, 11)
    assert mc.combination(0, 0) == 1%11
    assert mc.combination(10, 10) == 1%11
    assert mc.combination(8, 3) == 56%11
    assert mc.combination(8, 5) == 56%11
