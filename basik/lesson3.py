import math

#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def f_del(a, b):
    if b == 0:
        print('На ноль делить нельзя')
    else:
        print(a/b)


#a = int(input('Весдите первое число: '))
#b = int(input('Весдите второе число: '))
#f_del(a, b)    
    

#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, 
# телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def f_data(**kwargs):
    date = kwargs
    return f"Имя: {date['first_name']} Фамилия: {date['last_name']} Год рождения: {date['date']} город: {date['city']} email: {date['mail']} телефон: {date['phone']}"


#print(f_data(first_name=1, last_name='2', date=3, city=5, mail=3, phone=4))

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = []
    if a >= b:
            my_list.append(a)
    if b >= c:
            my_list.append(b)
    if c >= a:
            my_list.append(c)
    else:
        my_list.append(a)

    return sum(my_list)

# print(my_func(6, 2, 22))



#4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. 
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func3(x, y):
    return math.pow(x, y)


def my_func2(x, y):
    result = x
    for i in range(1, int(math.fabs(y))):
        result = result*x
        i+=1
    return 1/result  


# print(my_func(8, -3))

#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, 
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def f_sum():
    chek = 0
    res = 0
    while chek != 1:
        answer = input('Введите числа через пробел: ')
        my_set = answer.split(' ')
        my_array = []
        for i in range(0, len(my_set)):
            if my_set[i] in '/':
                chek = 1
                break
            else:
                my_array.append(int(my_set[i]))
        print(f'Сумма текущих значений: {sum(my_array)}')
        res += sum(my_array)   
        print(f'Сумма всех значений: {res}')
    print('Работа программы окончена')


# f_sum()
        



#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(answer):
    my_set = answer.split(' ')
    for i in range(0, len(my_set)):
        my_set[i] = my_set[i].capitalize()
    print(my_set)

# int_func('answer')    