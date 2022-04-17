from random import randint
from time import perf_counter_ns

WHITE = '\033[0m'
CYAN = '\033[96m'
GREEN = '\033[92m'


def test_sort_time(func, arr_size, max, runs=1000, output=True):
    '''
    Выполняет runs прогонов заданной функции сортировки func и вычисляет
    среднее время сортировки.
    На каждом прогоне заполняет массив из arr_size элементов
    случайными числами от 0 до max-1 и сортирует его с помощью
    заданной функции.
    func - функция сортировки
    arr_size - размер генерируемого массива
    max - максимально возможное значение в массиве
    runs - количество прогонов
    output - выводить или нет процесс на экран (булевская переменная)
    Возвращает среднее время сортировки в наносекундах
    '''

    total_time = 0
    for run in range(runs):
        if output:
            print(
                f'{WHITE}Testing {CYAN}{func.__name__}'
                f'{WHITE}: run {GREEN}{run}',
                end='\r'
            )
        arr = [randint(0, max) for _ in range(arr_size)]
        start = perf_counter_ns()
        func(arr)
        stop = perf_counter_ns()
        total_time += (stop - start)

    avg_time = total_time / runs
    if output:
        print(
            f'{CYAN}{func.__name__}: {GREEN}{runs} {WHITE}runs, '
            f'{GREEN}{avg_time // 1e3} μs {WHITE}average'
        )

    return avg_time
