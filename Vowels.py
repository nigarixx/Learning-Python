#Count the number of vowels contained in the string
userinput = input("Write something: ")
s = userinput
vowels = 'aeiou'
count_vowels = 0
for x in s:
  if x in vowels:
    count_vowels += 1

print("Number of vowels: ", count_vowels)