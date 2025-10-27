a = [12, False, "Green", 3394.22]

print(a)
print(a[3]) # with the help of key value pair we can print any value in lists and it starts numbers from 0
print(a[1:]) # This will print from 1 index to last
print(a[:]) # This is as equal as print(a)

a[3] = 3.2
# Since it is mutable so we can modify the data
print(a)

a.pop()
# This removes last element of the list
print(a)

a.append(34)
# This adds the value
print(a)