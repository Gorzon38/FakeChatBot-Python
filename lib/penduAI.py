from random import *
from pathlib import Path
import time,os

clear = lambda: os.system('cls')

answ_yes = ['oui','yes','ui','ya']
answ_no = ['non','no','nope','nein']



def penduAI():
    hangmanPics = ['''
        +---+
            |
            |
            |
           ===''',''' 
        +---+
        0   |
            |
            |
           ===''','''
        +---+
        0   |
        |   |
            |
           ===''','''
        +---+
        0   |
       /|   |
            |
           ===''','''
        +---+
        0   |
       /|\  |
            |
           ===''','''
        +---+
        0   |
       /|\  |
       /    |
           ===''','''
        +---+
        0   |
       /|\  |
       / \  |
           ===''']
   
    missedLetter = ''
    correctLetter = ''
    word = ''
    
    def data(UserSecretWord):
        pathSecretWord = './data/data.txt'
        secretWordFile = open(pathSecretWord).read().split()

        if UserSecretWord not in secretWordFile:
            secretWordWrite = open(pathSecretWord, 'a')
            secretWordWrite.write(' '+UserSecretWord)
            secretWordWrite.close()

    def board(getMissedLetter, getCorrectLetter, secretWord):
        print(hangmanPics[len(missedLetter)])
        print()

        blanks ='_' * len(secretWord)

        for i in range(len(secretWord)):
            if secretWord[i] in correctLetter:
                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
        
        for letter in blanks:
            print(letter, end=' ')
        print()

        print('Mauvaise Lettre:', end=' ')
        for letter in missedLetter:
            print(letter, end=' ')
        print('\n\n')

    def getRandomLetter(alreadyGuess, getCorrectLetter, secretWord):
        start = 1
        if len(getCorrectLetter) >= 1:
            start = 2
        start_2 = 0
        while start == 1:
            while start_2 == 0:
                take_time = 0
                letterChoice = 'a e i o u'.split()
                letterChoose = randint(0, len(letterChoice) - 1)
                if take_time == 5:
                    start_2 == 1
                elif letterChoice[letterChoose] in alreadyGuess:
                    take_time += 1
                    continue
                else:
                    return letterChoice[letterChoose]
            while start_2 == 1:
                letterChoice = 'z r t y p m l k j h g f d s q w x c v b n'.split()
                letterChoose = randint(0,len(letterChoice)-1)
                if letterChoice[letterChoose] in alreadyGuess:
                    continue
                else:
                    return letterChoice[letterChoose]
        
        while start == 2:
            #pathSecretWord = './data/data.txt'
            secretWordRead = open(r'C:\Users\utilisateur\Documents\PYTHON\AI\lib\data\data.txt').read().split()
            word = getCorrectLetter
            Index_list = ''
            for i in range(len(secretWordRead)):
                if len(UserSecretWord) == len(secretWordRead[i]):
                    test = secretWordRead[i]
                    for k in range(len(test)):
                        if test[k] == secretWord[k]:
                            print(test[k],'           ', secretWord[k])
                #if word in secretWordRead[i]:        
                            #print(str(i) + '           ' + secretWordRead[i])
                            break
                        print('for k')
                    Index_list = Index_list + ' ' + secretWordRead[i]
            start = 3
        print('break')
        while start == 3:
            #Index_list = Index_list.split()
            print(Index_list)
            len_list = len(Index_list.split())
            if len_list == 1:
                letter = Index_list[1]
                letterChoice = randint(0, len(letter) - 1)
                print(letter[letterChoice])
                if letter[letterChoice] in alreadyGuess:
                    continue
                else:
                    return letter[letterChoice]

            elif len_list == 0:
                while start_2 == 1:
                    letterChoice = 'a z e r t y u i o p m l k j h g f d s q w x c v b n'.split()
                    letterChoose = randint(0,len(letterChoice)-1)
                    if letterChoice[letterChoose] in alreadyGuess:
                        continue
                    else:
                        return letterChoice[letterChoose]
            break
        

    UserSecretWord = input("Mot Secret ?\n>>").lower()

    game = 1
    while game == 1:
        clear()
        board(missedLetter, correctLetter, UserSecretWord)

        guess = getRandomLetter(missedLetter + correctLetter, correctLetter, UserSecretWord)

        validation = input('Est-ce que ton mot comprend cette lettre : '+ guess +' ?\n>>').lower()
        ask = 1

        while ask == 1:
            if validation in answ_yes:

                correctLetter = correctLetter + guess 
                foundAllLetter = True

                for i in range(len(UserSecretWord)):
                    if UserSecretWord[i] not in correctLetter:
                        foundAllLetter= False
                    
                if foundAllLetter:
                    print('Ouai ! J\'ai trouvé toute les lettres. :D')
                    print('Le mot secret étais '+UserSecretWord)
                    data(UserSecretWord)
                    
                ask = 2
                
            elif validation in answ_no:

                missedLetter = missedLetter + guess

                if len(missedLetter) == len(hangmanPics)-1:
                    clear()
                    board(missedLetter, correctLetter, UserSecretWord)
                    print('Mince, j\'ai pas trouver. :/')
                    data(UserSecretWord)
                    game = 2
                ask = 2
            else:
                continue

penduAI()
