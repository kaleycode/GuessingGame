print("Let's play guess the number!")
print()
print("Guess a number between 1 and 100, and let's see when you get it right!")
print()

correctNumber = 66
attempt = 1
while True:
  userguess=int(input("Type in a number between 1 and 100: "))
  if userguess < 0:
    print("Nope! It's not a negative number. Try again!")
    attempt +=1
    continue
  elif userguess < correctNumber:
    print("Nope! That's too low, try again!")
    attempt +=1
    continue
  elif userguess > correctNumber:
    print("Nope, too high!")
    attempt +=1
    continue
  elif userguess == correctNumber:
    print("YOU WIN!")
    print("It took you", attempt, "attempt(s) to get the correct answer")
    break
  else:
    print("Pick a number between 1 and 100. ")
    attempt +=1
    continue
  
