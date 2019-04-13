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
