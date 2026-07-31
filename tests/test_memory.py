from h1_agent.memory import ObstructionMemory
from h1_agent.obstruction import make_obstruction


def test_repeated_cycle_updates_memory() -> None:
    memory = ObstructionMemory()
    first = make_obstruction(("a", "b", "c", "a"), 0.7, 1, ["first"])
    second = make_obstruction(("a", "b", "c", "a"), 0.75, 2, ["second"])

    memory.add_or_update(first)
    updated = memory.add_or_update(second)

    assert len(memory.items) == 1
    assert updated.recurrence_count == 2
    assert updated.last_seen == 2
