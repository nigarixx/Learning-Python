#Print the half-pyramid pattern
row = int(input('Enter number: '))
for x in range(1, row + 1):
  for y in range(1, x + 1):
    print(x, end=" ")
  print()