

def add_new_word_func(word,sword,letter):
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
    while len(letter1) != 1:
        print("You must enter a letter")
        print()
        letter1 = input('guess a letter in the secret name ')
    return letter1.casefold()


def main(word,sword=["_"]*5):
    while word != sword:
        letter = enter_letter()
        if letter in word and letter not in sword:
            print(f"There is a {letter} in the word")
            add_new_word_func(word,sword,letter)
            see_advancement(sword)
        else:
            print(f"No {letter} in the word")
            see_advancement(sword)

    return print(f"Vous avez trouvé, le mot est {see_advancement(sword)} !")

main(["m","a","n","g","o"])