"""Sorting algorithms."""


def quick_sort(xs: list[float]) -> list[float]:
    """Quick sort: A very radical implementation.

    Args:
        xs: comparable list

    Returns:
        sorted list

    Examples:
        >>> quick_sort([1, 3, 2, 4, 5])
        [1, 2, 3, 4, 5]
        >>> quick_sort([1.1, 3.3, 2.2, 4.4, 5.5])
        [1.1, 2.2, 3.3, 4.4, 5.5]
    """
    if len(xs) <= 1:
        return xs
    return [*quick_sort([x for x in xs[1:] if x <= xs[0]]), xs[0], *quick_sort([x for x in xs[1:] if x > xs[0]])]
