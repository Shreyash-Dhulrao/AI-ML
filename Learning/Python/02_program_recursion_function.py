# Lambda and Recursion Example

sum = lambda a , b: a+b

# print(f"The sum of 10 and 20 is: {sum(10,20)}")
# This is a short way to write the functions

# Recursion Function

# Q. Count how many ways you can climb n stairs if you can take 1 or 2 steps at a time

# Answer:
stairs = int(input("Enter number of stairs: "))

def func_stairs(n):
    # Base value
    if n == 0 or n == 1:
        return 1
    
    return func_stairs(n-1) + func_stairs(n-2)


Total_ways = int(func_stairs(stairs))
print(f"Total ways to climb {stairs} stairs: {Total_ways}")

# Explaination:
'''

Here the values are like this:
if it is 0 or 1 then it returns 1 on both values

Numbers(Stairs)     = 0 1 2 3 4 5 6....
Values(steps)       = 1 1 2 3 5 8 13....

Here we enter how many stairs are available to climb and it gives us the values in steps/ways.
'''
