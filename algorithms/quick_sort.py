def quick_sort(arr):
    '''
    Быстрая сортировка (алгоритм Хоара)
    Выбирается опорный элемент pivot.
    Все элементы, меньшие либо равные pivot перемещаются влево от него,
    а все элементы, большие либо равные pivot - вправо.
    Далее алгоритм рекурсивно применяется к каждой из частей.
    В чистом виде не работает в Python для больших массивов
    в силу ограниченности уровней вложенности рекурсии.
    '''

    def partition(arr, start, end):
        pivot = arr[(start + end) // 2]
        left = start
        right = end
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        if start < right:
            partition(arr, start, right+1)
        if left < end:
            partition(arr, left, end)

    partition(arr, 0, len(arr)-1)


def quick_sort_iter(arr, low=0, high=-1):
    '''
    Итерационный вариант алгоритма быстрой сортировки
    (без применения рекурсии)
    '''

    if high == -1:
        high = len(arr)-1

    def partition(arr, low, high):
        i = low - 1
        x = arr[high]

        for j in range(low, high):
            if arr[j] <= x:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    size = high - low + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = low
    top += 1
    stack[top] = high

    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        p = partition(arr, low, high)

        if p-1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1

        if p+1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high
