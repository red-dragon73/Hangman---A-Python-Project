import sample_words
import random


# greet user
def greet_user():
    user_name = input("Welcome, what is your name?")
    print("Hello,", user_name, "Good Luck!")
    print("Figure out this word:")


def select_word():
    # rand_number = random.randint(1,50)
    # word = sample_words.word_list[rand_number]
    # print(word)
    word = random.choice(sample_words.word_list)  # import the word from another file
    return word.upper()


def play_game(word):
    word_length = len(word)
    status = '_' * len(word)
    guessed=False  # set guess to false because player hasn't guessed yet
    guessed_words = []
    guessed_letters = []
    tries = 6  # the hangman counts 6 body parts
    print(show_hangman(tries))
    print(status)

    while not guessed and tries>0:
        print("no. of letters =", word_length)
        guess = input("Guess a letter or the word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:  # if player has already guessed it
                print("You have already guessed this word.")
            elif guess not in word:  # if player guessed wrong letter
                print("Wrong guess, try again.")
                tries -= 1
                guessed_letters.append(guess)
            else:                   # if player guessed a letter correctly
                print("Nice! ",guess," is there.")
                guessed_letters.append(guess)
                # to update the word_completion, for that we need to convert the word to list to update it for each letter occurrence.
                word_as_list = list(status)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                status = "".join(word_as_list)
                if "_" not in status:
                    guessed=True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed this.")
            elif guess!=word:
                print("Not the right word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                print("Congrats, that is correct.")
                guessed=True
        else:
            print("Invalid input, learn how to play the game.")
        print(show_hangman(tries))
        print(status, "\n")

    if guessed:
        print("Congrats, that's the right word.")
    else:
        print("Better luck next time. The word was ", word)


def show_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


if __name__ == "__main__":
    #greet_user()
    gen_word = select_word()  # get a random word  from the list of word
    # print(gen_word)
    play_game(gen_word)