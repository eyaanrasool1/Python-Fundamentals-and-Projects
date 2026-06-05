import math

class calculator:
    def __init__(self, n):
        self.n=n

    def square(self):
        print(f"the square of {self.n} is:  {self.n*self.n}")

    def cube(self):
        print(f"the cube of {self.n} is:  {self.n*self.n*self.n}")

    def square_root(self):
        print(f"the square root of {self.n} is: {math.sqrt(self.n)}")
    

# automaticlly call if @staticmethod 

    @staticmethod
    def hello():
        print("Hi here enter the number to perform calculations\n")


# static method call
calculator.hello()

# USER INPUT (this is the key change)
num = int(input("Enter a number: "))

a = calculator(num)

a.square()
a.cube()
a.square_root()