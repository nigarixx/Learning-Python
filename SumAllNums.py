#Calculate the sum of all numbers from 1 to a given number
sum = 0
user_input = int(input('Enter number: '))
for u in range(1, user_input + 1):
  sum = sum + u
print('Sum is: ', sum)