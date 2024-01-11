

if True:
    print("Holberton")
else:
    print("School")

for i in range(2, 10, 2):
    print(i, end=" ")

if 12 == 48/5 and False:
    print("Holberton")
else:
    print("School")

print("{} Battery street, {}".format(98,"San Francisco"))

for i in range(4):
    print(i, end=" ")

if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
    print("School")


a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton")
    else:
        print("C is fun")
else:
    print("School")


a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun")
else:
    print("School")


a = "Python is cool"
print(a[7:-5])