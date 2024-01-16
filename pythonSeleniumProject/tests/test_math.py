import pytest


def add_two_numbers(a, b):
    return a + b


class TestMath:
    @pytest.mark.math
    def test_sum_small(self):
        assert add_two_numbers(1, 2) == 3, "The sum result is correct"

    @pytest.mark.math
    def test_sum_large(self):
        assert add_two_numbers(155, 245) == 400, "The sum is correct"
