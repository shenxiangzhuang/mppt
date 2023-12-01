from typing import List, Union

Item = Union[float, int]


def quick_sort(xs: List[Item]) -> List[Item]:
    """
    Quick sort: A very radical implementation
    :param xs: comparable list
    :return: sorted list
    """
    return (
        (
            quick_sort([x for x in xs[1:] if x <= xs[0]])
            + [xs[0]]
            + quick_sort([x for x in xs[1:] if x > xs[0]])
        )
        if len(xs) > 1
        else xs
    )
