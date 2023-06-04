# ROCK,PAPER,SCISSORS

import random 
l=("ROCK","PAPER","SCISSOR")
while True:
    ccount=0
    ucount=0
    u=int(input('''
Game start....
1 start
2 exit    
    '''))
    if u==1:
        for a in range(1,6):
            ui=int(input('''
1 ROCK            
2 PAPER            
3 SCISSOR             
            '''))
    if ui==1:
        uchoice="ROCK"
    elif ui==2:
        uchoice="PAPER"
    elif ui==3:    
        uchoice="SCISSOR"

    Cchoice=random.choice(l)
    if  Cchoice==uchoice:
        print("computer value",Cchoice)
        print("user value",uchoice)
        print("Game draw")
        ucount=ucount+1
        ccount=ccount+1
    elif (uchoice=="ROCK" and Cchoice=="SCISSOR") or (uchoice
        =="PAPER" and Cchoice=="ROCK") or (uchoice=="SCISSOR"
        and Cchoice=="PAPER"):
          print("you win the round")
          ucount=ucount+1
    else: 
        print("computer value",Cchoice)
        print("user value",uchoice)
        print("computer win")
        ccount=ccount+1 
        