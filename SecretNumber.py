#create a program that guesses a secret number.
def guess_secret_number():
  low = 0
  high = 100

  print("Please think of a number between 0 and 100!")

  while True:
    guess = (low + high) // 2
    print(f"Is your secret number {guess}?")
    response = input(
      "Enter 'h' if the guess is too high, 'l' if it's too low, or 'c' if I guessed correctly: "
    ).lower()

    if response == 'c':
      print(f"Game over. Your secret number was: {guess}")
      break
    elif response == 'h':
      high = guess
    elif response == 'l':
      low = guess
    else:
      print(
        "Sorry, I did not understand your input. Please enter 'h', 'l', or 'c'."
      )