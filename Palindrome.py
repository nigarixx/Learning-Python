#Write a program to check if the given number is a palindrome number
def palindrome(number):
  org_number = number
  rev_num = 0

  while number > 0:
    last_digit = number % 10
    rev_num = rev_num * 10 + last_digit
    number = number // 10

  if org_number == rev_num:
    return "Yes. given number is palindrome number"
  else:
    return "No. given number is not palindrome number"

#Example
print(palindrome(6555))