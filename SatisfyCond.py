#Display numbers from a list using loop.
numbers = [12, 75, 150, 180, 145, 525, 50]
for x in (numbers):
  if x % 5 == 0:
    if x > 500:
      break
    elif x > 150:
      continue
    else:
      print(x)