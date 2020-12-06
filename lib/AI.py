#UTF-8
from random import randint, choice
import time, os
from datetime import datetime

#ignorer les pb de modules souligner en jaune
from jsonpy import cjson, interact, answ, feel, emote

from AIplay import rpsAI, rpsAIRage, guessNumber, TicTacToe, pendu
from draw import drawAI

clear = lambda: os.system('cls'); #func clear


def emotion(userInput):
    if    userInput in feel('bad'):    return f"C'est pas cool ça. {cjson('emote','bad')}";
    elif  userInput in feel('good'):   return f"Cool. {cjson('emote','good')}";
    elif  userInput in feel('sad'):    return f"Ah non pleure pas. {cjson('emote','sad')}";
    elif  userInput in feel('super'):  return f"{cjson('feel','super').capitalize()} ! {cjson('emote','super')}";
    else: print("rien à dire ? Pas grave..")


clear()
print(f"Salut {os.getlogin()}, je suis Ordis, une IA (Inteligence Artificiel) ! :D\n")
time.sleep(1);
print("Alors vas y parle, enfin écrit. :)\n'help' pour voir les commandes.\n")



while True:
    
    userInput=input(">").lower();
    if userInput in interact('feel'):
        if randint(1,3)==1:
            print(f"\n{cjson('feel','super').capitalize()} et toi ? {cjson('emote','good')}\n");    userInput=input(">>").lower();  print(emotion(userInput))
        elif randint(1,3)==2:
            print(f"\n{cjson('feel','bof').capitalize()} Et toi ? {cjson('emote','bof')}\n");       userInput=input(">>").lower();  print(emotion(userInput))
        else:
            print(f"\n{cjson('feel','sad').capitalize()}. Et toi ? {cjson('emote','sad')}\n");      userInput=input(">>").lower();  print(emotion(userInput))     
            if userInput in interact('why'):
                if randint(1,2)==1:    print(f"Tes messages m'ennuie. {cjson('emote','wink')}")
                else:   print(f"Aucune idée je ne ressent pas d'émotion. {cjson('emote','wink')}")
            else:   print(emotion(userInput))


    elif userInput in interact('time'):
        timeDate=datetime.now();
        timeNow=timeDate.strftime("%d/%m/%Y");
        dateNow=timeDate.strftime("%H:%M:%S");
        print("On est le :",dateNow," et il est :",timeNow);
        

    
    elif userInput=='': print(f"Rien à dire ? {cjson('emote','bof')}\n")
    
    elif userInput in interact('play'):
        userInput=input("\nA quel jeux veut-tu jouer ? 'rps', 'guess my number', 'morpion', 'pendu' ?\n>>").lower();
        if userInput not in ('guess my number' or "rps" or "morpion" or "pendu"):
            print("Aucun ? Dommage..")
        else:
            userInput=input(f"\nTu veux jouer à {userInput} ? {cjson('emote','good')}\n>>").lower();
            if userInput in answ('yes'):
                if userInput=="guess my number":    guessNumber()
                elif userInput=="rps":              rpsAI()
                elif userInput=="morpion":          TicTacToe()
                elif userInput=="pendu":            pendu()
            else:
                print('\nDommage une prochaine fois peut-être..');


    elif userInput in answ('no'):
        print(f"Ah! Ah! Pourtant tu viens de le faire ! {cjson('emote','wink')}");
        time.sleep(1);
        userInput = input(f"Tu te crois plus malin que moi ? {cjson('emote','good')}\n").lower();
        if userInput in answ('yes'):
            print("Ah oui ?! Ben on va voir ça toute suite ! Avec un pierre, feuille, scisseaux ! >:D");
            userInput=input("Alors, partant ? >:D\n").lower();
            if userInput in answ('yes'):
                rpsAI();
            elif userInput in answ('no'):
                if randint(1,2)==1:
                    userInput=input(f"Bah alors ! On abandonne déjà ? {cjson('emote','moque')}\n").lower();
                    if userInput in answ('no'):
                        userInput=input(f"bah alors relèvent mon défi ! {cjson('emote','bad')}").lower();
                        if userInput in answ('ok'):
                            print(f"Alors c'est partie et là pas de quartier ! {cjson('emote','moque')}");
                            rpsAIRage();
                        elif userInput in answ('no'):
                            print("Quoi ?!  ? >:(\n");
                            time.sleep(0.75);
                            print(f"si c'est comme ça je pars !! {cjson('emote','bad')}");
                            exit();
                        else: 
                            print(f"Ça ça veut dire oui ! {cjson('emote','moque')}")
                    elif userInput in answ('yes'):
                        print("Comme je te comprend. ^^");
                    else: 
                        print(f"Je prend ça pour un oui. {cjson('emote','moque')}");
                        
                else:
                    print(f"Comme je te comprend, tu sais que tu vas perdre alors tu ne tente pas. {cjson('emote','moque')}");
        elif userInput in answ('no'):
            print(f"C'est bien tu as compris. {cjson('emote','good')}");
        else: 
            print(f"Tu reste sans voix devant mon génie {cjson('emote','good')}");


    elif userInput in interact('bye'):
        if randint(1,2)==1:
            print(f"Au revoir ! Tu va me manquer.. {cjson('emote','sad')}");
            time.sleep(10);
            exit()
        else:
            print(f"\nAu revoir ! {cjson('emote','good')}");
            time.sleep(1)
            print("*Il ma souller celui là !*");
            time.sleep(1)
            print("Oups ! J'ai oublié que je ne pouvais pas penser.");
            time.sleep(1)
            userInput=input("Bon, j'espère au moins qu'il a fermé la console. Au quel cas il ne verra pas ce message.\n").lower();
            if userInput in answ('what'):
                r=randint(1,3);
                if r==1:
                    print(f"Ques-ce-qu.. Je disais que les oiseaux sont magnifique aujourd'hui. {cjson('emote','sweat_no')}\n\n");
                    time.sleep(1);
                    drawAI("bird");
                elif r==2:
                    print("Oh, min.. mince.. je bu..bu..bug..");
                    time.sleep(1);
                    for i in range(25):
                        print(('#'*randint(0,20), ' '*randint(0,10))*20)
                    time.sleep(1);
                    clear();
                    time.sleep(1);
                    print("Oups, tu disais quoi ? :)");
                    time.sleep(2);
                    exit()
                elif r==3:
                    print("Formation...Heuu...Crash..");
                    time.sleep(2);
                    exit();


    elif userInput=="help":
        print('<<<| LES COMMANDES SUIVANTE NE SONT QUE DES EXEMPLE',end='')
        time.sleep(1)
        print(' IL EN EXISTE D\'AUTRE',end='')
        time.sleep(1)
        print(' ET DES MANIERES DIFFERENTES',end='')
        time.sleep(1)
        print(' DE LES ECRIRES |>>>')
        print("\n'ça va'\n\n'game'\n\n'au revoir'");
    
    else:
        print(f"Ce que tu as marqué n'est pas pris en compte dans mon code. {cjson('emote','bof')}\n'help' pour plus d'information");

