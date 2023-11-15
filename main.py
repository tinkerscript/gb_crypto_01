def task3():
    pass


def task4():
    pass


def task5():
    pass


def main():
    task_number = int(input('Введите номер задания: '))

    if task_number == 3:
        task3()
    elif task_number == 4:
        task4()
    elif task_number == 5:
        task5()
    else:
        print(f'Задание с номером {task_number} отсутствует')


if __name__ == '__main__':
    main()
