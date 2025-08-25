import math
from symbol import return_stmt


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

    def reverse(self, x: int) -> int:
        max = 2 ** 31 - 1
        min = -2 ** 31
        ans = 0
        y = x;
        if y < 0:
            y = -y
        while y > 0:
            ans = ans * 10 + y % 10
            y = y // 10

        if x < 0:
            ans = -ans
        if ans >= max or ans <= min:
            return 0

        return ans

if __name__ == "__main__":
    calculator = Calculator();
    # print(calculator.divide(1,0))
    # print(-2**31)
    print(calculator.reverse(-1563847412))