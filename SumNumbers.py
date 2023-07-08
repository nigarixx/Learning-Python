#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
for x in range(10):
  prev_num = x - 1
  if prev_num == -1:
    prev_num = 0
  sum = x + prev_num
  print(f"Current Number {x} Previous Number {prev_num} Sum: {sum}")