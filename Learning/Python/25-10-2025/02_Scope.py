# Scope of variables
'''
There are 2 types of variables
1. Global 
2. Local: The varaible which works inside the function and destorys after returning the function

In the below function we are declaring the value of c outside of the function thats why it is global variable


def funct(a , b):
    return a + b

c = 5 # This is a global variable
print(funct(5, 10))
'''

def greet():
    c = 10 # This is local variable
    return c

''' 
print(c) # This will throw an error saying c is not defined
if we want to use the c outside the function then we have to use the global keyword before declaring the vairable
'''

ca = 5
def greet2():
    global ca
    ca = 20
    return ca

print(greet2()) # From this the value of ca will override on existing value
print(ca)

# Note: The global variable will not work until there is previously value of that variable like in above example we declare the ca first then in function greet2 we have modified it using global keyword