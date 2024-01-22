from sorts import *
from brackets import *
from islands import  *
while True:
    task = input('Введите номер задания(Задания: 1, 2, 3, выход: 4):')
    if task == '1':
        array = input('Введите числа:').split(',')
        array = [int(i) for i in array]
        type_of_sort = input('Введите способ сортировки(пузырьком, вставкой, выбором):')
        task_of_sort(array, type_of_sort)
    elif task == '2':
        brack = input('Введите скобочную последовательность:')
        task_of_brackets(brack)
    elif task == '3':
        task_of_islands()
    elif task == '4':
        break
    else:
        print('Такого задания нету!')