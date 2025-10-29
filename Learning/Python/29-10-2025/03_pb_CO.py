# Write a python program where we take input from user and solve using arithmetic operator

class solv:
    def __init__(self):
        pass

    def add(self, value1, value2):
        return value1 + value2
    
    def sub(self, value1, value2):
        return value1 - value2
    
    def mult(self, value1, value2):
        return value1 * value2
    
    def div(self, value1, value2):
        return int(value1 / value2)
    
val1 = int(input("Enter value 1: "))
val2 = int(input("Enter value 2: "))

s = solv()
soln = s.add(val1, val2)
print("Addition of 2 values: ",soln)

