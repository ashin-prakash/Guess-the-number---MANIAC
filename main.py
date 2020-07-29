import random

name = input("Please enter your Beautiful Name >> ")
Age = int(input("Please enter your age >> "))

print("Welcome ", name, "to a small guessing game called the Maniac")

play_game = "yes"

while (play_game == "yes"):
  ans = random.randint(1, 1000)
  try_number = int(input("Please guess a number between 1 and 1000 >> "))
  counter = 1

  while try_number != ans:
    if try_number > ans:
      print("The number is too large...")

    if try_number < ans:
      print("The number is too slow...")

    try_number = int(input("Please guess another number between 1 and 1000 >> "))
    counter = counter + 1

  print("Congratulations ",name, "!" )
  print("You have completed Manic")
  print("You got the answer in ", str(counter) + " times!")
  play_game = input("Wish to play more? (yes/no)")
  if play_game == "no":
    print("Game Over!")