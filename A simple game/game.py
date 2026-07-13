import random
options=('Rock','Scissors','Paper')
running =True
while running:
    computer=random.choice(options)
    person=None
    while person not in options:
        person=input("Enter your choice (Rock,Paper,Scissors): ").capitalize()
    print( f"Player : {person}")
    print(f"Computer : {computer}")
    if person == computer:
        print("Tie")
    if person =="Rock" and computer =="Scissors":
        print("You Win")
    elif person =="Scissors" and computer =='Rock':
         print("You Win")
    elif person == "Paper" and computer =="Rock":
         print("You Win")
    else:
        print("You Lose")
    if not input('Play again y/n:').lower() == "y":
        running=False




    
   
