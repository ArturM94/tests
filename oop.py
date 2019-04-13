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
        return f'{self._name} is walking'


class Runner(Person):
    def __init__(self, name, speed):
        super().__init__(name)  # inherits 'name' and 'age' attributes from parent class Person
        self.speed = speed

    def walk(self):  # redefined method
        return f'{self._name} is walking to stadium'

    def run(self):  # own unique method
        return f'{self._name} is running with speed {self.speed} km/h'


class Driver(Person):
    def drive(self):  # own unique method
        return f'{self._name} is driving'


person = Person('Person')
print(person.walk())

runner = Runner('John', 15)
print(runner.walk())  # redefined method with the same name but another implementation (polymorphism)
print(runner.run())

driver = Driver('Andrew')  # driver instance inherits constructor method from Person class
print(driver.walk())  # driver instance inherits walk() method from Person class
print(driver.drive())
