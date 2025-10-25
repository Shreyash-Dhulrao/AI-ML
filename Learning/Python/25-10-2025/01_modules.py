# Modules and pip

'''
There are 2 types of modules
1. Built-in Modules
2. External Modules
'''

# import math # This is an built in module where we dont have to install it, we can directly using it by just importing it

# print(math.sqrt(900)) # This will print 30
'''
There are many functions in math and we can access it by using math. and name of the function
'''

import requests # Here we have installed the requests using pip

req = requests.get("https://www.google.com")
print(req.text) # This will print whole webpage in text format.
