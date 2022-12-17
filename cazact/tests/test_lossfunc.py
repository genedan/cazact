from cazact.lossfunc import (
    agg_loss,
    frequency,
    pure_premium
)


def test_frequency():
    val = frequency(
        n_policies=200,
        n_claims=5
    )

    assert val == .025


def test_agg_loss():
    val = agg_loss([800, 500])

    assert val == 1300


def test_pure_premium():
    val = pure_premium(
        freq=.05,
        sev=20000
    )

    assert val == 1000
