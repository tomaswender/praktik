


# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date
    @classmethod
    def prep_date(cls, obj):
        results = obj.date.split('-')
        result = [int(i) for i in results]
        return result
    @staticmethod
    def valid(obj):
        if obj[1] in range(1,13):
            if (obj[2]%4 == 0) & (obj[1] == 2) & (obj[0]<=29):
                return obj
            if (obj[2]%4 != 0) & (obj[1] == 2) & (obj[0]<=28):
                return obj
            if (obj[1]%2 == 0) & (obj[0]<=30):
                return obj
            if (obj[1]%2 != 0) & (obj[0]<=31):
                return obj
            else:
                return 'Не корректный день'
        else:
            return 'Не корректный месяц'    


# d = Date('30-04-2003') 
# prep = Date.prep_date(d)
# print(Date.valid(prep))   

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
#  При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Try:
    def __init__(self, a):
        self.a = a

    def __truediv__(self, other):
        if other.a !=0:
            return self.a/other.a
        else:
            return 'Деление на ноль запрещено'

# a = Try(7)
# b = Try(5)
# print(a/b)           


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. 
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
#  При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class Stop(Exception):
    pass

class Error:
    @classmethod
    def inp(cls):
        my_list = []   
        while True:
            try:
                n = input("Введите число: ")
                if n == 'stop':
                    raise Stop
                else:
                    n = int(n)
                    my_list.append(n)
            except Stop:
                print(f'Итоговый список: {my_list}')
                break
            except ValueError:
                print('Неверный формат')


#Error.inp()   

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    warehouse = []
    def __init__(self, types, count, place, name):
        self.types = types
        self.count = count
        self.place = place
        self.name = name
    @classmethod
    def receipt(cls, obj):
        my_dict = {
            'types' : obj.types,
            'count' : obj.count,
            'place' : obj.place,
            'name' : obj.name          
        }
        cls.warehouse.append(my_dict)
        print(cls.warehouse)
    def update(self, id, key, value):
        self.warehouse[id][key]=value
        print(self.warehouse)
class Office:
    def __init__(self, speed, dpi, name, laser=False):
        self.speed = speed
        self.dpi = dpi
        self.type = name
        self.laser = laser
class Printer(Office):
    def __init__(self, speed, dpi, name, volume, paper, laser=False):
        super().__init__(speed, dpi, name, laser=laser)
        self.volume = volume
        self.paper = paper             
class Scanner(Office):
    def __init__(self, speed, dpi, name, resolution, laser=False):
        super().__init__(speed, dpi, name, laser=laser)
        self.resolution = resolution
class Copier(Office):
    def __init__(self, speed, dpi, name, network=False, laser=False):
        super().__init__(speed, dpi, name, laser=laser)
        self.network = network

s = Storage('Printer', 10, 'home', 'HP')
Storage.receipt(s)
s.update(0, 'count', 2)


# дальнейшее выполнение продолжить не могу, не могу увидеть реализацию кроме как с БД по указанному задание, проверку на наличие только цыфр в колличестве не делал
# потому что она есть в предыдущем задании 

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.



# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.



# 7. Реализовать проект «Операции с комплексными числами». 
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
#  Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

# не знаю что такое комплексные числа, в математике плохо понимаю