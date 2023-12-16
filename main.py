import random

max_range = input("Type a number: ")

if max_range.isdigit():
  max_range = int(max_range)

  if max_range <= 0:
    print("Please type a number greater than 0")
    quit()
else:
  print("Please type another number")
  quit()

r = random.randint(0, max_range)
guesses = 0

while True:
  guesses += 1
  who_guessin = input("Make a guess: ")
  if who_guessin.isdigit():
    who_guessin = int(who_guessin)

  else:
    print("Please type another number")
    continue

  if who_guessin == r:
    print("You got it!")
    break
  elif who_guessin > r:
    print("You were above the number average")
  else:
    print("You were below the number average")

print("You scored it in", guesses, "guesses")


    
  

  