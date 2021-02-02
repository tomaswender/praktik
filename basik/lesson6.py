



#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    def __init__(self):
        self.__true_color = '1'
        self.color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        if self.__true_color in '1':   #красный
            for i in range(0, 7):
                print(self.color[0])
                i +=1
                if i >5:
                    print(self.color[1])  #мигающий
                self.__true_color = '12'
        if self.__true_color in '12':  # зеленый
            for i in range(0,3):
                print(self.color[2])
                i +=1
            self.__true_color = '3'
        if self.__true_color in '3':  
            for i in range(0,2):
                print(self.color[1])
            self.__true_color = '1'
            print(self.color[0])
        else:
            print('Светофор не работает')

#a= TrafficLight()
#a.running()

#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. 
# Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        a = (self._length*self._width*25*5)/1000
        print(a, 'т')

#a = Road(length=20, width=5000)
#print(a.massa())


#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        print (self.income['wage']+self.income['bonus'])



income = {
    "wage": 15000, 
    "bonus": 1500
}
#a = Position(name='Ivan', surname='Petrov', position='CEO', income=income)
#a.get_full_name()
#a.get_total_income()



#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        if self.speed != 0:
            print(f'Машина {self.name} поехала')
    def stop(self):
        if self.speed == 0:
            print(f'Машина {self.name} остановилась')
    def turn(self):
        pass
    def show_speed(self):
        print(f'Скорость машины {self.name}: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed >60:
            print('Вы привысили скорость')
        else:
            print(f'Скорость машины {self.name}: {self.speed}')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed >40:
            print('Вы привысили скорость')
        else:
            print(f'Скорость машины {self.name}: {self.speed}')
class PoliceCar(Car):
    def pocice(self):
        if self.is_police != True:
            print(f'Машина {self.name} не является полицейской, значит она в угоне')
        else:
            print(f'Включи сирену')

tc = TownCar(15, 'green', 'mini') 
sc = SportCar(0, 'blue', 'mg')
wc = WorkCar(60, 'red', 'max')
pc = PoliceCar(150, 'black', 'poli', True)

#tc.go()


#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Запуск тонкой отрисовки')
class Pencil(Stationery):
    def draw(self):
        print('Запуск цветной отрисовки')
class Handle(Stationery):
    def draw(self):
        print('Запуск толстой отрисовки')

p = Pen('parker')
penc = Pencil('pirker')
h = Handle('pufler')

#p.draw()