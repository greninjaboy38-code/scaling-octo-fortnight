n = int(input("Enter a number: "))

print("Odd numbers:", [i for i in range(n) if i % 2 != 0])
print("Even numbers:", [i for i in range(n) if i % 2 == 0])

fruits = ["apple", "banana", "mango", "orange"]
print("Updated fruits:", [fruit.capitalize() for fruit in fruits])
