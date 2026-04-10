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