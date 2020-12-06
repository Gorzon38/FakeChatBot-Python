from random import *
from pathlib import Path
import time,os

clear = lambda: os.system('cls')

answ_yes=['oui','yes','ui','ya'];
answ_no=['non','no','nope','nein'];

def mastermind():
    def code():
        code =''
        for i in range(4):
            code+=str(randint(1,9))
        return code
    
    def getInput():
        while True:
            userInput = input('Entrez 4 chiffre:\n>>')
            if len(userInput) !=4:
                print("\n<<<|ENTREZ UN CODE A 4 CHIFFRE|>>>\n")
            else: 
                return userInput

    def isCode(code, U_input,G_number,wp_nbr):
        for i in code:
            for k in U_input:
                print(k,i)
                if k in code:
                    if k==i:
                        G_number+=1
                        print('gn',k,i)
                    else:
                        wp_nbr+=1
                        print("wp",k,i)
        print(G_number,'     ',wp_nbr)
        return G_number, wp_nbr

    code = str(code())

    while True:
        goodNumber = 0
        wrongPlaceNumber = 0

        userInput = getInput()
        goodNumber,wrongPlaceNumber = isCode(code,userInput,goodNumber,wrongPlaceNumber)

        if goodNumber==4:
            print('Bravo, tu as trouver les 4 chiffre !:)')
            break

        print(str(goodNumber)+' chiffre sont à la bonne place.', str(wrongPlaceNumber) + ' sont a la mauvaise place')
            
mastermind()
