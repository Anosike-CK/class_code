import random

def registerUser(reg_username, reg_password):

    # reg_username = input('please enter your username : ')
    # reg_password = input('please enter your password : ')
    # password_confirm = input('please re-enter password to confirm : ')

    # if password_confirm != reg_password:
    #     password_confirm = input('please re-nter password confirmation :')

    # else:
    #     return (reg_username, reg_password)
    pass

def login(username, password):

    pass

def openWordsFile(filename):

    file = open(filename, 'r')
    for words in file:

        words = words.split(' ')

    return words


def getRandomWord(wordlist):
    
    return random.choice(wordlist)

def display(guessed, secretword):

    guess_space = '_' * len(secretword)

    for i in range (len(secretword)):

        if secretword[i] in guessed:

            guess_space = guess_space[:i] + secretword[i] + guess_space[i+1:]
        
    for letters in guess_space:

        print(letters, end=' ')
        
    print()

def getUserGuess(alreadyGuessed):

    while True:

        guess = input('Please enter a guess')

        if len(guess) != 1:

            print('please enter a letter')

        elif guess in alreadyGuessed:

            print('you have already guessed this letter')

        elif guess not in 'abcdefghijklmnopqrdstuvwxyz':

            print('please enter a letter in the 36 alphabets')
    
        else:
            return guess


wordlist = openWordsFile('twist.txt')
secretword = getRandomWord(wordlist)
guessed = ''
no_of_trials = 0

while True:

    no_of_trials += 1
    display(guessed, secretword)
    guess = getUserGuess(guessed)

    if guess in secretword:

        guessed = guessed + guess
    
        for i in range(len(secretword)):

            foundword = True

            if secretword[i] not  in guessed:

                foundword = False

                break

        if foundword == True:

            display(guessed, secretword)
            print(f'the secret word is {secretword}, you won!')
            break
    
    else:

        if no_of_trials == 10:

            display(guessed,secretword)
            print(f'you have ran out of guesses, the word is {secretword}')






