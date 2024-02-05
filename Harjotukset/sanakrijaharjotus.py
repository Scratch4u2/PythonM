"""
numbers = {"Viivi": "122345"
           , "Joni": "12142356"
           , "Kalle": "124224525"}
numbers["Olga"] = "198246"

print(numbers)

name = input("What is your name?: \n ")
if name in numbers:
    print(f"Hello, {name}´s number is {numbers[name]}")
"""

numbers ={}
for i in range(1,10):
    numbers[i] = i**2
print(numbers)