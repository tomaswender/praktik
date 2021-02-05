import re
import json



#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.

def create_file(way="folder_lesson5\my_file.txt"):
    while True:
        message = input('Введите текст: ')   
        if message in '':
            break
        else:
            my_file = open(way, 'a')
            my_file.write(message+'\n')
            my_file.close()


#create_file()



#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

def count_line():
    way = "folder_lesson5\my_file2.txt"
    my_file = open(way, 'r')
    content = my_file.readlines()
    print(f'Колличество строк: {len(content)}')

    for i in range(0, len(content)):
        my_set = content[i].split(' ')
        print(f'В строке {i+1}: {len(my_set)} слов')

    my_file.close()

#count_line()




#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

def many():
    way = "folder_lesson5\my_file3.txt"
    my_file = open(way, 'r')
    content = my_file.readlines()
    szp = 0
    print(content)
    for i in range(0, len(content)):
        my_set = content[i].split(' ')
        if int(my_set[1]) < 20000:
            print(f'Сотруник {my_set[0]} имеет ЗП меньше 20000')
        szp +=  int(my_set[1])
    print(f'Средняя ЗП сотрудников: {szp/len(content)}')

#many()

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

def trans():

    transete = {
      'One' : 'Один',
      'Two' : 'Два',
      'Three' : 'Три',
      'Four' : 'Четыре'
    }

    way = "folder_lesson5\my_file4.txt"
    my_file = open(way, 'r', encoding = 'utf-8')
    content = my_file.readlines()
    my_list = []
    for i in range(0, len(content)):
        my_set = content[i].split(' — ')
        key = my_set[0]
        my_list.append(f'{transete[key]} — {my_set[1]}')
    my_file.close()
    for elem in my_list:
        my_file = open("folder_lesson5\my_file4_2.txt", 'a', encoding = 'utf-8')
        my_file.write(elem)
        my_file.close()


#trans()


#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def sumator():
    way="folder_lesson5\my_file5.txt"
    message = input('Введите числа через пробел: ')
    my_file = open(way, 'a')
    my_file.write(message+'\n')
    my_file.close()
    summ = 0
    my_file = open(way, 'r', encoding = 'utf-8')
    content = my_file.readlines()
    my_set = content[0].split(' ')
    for i in range(0, len(my_set)):
        summ += int(my_set[i])
    print(f'Сумма введенных чисел: {summ}')

# sumator()

#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —

#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def school():
    way="folder_lesson5\my_file6.txt"
    my_file = open(way, 'r', encoding = 'utf-8')
    content = my_file.readlines()
    my_dict = {
    }
    for con in content:
        my_set = con.split(':')
        match = re.findall(r'\d+', con)
        summ = 0
        for i in match:
            summ += int(i)
        keys = my_set[0]
        my_dict[keys] = summ       

# school()

#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

#Подсказка: использовать менеджеры контекста.


def firm():
    way="folder_lesson5\my_file7.txt"
    with open(way, encoding = 'utf-8') as firms:
        my_list = []
        profit = 0
        firm_profit = 0
        for line in firms:
            my_set = line.split(' ')
            my_dict = {my_set[0] : (int(my_set[2])-int(my_set[3]))}
            my_list.append(my_dict)
            if int(my_set[2])-int(my_set[3]) >0:
                profit += int(my_set[2])-int(my_set[3])
                firm_profit += 1
        my_list.append({"average_profit": round(profit/firm_profit)})
        print(my_list) 
    with open('folder_lesson5\json_list.json', 'w', encoding = 'utf-8')  as j:
        json.dump(my_list, j)
    
#firm()        