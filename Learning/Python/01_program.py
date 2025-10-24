# Functions and its arguments

def args(x , y , c=5): # Default argument in c = 5
    d = ( x + y + c )/3
    # print(d) # This will print the values but we cant save it in any variable
    return d

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"The value of a and b is: {args(a , b)}")
print(f"The value of a and b with new c value is: {args(a , b, 20)}") # Overriding default argument
# args(y = 30, x = 10) # Keyword arguments