def select_sort(arr):
    '''
    Селективная сортировка (сортировка выбором)
    Делит входной массив на упорядоченную и неупорядоченную части.
    Затем последовательно переносит в первую часть
    наименьшие элементы из второй
    '''

    n = len(arr)
    for i in range(n):
        jmin = i
        for j in range(i+1, n):
            if arr[j] < arr[jmin]:
                jmin = j
        arr[i], arr[jmin] = arr[jmin], arr[i]
