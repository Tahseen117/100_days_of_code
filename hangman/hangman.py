import random
import  os
from ascii_art import art , hangman
from wordlist import word_list


word = random.choice(word_list)
lost=0
os.system('cls')
print(hangman)

display = []
for position in range(len(word)):
    display += "_"
print(art[0])
print("Number of letters in the chosen word: {}".format(display))

p=0
while "_" in display:
    guess = input ("Guess the letter :")
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = word[i]
    
    
    os.system('cls')

    print(hangman)
    if guess not in word:
        if p == len(art)-2:
            lost=1
            print("You lose")
            print(art[p+1])
            print (word)
            break
        print(art[p+1])
        p+=1
    else:
        print(art[p])
    
    print (display)

if lost != 1:
    print("YOU WON !!")

