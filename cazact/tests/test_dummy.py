from ..lossfunc import (
    pure_premium
)


def test_pp():
    res = pure_premium(freq=.05, sev=100)
    assert res == 5


def test_pp2():
    res = pure_premium(freq=.05, sev=200)
    assert res == 10
