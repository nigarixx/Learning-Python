#Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.
result = (15 + 30) / 2
print("The answer is:", result)

#Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.
num1 = 5
num2 = 30

sum = num2 + num1
print("Sum is:", sum)

sub = num2 - num1
print("Sub is:", sub)

mult = num1 * num2
print("Mult is:", mult)

div = num1 / num2
print("Div is:", div)

rem = num1 % num2
print("Rem is:", rem)

#Create a variable called name and store your name in it as a string.
name = "Nigar"

#Create three variables in one line and assign each one a different food item.
fruit, protein, fat = "apple", "meat", "butter"
print(fruit, protein, fat)

#Print out "Hello" ten times using arithmetic operators.
print("Hello " * 10)

#Set your name and age variables in one line with multiple assignment
name, age = "Nigar", 24
print(name, age)

#Create two strings and then create a third variable combining both of the two original strings.
str1 = "Hello"
str2 = "World"
strfull = str1 + " " + str2
print("Combined string:", strfull)

#Create a string and print the fourth letter of the word & Create a string and print the letters from index 0 to 5 & Create a variable and print all the letters from the first index until the end.
name = "Nigar"
print("4th letter:", name[3])
print("Full index of name:", name[0:5])
print("1st index until the end:", name[:])

#Create a list of names and print the second item.
names_list = ['Nigar', 'Shirin', 'Gulshan', 'Azad', 'Camal']
print("Second name:", names_list[1])

#Create a list of sports and then replace the second item with another sport.
sports_list = ['baseball', 'basketball', 'football', 'swimming']
sports_list[1] = 'tennis'
print('Replaced second item:', sports_list)

#Create a list containing numbers and delete the fifth number from the array.
numbers_list = ['1', '2', '3', '4', '5', '6']
del numbers_list[4]
print('Deleted 5th item:', numbers_list)

#Create two lists of numbers and merge them.
num_list1 = ['1', '2', '3', '4', '5', '6']
num_list2 = ['7', '8', '9', '10', '11', '12']
print('Merged list:', num_list1 + num_list2)

#Create a list of numbers and find the length, minimum, and maximum.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(max(number_list))
print(min(number_list))
print(len(number_list))

#Create a dictionary of students and scores and print out a student’s score.
students_scores = {'Dan': 40, 'Elvis': 20, 'Adam': 32}
print('Dan score is :', students_scores['Dan'])

#Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
people = {'Dan': 12, 'Elvis': 13, 'Adam': 14, 'Elie': 15, 'Isma': 16}
del people['Elvis']
print('People list after deleting 2nd item:' ,people)

#Create a dictionary of names and ages and then print out all the keys and values
people1 = {'Dan': 12, 'Elvis': 13, 'Adam': 14, 'Elie': 15, 'Isma': 16}
print('Keys:', list(people.keys()))
print('Values:', list(people.values()))

#Create a tuple of your favorite movies & Create a tuple and print all the items from the first to third index.
movies = ('Me Before You', 'Titanic', 'Blabla')
print('Fav movies:', movies)
print('From 1st - 3rd index:', movies[0:3])