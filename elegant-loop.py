single_digits = list(range(10))
squares = []
for i in single_digits:
  squares = [i**2 for i in single_digits]
print(squares)

cubes = [i**3 for i in single_digits]
print(cubes)
