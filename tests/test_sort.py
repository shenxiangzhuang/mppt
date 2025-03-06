from hypothesis import given, settings
from hypothesis.strategies import floats, lists

from mppt.sort import quick_sort

float_list = lists(floats(allow_nan=False, allow_infinity=False), min_size=0, max_size=50)


class TestQuickSort:
    @given(items=float_list)
    @settings(max_examples=300)
    def test_float(self, items: list[float]) -> None:
        assert quick_sort(items) == sorted(items)
