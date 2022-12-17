def severity() -> float:
    pass


def frequency(
        n_policies: int,
        n_claims: int
) -> float:

    res = n_claims / n_policies

    return res


def agg_loss(
        losses: list
) -> float:

    return sum(losses)


def pure_premium(
        freq: float,
        sev: float
) -> float:

    return freq * sev
