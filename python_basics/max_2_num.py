def max(a, b):
    if a > b:
        c = a
    else:
        c = b
    return c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = max(a, b)
print("The maximum number is:", result)
