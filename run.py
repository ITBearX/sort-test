from utils import test_sort_time
from algorithms import (
    bubble_sort, select_sort, quick_sort_iter, radix_sort
)

SIZE = 1000
MAX_VAL = 10000


def run_tests(runs):
    # Функции для тестов. Последняя в списке (sorted) - встроенная в Python
    func_to_test = [
        bubble_sort, select_sort, quick_sort_iter, radix_sort, sorted
    ]
    for func in func_to_test:
        test_sort_time(func, SIZE, MAX_VAL, runs=runs)


if __name__ == '__main__':
    run_tests(100)
