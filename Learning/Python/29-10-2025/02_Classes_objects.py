# class sub:
#     sub_name = "English"

# s1 = sub()
# print(s1) # This will print an object and the memory location where the subject(english) has been stored
# print(s1.sub_name) # This will print the value of sub_name

''' This is the basic syntax of classes and object where we have created the class and initialize a variable with value
* Here we have to define an inbuilt function or we call it as object which is derived as:

    def __init__(self):
if we dont mention it then it takes default as like this function mentioned above
'''

class sub:
    def __init__(self,name):
        self.name = name
    

s1 = sub("Mathematics")
print(s1.name) # This will print the value which we give it to print

s2 = sub("Social Science")
print(s2.name)

