print("Let's play guess the number!")
print()
print("Guess a number between 1 and 100, and let's see when you get it right!")
print()

correctNumber = 66
attempt = 1

while True:
  userguess = int(input("Pick a number between 1 and 100. "))
  if userguess < 0:
    print("Nope! It's not a negative number!")
    attempt +=1
    continue
  if userguess < correctNumber:
    print("Nope, too low!")
    attempt += 1
  elif userguess > correctNumber:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif userguess == correctNumber:
    print("It took you", attempt, "attempt(s) to get the correct answer.")
    print("YOU WIN")
    break
  else:
    print("That is not a number you can use.")
