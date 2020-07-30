import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
com_lang, temp = ['python', 'java', 'kotlin', 'javascript'], set()
rand_com_lang = random.choice(com_lang)
string = "-" * len(rand_com_lang)
count = 0

print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
        while True:
            print("\n" + string)
            letter = input("Input a letter: ")
            if 0 <= len(letter) > 1:
                print("You should input a single letter")
                temp.add(letter)
            elif letter not in alphabet:
                print("It is not an ASCII lowercase letter")
                temp.add(letter)
            elif letter in temp:  # or letter in string
                print("You already typed this letter")
            elif letter not in rand_com_lang:
                print("No such letter in the word")
                count += 1
                temp.add(letter)
            elif letter in rand_com_lang:
                temp.add(letter)
                for i in range(len(rand_com_lang)):
                    if letter == rand_com_lang[i]:
                        string = string[:i] + letter + string[i + 1:]
            if string == rand_com_lang:
                # print("\n" + string)
                print("You guessed the word!")
                print("You survived!\n")
                break
            elif count == 8:
                print("You are hanged!\n")
                break
    else:
        break
