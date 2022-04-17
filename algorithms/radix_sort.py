def radix_sort(arr):
    '''
    Поразрядная сортировка.
    Массив сортируется с помощью поразрядного сравнения чисел (по битам)
    без использования условного оператора.
    '''

    def counting_sort(arr, exp):

        output = [0] * len(arr)

        count = [0, 0]
        for x in arr:
            index = x >> exp
            count[index & 1] += 1

        count[1] += count[0]

        for x in arr[::-1]:
            index = x >> exp
            count[index & 1] -= 1
            output[count[index & 1]] = x

        for i in range(len(arr)):
            arr[i] = output[i]

    max_val = max(arr)
    exp = 0
    while (1 << exp) <= max_val:
        counting_sort(arr, exp)
        exp += 1
