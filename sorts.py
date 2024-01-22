def bubble_sort(ar):
    n = len(ar)
    for i in range(n):
        for j in range(i):
            if ar[j] > ar[i]:
                ar[j], ar[i] = ar[i], ar[j]
    print(ar)
def insertion_sort(ar):
    n = len(ar)
    for i in range(1, n):
        temp = ar[i]
        j = i - 1
        while j >= 0 and temp < ar[j]:
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j + 1] = temp
    print(ar)
def selection_sort(ar):
    n = len(ar)
    for i in range(n):
        mx_ind = n - 1 - i
        for j in range(n - i):
            if ar[j] > ar[mx_ind]:
                mx_ind = j
        ar[n - 1 - i], ar[mx_ind] = ar[mx_ind], ar[n - 1 - i]
    print(ar)
def task_of_sort(sp, type_of_sort):
    print(sp)
    print(type_of_sort)
    if type_of_sort == 'пузырьком':
        bubble_sort(sp)
    elif type_of_sort == 'вставкой':
        insertion_sort(sp)
    elif type_of_sort == 'выбором':
        selection_sort(sp)
    else:
        print('Такого способа сортировки нету!')