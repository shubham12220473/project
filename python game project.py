def random():
        import random
        a=int(input("enter the starting of range: "))
        b=int(input("enter the ending of range: "))
        r=random.randint(a,b)
        c=0
        point=0
        while c<3:
                number=int(input("Guess the no. that you think will come between the above range: "))
                if number>r:
                        print("Have one more try")
                        print("************************ Your guess is too high **************************")
                elif number==r:
                        print("Congratulation you won this round")
                        point_won=random.randint(40,50)
                        point=point_won
                        print("Points won this round",point_won)
                        break
                else:
                        print("Have one more try")
                        print("************************ Your guess is too small ***************************")
                c=c+1
        return point_won
random()
total_point=0
while True:
    n=input("Press yes to play again |||| no to exit: ")
    if n=="yes":
        point=random()
        total_point=total_point+point
    elif n=="no":
        print("thankxx for playing")
        break
    else:
        print("restart")
print("total point scored",total_point)
