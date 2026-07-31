from h1_agent.discrepancy import Discrepancy
from h1_agent.obstruction import cycle_residual


def test_zero_cycle_has_zero_residual() -> None:
    edges = [
        Discrepancy("a", "b", (1.0, 0.0)),
        Discrepancy("b", "c", (0.0, 1.0)),
        Discrepancy("c", "a", (-1.0, -1.0)),
    ]
    assert cycle_residual(edges) == 0.0


def test_nonzero_cycle_has_positive_residual() -> None:
    edges = [
        Discrepancy("a", "b", (1.0, 0.0)),
        Discrepancy("b", "c", (0.0, 1.0)),
        Discrepancy("c", "a", (0.0, 0.0)),
    ]
    assert cycle_residual(edges) > 0.0
