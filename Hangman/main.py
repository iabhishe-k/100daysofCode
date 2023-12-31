import random
import hangman_art
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed the letter {guess}")
   
    flag=False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            flag=True


    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word and You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            break

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])