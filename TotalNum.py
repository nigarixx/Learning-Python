#Count the total number of digits in a number
usr_input = int(input("Enter number: "))
counter = 0

while usr_input > 0:
  usr_input = usr_input // 10
  counter = counter + 1
print(counter)