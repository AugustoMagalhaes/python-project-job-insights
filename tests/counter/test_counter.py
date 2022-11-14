from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "Javascript") == 122
    assert count_ocurrences("src/jobs.csv", "Python") == 1639

    assert not count_ocurrences("src/jobs.csv", "Javascript") > 122
    assert not count_ocurrences("src/jobs.csv", "Python") < 1639
    pass
