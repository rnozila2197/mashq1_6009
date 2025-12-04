# 1
number = 1
while number < 5:
    print(f"number = {number}")
    number += 1
print(number)

# 2
number = 1
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}")
print("ishladi")

# 3
number = 10
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}")
print("ishladi")

# 4
message = "Hello"
for c in message:
    print(c)

# 5
for i in range(4, 10):
    print(i, end=" ")

# 6
for i in range(0, 10, 2):
    print(i, end=" ")

# 7
message = "Hello"
for i in message:
    print(i)
else:
    print(f"Ohirgi simvol: {i}")

# 8
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

# 9
for i1 in "ab":
    for i2 in "ba":
        print(f"{i1}{i2}")

# 10
number = 0
while number < 5:
    number += 1
    if number == 3:
        break
    print(f"number = {number}")






