print("Let's play guess the number!")
print()
print("Pick a number between 1 and 100 and see when you can guess it right!")
print()
print("Let's begin!")
correct_number = 57
attempt = 1
while True:
  user_guess = int(input("Pick a number between 1 and 100: "))
  if user_guess < 0:
    print("Nope! It's not a negative number!")
    exit()
  if user_guess < correct_number:
    print("Nope, too low!")
    attempt += 1
  elif user_guess > correct_number:
    print("Too high! Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You WIN! ")
    break 
  else:
    print("That is not a number. ")
print("It took you", attempt, "attempt(s) to get the correct answer.")