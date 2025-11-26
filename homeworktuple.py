def tuple_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage:
t = (2, 3, 4, 5)
result = tuple_product(t)
print("Product of tuple elements:", result)
