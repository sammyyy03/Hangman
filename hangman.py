import random

num_lives = 10


potential_words = ("samantha", "blanket", "pink", "fuzzy", "soft", "beautiful")

word = random.choice(potential_words)


def print_word(word, guesses):
  line = ""
  for letter in word:
    if letter in guesses:
      line = line + letter
    else:
      line += "_"
    line += " "
  print(line)


def did_player_win(word, guesses):
  correct = 0
  for letter in word:
    if letter in guesses:
      correct += 1
  return correct == len(word)


all_guesses = []
print_word(word, all_guesses)
while num_lives > 0:
  guess = input("What is your next guess?\n")
  if not guess in word:
    num_lives = num_lives - 1
    print("wrong guess - please try again")
  all_guesses.append(guess)
  print_word(word, all_guesses)
  if did_player_win(word, all_guesses):
    print("congrats you won!!")
    break

if num_lives == 0:
  print("You have lost the game!")