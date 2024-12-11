#Nested if Statements
number = 15

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number or zero")
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
