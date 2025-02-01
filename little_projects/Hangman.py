import random
from wordslist import words



def word_to_guess(tuple):
    word_to_guess = random.choice(tuple)
    w = []
    for char in word_to_guess:
        w.append(char)
    return w, len(w)


def add_new_word_func(word,sword,letter):
    if letter in sword:
        print(f"The letter {letter} is already guessed ")
    else:
        for le in range(len(word)):
            if word[le] == letter:
                sword[le] = letter


def see_advancement(sword):
    word = ""
    for le in range(len(sword)):
        print(sword[le], end="")
        word += sword[le]
    print()
    return word

def enter_letter():
    letter1 = input('guess a letter in the secret name ')
    while len(letter1) != 1 or not letter1.isalpha():
        print("You must enter a letter")
        print()
        letter1 = input('guess a letter in the secret name ')
    return letter1.casefold()


def main():
    word, sword = word_to_guess(words)
    sword *= ["_"]
    error = 0
    see_advancement(sword)
    while word != sword:
        letter = enter_letter()
        if letter in word:
            add_new_word_func(word,sword,letter)
            see_advancement(sword)
        else:
            error+=1
            print(f"No {letter} in the word")
            print(f"{5-error} try remaining")
            see_advancement(sword)
            if error == 5:
                print(f"The word was {see_advancement(word)}")
                new_game = input("You lose, try again (type y to continue) : ")
                if new_game.casefold() == "y":
                    main()
                else:
                    return None

    print(f"Vous avez trouvé, le mot est {see_advancement(sword)} !")
    new_game = input("Do you want to play again (type y to continue) : ")
    if new_game.casefold() == "y":
        main()
    else:
        return None


main()
