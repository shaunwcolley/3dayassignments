num = int(input("Please provide a number to do the factorial for: "))

result = 1
while num > 0:
    result = result * num
    num = num - 1
print(result)
