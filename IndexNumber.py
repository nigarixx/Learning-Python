#Write a program to accept a string from the user and display characters that are present at an even index number.
word = 'Nigar'
for w in range(len(word)):
  if w % 2 == 0:
    print(word[w])