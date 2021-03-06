class Person:
    def __init__(self, name):
        self._name = name  # protected attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def walk(self):
        return f'{self.name} is walking'


class Runner(Person):
    def __init__(self, name, speed):
        super().__init__(name)  # inherits 'name' and 'age' attributes from parent class Person
        self.__speed = speed  # private attribute

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def walk(self):  # redefined method
        return f'{self.name} is walking to stadium'

    def run(self):  # own unique method
        return f'{self.name} is running with speed {self.speed} km/h'


class Driver(Person):
    def drive(self):  # own unique method
        return f'{self.name} is driving'


person = Person('Person')
print(person.walk())

runner = Runner('John', 15)
print(runner.walk())  # redefined method with the same name but another implementation (polymorphism)
print(runner.run())

driver = Driver('Andrew')  # driver instance inherits constructor method from Person class
print(driver.walk())  # driver instance inherits walk() method from Person class
print(driver.drive())
