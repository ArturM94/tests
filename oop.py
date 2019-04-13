class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is walking'


class Runner(Person):
    def __init__(self, name, age, speed):
        super().__init__(name, age)  # inherits 'name' and 'age' attributes from parent class Person
        self.speed = speed

    def walk(self):  # redefined method
        return f'{self.name} is walking to stadium'

    def run(self):  # own unique method
        return f'{self.name} is running with speed {self.speed} km/h'


class Driver(Person):
    def __init__(self, name, age, driver_license):
        super().__init__(name, age)
        self.driver_license = driver_license

    def drive(self):  # own unique method
        return f'{self.name} is driving with driver license №{self.driver_license}'


person = Person('Person', 30)
print(person.walk())

runner = Runner('John', 21, 15)
print(runner.walk())  # redefined method with the same name but another implementation (polymorphism)
print(runner.run())
