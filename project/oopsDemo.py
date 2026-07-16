class Calculator:
    number = 100
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("init method")

    def getData(self):
        print("I am calculator")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.number


obj = Calculator(2, 3)
obj.getData()
print(obj.number)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Mohammad", 18)
print(person1.name)
print(person1.age)