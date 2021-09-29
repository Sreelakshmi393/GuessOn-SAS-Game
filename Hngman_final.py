import random 
def hangman() :
     
    with open('wordlist.txt', 'r') as f:
        words = f.readlines()

    word = random.choice(words)[:-1]
    turns = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')

    while len(word) > 0:
        main_word=""
        for letter in word:
            if letter in guessmade:
               main_word= main_word + letter
            else:
                main_word = main_word + "_ "
        if main_word ==word:
            print(main_word)
            print("You Won!!")
            break
        
        print("Guess the words ",main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Enter a valid entry")
            guess= input()

        if guess not in word:
            turns= turns-1

            if turns==9:
                 print("9 turns left!!")
                 print("-------------------")
               
            if turns==8:
                print("8 turns left!!")
                print("-------------------")
                print("        O          ")
            if turns==7:
                print("7 turns left!!")
                print("-------------------")
                print("        O          ")
                print("        |          ")
            if turns==6:
                print("6 turns left!!")
                print("-------------------")
                print("        O          ")
                print("        |          ")
                print("       /           ")
            if turns==5:
                print("5 turns left!!")
                print("-------------------")
                print("        O          ")
                print("        |            ")
                print("       / \          ")
            if turns==4:
                print("4 turns left!!")
                print("-------------------")
                print("       \O          ")
                print("        |            ")
                print("       / \          ")
            if turns==3:
                print("3 turns left!!")
                print("-------------------")
                print("       \O/          ")
                print("        |            ")
                print("       / \          ")
            if turns==2:
                print("2 turns left!!")
                print("-------------------")
                print("       \O/ |          ")
                print("        |            ")
            
                print("       / \          ")
            if turns==1:
                print("1 turn left!!")
                print("-------------------")
                print("       \O/_|          ")
                print("        |            ")
                print("       / \          ")
            if turns==0:
                print("You Lose!!")
                print("Oops, The Hangman Game is over")
                print("The correct word was",word)
                print("------------------------")
                print("          O_|          ")
                print("         /|\            ")
                print("         / \          ")
                break
                                
name=input("PLEASE ENTER YOUR NAME")
print("Welcome",name ,"!!")
print("---------------------------")
print(name,",Try to guess the word in less than 10 attempts")
hangman()
