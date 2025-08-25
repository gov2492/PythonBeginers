import math
class Calculator:
    def add(self,a, b):
        return a+b;
    def sub(self, a,b):
        return math.fabs(a-b)
    def multiply(self, a, b):
        return a*b;
    def divide(self,a,b):
        try:
           return a/b
        except ZeroDivisionError as e:
                print(e)
    def square(self,a):
        return a**2;

if __name__ == "__main__":
    calculator = Calculator();
    print(calculator.divide(1,0))
