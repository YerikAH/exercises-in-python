import random
import os
def run():
    #1: scissors
    #2: stone
    #3: paper
    os.system('clear')
    heart_pc=3
    heart_user=3
    hand=[1,2,3]
    ale=random.choice(hand)
    while True:
        print('You have '+str(heart_user)+' lives โค๏ธ')
        print('Your opponent has '+str(heart_pc)+' lives ๐')
        print("""
        Choose an option:
            1: scissors ๐
            2: stone ๐
            3: paper โ
        """)

        user_choice=int(input())
        if user_choice == 1:
            os.system('clear')
            if ale == 1:
                print('______________________________Tie ๐คจ______________________________\n\n\n\n')
                print('Scissors was chosen by the opponent ๐')
                print('You chose scissors ๐')
       
            elif ale == 2 :
                print('______________________________You lost ๐ค______________________________\n\n\n\n')
                print('Stone was chosen by the opponent ๐')
                print('You chose scissors ๐')
                heart_user-=1
            
            elif ale == 3:
                print('______________________________Won ๐______________________________\n\n\n\n')
                print('Paper was chosen by the opponent โ')
                print('You chose scissors ๐')
                heart_pc-=1
                


        elif user_choice == 2:
            os.system('clear')
            if ale == 1:
                print('______________________________Won ๐______________________________\n\n\n\n')
                print('Scissors was chosen by the opponent ๐')
                print('You chose stone ๐')
                heart_pc-=1
       
            elif ale == 2 :
                print('______________________________Tie ๐คจ______________________________\n\n\n\n')
                print('Stone was chosen by the opponent ๐')
                print('You chose stone ๐')
            
            elif ale == 3:
                print('______________________________You lost ๐ค______________________________\n\n\n\n')
                print('Paper was chosen by the opponent โ')
                print('You chose stone ๐')
                heart_user-=1
                


            
        elif user_choice == 3:
            os.system('clear')
            if ale == 1:
                print('______________________________You lost ๐ค______________________________\n\n\n\n')
                print('Scissors was chosen by the opponent ๐')
                print('You chose paper โ')
                heart_user-=1
       
            elif ale == 2 :
                print('______________________________Won ๐______________________________\n\n\n\n')
                print('Stone was chosen by the opponent ๐')
                print('You chose paper โ')
                heart_pc-=1
            
            elif ale == 3:
                print('______________________________Tie ๐คจ______________________________\n\n\n\n')
                print('Paper was chosen by the opponent โ')
                print('You chose paper โ')

        else:
            os.system('clear')
            print('Enter a valid number ๐ตโ๐ซ')

        if heart_pc == 1 and heart_user == 3 :
            print('Won the play ๐ค') 
            print('You have '+str(heart_user)+' lives ๐')
            print('Your opponent has '+str(heart_pc)+' lives ๐ค๐ค๐ค')
            break
        elif heart_pc == 3 and heart_user == 1:
            print('You lose the play โ?๏ธโ?๏ธโ?๏ธ')
            print('You have '+str(heart_user)+' lives ๐ค๐ค๐ค')
            print('Your opponent has '+str(heart_pc)+' lives ๐')
            break
        elif heart_pc == 0:
            print('Won the play ๐ค')
            print('You have '+str(heart_user)+' lives ๐')
            print('Tu oponente tiene '+str(heart_pc)+' lives ๐ค๐ค๐ค')
            break
        elif heart_user == 0:
            print('You lose the play โ?๏ธโ?๏ธโ?๏ธ')
            print('You have '+str(heart_user)+' lives ๐ค๐ค๐ค')
            print('Your opponent has '+str(heart_pc)+' lives ๐')
            break


if __name__ == '__main__':
    run()