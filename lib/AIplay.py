from random import *
from pathlib import Path
import time, os

from jsonpy import cjson, answ, interact 

clear = lambda: os.system('cls')

#RPS
def NumberToLetter(computerChoice):
    if computerChoice==1:       return "/rock\n"
    elif computerChoice==2:     return "/paper\n"
    else:                       return "/scissors\n"

barre = '\n'+''.center(28,"=")
win = lambda userChoice, computerChoice:    print(NumberToLetter(computerChoice),barre+'\n','! Utilisateur a gagner !'.rjust(25),barre);

lose = lambda userChoice, computerChoice:   print(NumberToLetter(computerChoice),barre+'\n','! Ordis a gagner !'.rjust(22),barre);

draw = lambda userChoice, computerChoice:   print(NumberToLetter(computerChoice),barre+'\n','! Egaliter !'.rjust(15),barre)


def rpsAI():
    score_p=0;
    score_o=0;
    c=0;
    print("\nSuper ! Mais tu ne gagnera pas ! :D");
    print("Le premier arriver à trois gagne ! :)");
    time.sleep(1)
    while score_o!=3 or score_p!=3:
        if score_o == 3 or score_p ==3:
            break
        computerChoice = randint(1,3);
        print(f"\nSCORE :\n{os.getlogin()} : "+str(score_p)+'\t\tOrdis : '+str(score_o))
        time.sleep(1)
        userChoice=input("\nrock, paper, scissors ?\n\n").lower();
  
        if (userChoice=="rock" and computerChoice==3) or (userChoice=="paper" and computerChoice==1) or (userChoice=="scissors" and computerChoice==2):
            time.sleep(2)
            win(userChoice, computerChoice);
            score_p+=1;
            time.sleep(2)
            clear()

        elif (userChoice=="rock" and computerChoice==2) or (userChoice=="paper" and computerChoice==3) or (userChoice=="scissors" and computerChoice==1):
            time.sleep(2)
            lose(userChoice, computerChoice);
            score_o+=1;
            time.sleep(2)
            clear()

        elif (userChoice=="rock" and computerChoice==1) or (userChoice=="paper" and computerChoice==2) or (userChoice=="scissors" and computerChoice==3):
            time.sleep(2)
            draw(userChoice,computerChoice);
            time.sleep(2)
            clear()
        else:
            if c>=3:    print("Bon ta fini de te foutre de moi >:(\n");
            else:       
                print(NumberToLetter(computerChoice)+"\n\nHey tu aurais pu jouer !\n C'est pas drôle de me faire jouer seul.. :'(\n");  
                c+=1;

    if score_p>score_o:  print("Co..Comment a tu gagner ?.. \n");
    else:                print("Je t'avais dit que je gagnerai ! :D\n"); 





#RPS RAGE
def rpsAIRage():
    def nbr_Tour(userTour, computerTour):
        if userTour < computerTour:     print("Seulement",userTour,"?! Aller hop on va pour",computerTour,"points ! >:)");
        elif userTour==computerTour:    print("Très bien va pour",userTour,".");
        elif userTour > computerTour:   print("Quoi ?!",userTour,"points ?! T'es malades on vas en faire",computerTour,"!");
        return computerTour;

    def dontPlay_Rage(computerChoice):
        if randint(1,2)==1: print(NumberToLetter(computerChoice)+"\n\nWow mais tu me fais quoi là ?\n On est en pleine battaille là pas à prendre le thé !\n");
        else:               print(NumberToLetter(computerChoice)+"\n\nBen quoi ?! Tu abandonne déjà ? >:)")

    score_p=0;
    score_o=0;
    c=0

    print("\nBon, tu connais les règles ?");
    time.sleep(0.5);
    print("Non ?");
    time.sleep(0.5);
    print("Très bien alors.");
    time.sleep(0.5);

    userTour=int(input("On va jusqu'à combien de points ?\n"));
    computerTour=randint(1,20);
    nbrmax_point=nbr_Tour(userTour,computerTour);

    while score_o!=nbrmax_point or score_p!=nbrmax_point:
        computerChoice = randint(1,3);
        print(f"\nSCORE :\n{os.getlogin()} : "+str(score_p)+'\t\tOrdis : '+str(score_o))
        time.sleep(1)
        userChoice=input("\nrock, paper, scissors ?\n");
  
        if (userChoice=="rock" and computerChoice==3) or (userChoice=="paper" and computerChoice==1) or (userChoice=="scissors" and computerChoice==2):
            time.sleep(2)
            win(userChoice, computerChoice);
            score_p+=1;
            time.sleep(2)
            clear()
        elif (userChoice=="rock" and computerChoice==2) or (userChoice=="paper" and computerChoice==3) or (userChoice=="scissors" and computerChoice==1):
            time.sleep(2)
            lose(userChoice, computerChoice);
            score_o+=1;
            time.sleep(2)
            clear()
        elif (userChoice=="rock" and computerChoice==1) or (userChoice=="paper" and computerChoice==2) or (userChoice=="scissors" and computerChoice==3):
            time.sleep(2)
            draw(userChoice,computerChoice);
            time.sleep(2)
            clear()
        else:
            if c<3: print("Mais c'est quoi c'est co****** ?! Tu te fous de moi ?! (ì_í)\n");
            else: 
                dontPlay_Rage()
                c=c+1;
    if score_p>score_o: print("Co..Comment a tu gagner ?.. Tu as triché c'est ça ?!\n");
    else:               print("Bah voilà, je t'avais dit quoi ?! >:)\n");




#GuessNumber
def guessNumber():
    def end(secretNumber,userInput):
        if secretNumber==userInput:
            print("Bien joué ! Tu as trouvé ! Mon nombre secret était bien : " + str(secretNumber) + " :D");
            time.sleep(1.5);
        else:
            print("Dommage.. Mon nombre secret était : "+str(secretNumber)+" :/");
            time.sleep(1);

    def play(nbrMax):
        secretNumber=randint(1,int(nbrMax));
        print(f"\n\nJe pense à un nombre entre 1 et {nbrMax}. ");
        time.sleep(1);
        print("Tu as le droit à 8 chances pour trouver. :)\nC'est partie !\n")

        for i in range (9):
            userInput=int(input(""));
            if secretNumber<userInput:
                print("Mon nombre secret est plus petit");
            elif secretNumber>userInput:
                print("Mon nombre secret est plus grand");
            else:
                break;
        end(secretNumber,userInput);
    
    while True:
        difficulte=input("Niveau de difficulter ? (1, 2)\n");
        if difficulte=="1" or difficulte=="2":
            break;
        else:
            continue;
    if difficulte=="1":
        play(20);
    elif difficulte=="2":
        play(40);





#TIC TAC TOE
def TicTacToe():
    board = [' ' for x in range(10)]

    def insertLetter(letter, pos):  board[pos] = letter

    def spaceIsFree(pos):   return board[pos] == ' '

    def printBoard(board):
        print('     |    |')
        print('   ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3])
        print('     |    |')
        print('----------------')
        print('     |    |')
        print('   ' + board[4] + ' |  ' + board[5] + ' |  ' + board[6])
        print('     |    |')
        print('----------------')
        print('     |    |')
        print('   ' + board[7] + ' |  ' + board[8] + ' |  ' + board[9])
        print('     |    |\n\n')
    
    def isWinner(bo, le):
        return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

    def playerMove():
        run = True;
        while run:
            move = input("\n<<<|SELECTIONNER UNE POSITION (1-9)|>>>\n>>");
            try:
                move = int(move);
                if move > 0 and move < 10:
                    if spaceIsFree(move):
                        run = False;
                        insertLetter('X', move);
                    else:
                        print('\n<<<|CETTE ESPACE EST OCCUPER|>>>');
                else:
                    print('\n<<<|ENTRER UN NOMBRE VALIDE|>>>');
                    time.sleep(2);
            except:
                print('\n<<<|ENTRER UN NOMBRE|>>>');
                time.sleep(2);
            

    def compMove():
        possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0];
        move = 0;

        for let in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = board[:];
                boardCopy[i] = let;
                if isWinner(boardCopy, let):
                    move = i;
                    return move;

        cornersOpen = [];
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i);
            
        if len(cornersOpen) > 0:
            move = selectRandom(cornersOpen);
            return move;

        if 5 in possibleMoves:
            move = 5;
            return move;

        edgesOpen = [];
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i);
            
        if len(edgesOpen) > 0:  move = selectRandom(edgesOpen);
        
        return move;

    def selectRandom(li):
        ln = len(li);
        r = randrange(0,ln);
        return li[r];
    

    def isBoardFull(board):
        if board.count(' ') > 1:    return False
        else:                       return True

    
    print('\nAller jouons au morpions ! :D')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove();
            printBoard(board);
        else:
            print(f"\n{answ('yes').capitalize()} j'ai gagner !! :D");
            break

        if not(isWinner(board, 'X')):
            move = compMove();
            if move == 0:
                print('\n<<<|REMPLI|>>>');
            else:
                insertLetter('O', move);
                printBoard(board);
        else:
            print("\nComment as-tu gagner ?.. Mon génie ne peut être détronner..");
            break

    if isBoardFull(board):
        print("\nMince c'est remplie. Aucun de nous n'as gagner. :/");



#PENDU
def pendu():
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
    
    secretWordRead = open('lib\data\data.txt').read().split()
    secretWordChoose = randint(0,len(secretWordRead) -1)
    secretWord = secretWordRead[secretWordChoose]

    missedLetter =''
    correctLetter =''

    def board(missedLetter, correctLetter, secretWord):
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

        

    def getGuess(alreadyguess):
        while True:
            guess=input('>> ')
            guess=guess.lower()
            if len(guess) != 1:
                print('Entre une seul lettre s\'il te plait.')
            elif guess in alreadyguess:
                print('Tu as déjà choisi cette lettre choisie en une autre.')
            elif guess not in 'azertyuiopmlkjhgfdsqwxcvbn':
                print('Entre une lettre s\'il te plait.')
            else:
                return guess


    gameIsGone=False

    while True:
        clear()
        board(missedLetter, correctLetter, secretWord)

        guess = getGuess(missedLetter + correctLetter)

        if guess in secretWord:
            correctLetter = correctLetter + guess
            foundAllLetter = True

            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetter:
                    foundAllLetter = False
                    break
            if foundAllLetter:
                print("Bravo tu as trouver le mot secret qui était " + secretWord + " ! :D")
                gameIsGone=True
                break
        
        else:
            missedLetter=missedLetter + guess
            if len(missedLetter) ==  len(hangmanPics) -1:
                board(missedLetter, correctLetter, secretWord)
                print('Dommage, tu as échouer, le mot secret était : '+secretWord+' ...')
                gameIsGone=True
                break
