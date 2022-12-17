from ..lossfunc import (
    pure_premium
)


def test_pp():
    res = pure_premium(freq=.05, sev=100)
    assert res == 5