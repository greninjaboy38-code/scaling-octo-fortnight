start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

squares = [n**2 for n in range(start, end + 1)]
even_squares = [s for s in squares if s % 2 == 0]
odd_squares = [s for s in squares if s % 2 != 0]

print("All square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
