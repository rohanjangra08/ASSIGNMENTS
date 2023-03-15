import random

hang = ["""
H A N G M A N - Guess the edition

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Guess the edition

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Guess the edition

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Guess the edition

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Guess the edition

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Guess the edition

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Guess the edition

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():
    movies = ['sanju', 'main hoon na', 'kabir singh', 'dil to pagal hai', 'kalank', 'kedernath', 'kal ho na ho', 'sultan',
             'tamasha', 'dear zindagi', 'gully boy', 'dilwale', 'hum tum', 'chalte chalte', 'chhichore', 'wake up side', 'barfi',
             'sarkar', 'raid', 'rustom', 'don', 'mardaani', 'krrish', 'sholay', 'baahubali', 'aladin', 'laxmii', 'the kashmir files']

    movie = random.choice(movies)
    return movie


def displayBoard(hang, missedLetters, correctLetters, secretmovie):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretmovie)

    for i in range(len(secretmovie)):  # replace blanks with correctly guessed letters
        if secretmovie[i] in correctLetters:
            blanks = blanks[:i] + secretmovie[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    return input("\nDo you want to play again? ").lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretmovie = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretmovie)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretmovie:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretmovie)):
            if secretmovie[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretmovie + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, secretmovie)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretmovie + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretmovie = getRandomWord()
        else:
            break