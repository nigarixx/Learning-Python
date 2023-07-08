#Calculate the Factorial of a Number
def calculate_factorial(number):
  if number == 0:
    return 1
  result = number
  for x in range(number, 1, -1):
    result = result * (x - 1)
  return result

#Example
print(calculate_factorial(5))