n=0
while(n<10):
    a=input("do u want to play the game, y/n\n")
    if (a=="y"):
        p1=input("player1,choose rock,paper or scissor")
        p2=input("player2,choose rock,paper or scissor")

        if (p1==p2):
            print("Its a tie")
        elif(p1=="rock") and (p2=="paper"):
            print("p2 wins")
        elif(p1=="paper") and (p2=="scissor"):
            print("p2 wins")
        elif(p1=="scissor") and (p2=="rock"):
            print("p2 wins")
        elif(p1=="paper") and (p2=="rock"):
            print("p1 wins")
        elif(p1=="scissor") and (p2=="paper"):
            print("p1 wins")
        elif(p1=="rock") and (p2=="scissor"):
            print("p1 wins")
        else:
            print("invalid input")

    else:
        break



