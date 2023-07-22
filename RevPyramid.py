#Print the reverse half pyramid pattern
row = int(input('Enter number: '))
for x in range(row, 0, -1):
  for y in range(x, 0, -1):
    print(y, end=" ")
  print()