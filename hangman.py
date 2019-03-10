#python 2.7
import time
import random


def hangman():
    name = raw_input("What is your name? ")

    print "Hello, {} Time to play hangman!".format(name)
    print ""
    time.sleep(1)
    print "Start guessing..."
    time.sleep(0.5)
    words = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']
    word = random.choice(words)

    guesses = ''
    turns = 5
    while turns > 0:
        failed = 0
        for char in word:
            # see if the character is in the players guess
            if char in guesses:
                print char,
            else:
                # if not found, print a dash
                print "_",
                # and increase the failed counter with one
                failed += 1
        if failed == 0:
            print "\nCongratulations {} , \n your score is {} from 5 \n you can play another game if you want! ".format(name,turns)
            # print 'your score is {} from 5'.format(turns)
            response = raw_input("Do you want to continue[Y/N]")
            if response =='y'or response =='Y':
                hangman()
            elif response =='n'or response =='N':
                break
        print
        guess = raw_input("guess a character:")
        if len(guess) >1:
            print "you must enter one char!"
            continue

        # set the players guess to guesses
        guesses += guess
        if guess not in word:
            # turns counter decreases with 1 (now 4)
            turns -= 1
            # print wrong
            print "Wrong"
            # how many turns are left
            print "You have {} more guesses".format(turns)

            # if the turns are equal to zero
            if turns == 0:
                print "You Loose, you can try again if you want\n  "

                response2 = raw_input("Do you want to continue[Y/N]")
                if response2 == 'y' or response2 == 'Y':
                    hangman()
                elif response2 == 'n' or response2 == 'N':
                    break
            print

hangman()


