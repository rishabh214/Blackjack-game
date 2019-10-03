import random
lwin=[]
lbet=[]

while True:
    suit=['spade','diamond','club','heart']
    value=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    d1={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

    deck=[]
    for i in suit:
        for j in value:
            A=j+" of "+i
            deck.append(A)    
    def shuffle():
        random.shuffle(deck)                                # Formation and shuffling of a deck
    shuffle()


    
##EXCEPTION HANDLING concept
    while True:
        try:
            ch=int(input("\n\tHow much money will you bet:"))
            lbet.append(ch)                 # Adding the amount a person bets in each round to a list  
            chi=ch
        except:
            print("\tOOPS! Enter again")
            continue
        else:
            break
        

## OOPS CONCEPT
    class Dealer:                           # Formation of a class named Dealer.It will include functions of dealer
        card1=deck.pop()                                     
        s=0    #class variable

        print("Dealer's 1st card :\n\n\t\t",card1)
        def sum2(self,card):                ##function/method of class Dealer
            c=card.split()
            Dealer.s+=d1[c[0]]              # extracting the value of card using dictionary d1
            if Dealer.s>21 and c[0]=='A':
                Dealer.s-=10
            b= "Dealer's Sum:"+str(Dealer.s)
            return b                        # will return the sum of value of cards held by dealer
        def stand(self):                    ##function/method of class Dealer
            card5=deck.pop()
            print("\n\t\t",card5)
            self.sum2(card5)                #calling sum2 function and using card as argument in sum2 function 
            return Dealer.s
                      

    class Player:                           # Formation of a class named Player.It will include functions of Player
        cardp1=deck.pop()        
        cardp2=deck.pop()
        s=0
        def out(self):
            print("Your cards are :\n\n\t\t",Player.cardp1,"and\n\t\t",Player.cardp2)
        def sum1(self,card):
                c=card.split()
                if c[0]=='A':
                    ace=int(input("\tWhich value of Ace you wish to use : 1 or 11? "))
                    if ace==1:
                        Player.s+=1
                    elif ace==11:
                        Player.s+=d1[c[0]]
                    else:
                        print("\tDon't cheat a intelligent machine \n takin A as 11")
                        Player.s+=d1[c[0]]

                else:
                    Player.s+=d1[c[0]]               
                b="Your sum:"+str(Player.s) 
                return b                     # will return the sum of value of cards held by player
        def hit(self,card):
            print("\n\t\t",card)
            self.sum1(card)                  #calling sum1 function and using card as argument in sum1 function
            return Player.s

        
    D=Dealer()                              ## assigning class calls and calling differen functions
    D.sum2(Dealer.card1)
    P=Player()
    P.out()
    P.sum1(Player.cardp1)
    P.sum1(Player.cardp2)
    def next():
        global chi                          #Declaration of global variable 
        if Dealer.s>Player.s:
            print("\n\t\t\tDEALER WINS!!")
            chi=0*chi                       ## assigning value of prize amount depending on conditions
        elif Dealer.s==Player.s:
            print("\n\t\t\tDRAW GAME ")
        else:
            print("\n\t\t\tYOU WIN!!")
            chi=2*chi                       ## assigning value of prize amount depending on conditions

    q=5
    while q>0:
        
        if Player.s==21:                    # break straightaway if this condition satisfies
                print("\n\n\t\t\tBLACK JACK!!")
                chi=2.5*chi

                break                       
        
        a=input("\n\t\tHIT OR STAND  (H/S)")
        if a=='H' or a=='h':                 # checking for user input for HIT or STAND
            
            card3=deck.pop()
            P.hit(card3)
            if Player.s>21:
                print("\n\t\tYOU BUST!! \n\n \t\tGAME OVER\n")
                chi=0*chi
                break
        elif a=='S' or a=='s':
            print("DEALER PLAYS \n")
            m=D.stand()
            if m==21:
                chi=0
                break         

            else:  
                while m<17:             #setting condition for dealer of drawing cards until his sum is 16 or below it.
                    m=D.stand()

                if m>21:
                    print("\n\t\tDEALER BUSTS\n YOU WIN!!")
                    chi=2*chi
                    break
                elif m==21:
                    print("\n\t\tBLACK JACK!!")
                    chi=0
                    break
                else:
                    next()
                    break
        else:
            break
    
    lwin.append(chi)
    print("Money won in this round:",chi)
    print("total winnings",sum(lwin))     # calculating prixe money for all rounds 

    I=input("DO YOU WANT TO PLAY AGAIN??(Y/N)")
    if I=='N'or I=='n':
        print(" \n THANK YOU FOR PLAYING")
        money=sum(lwin) - sum(lbet)
        if money>0:
            print("\n\n\t\t\t Congratulations you made a profit of Rs:",money)
        else:
            print("\n\n\t\t\t I am so sorry you suffered a loss of Rs:",abs(money))
        break
    






        
