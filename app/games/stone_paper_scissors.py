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
        print('You have '+str(heart_user)+' lives ❤️')
        print('Your opponent has '+str(heart_pc)+' lives 💜')
        print("""
        Choose an option:
            1: scissors 🖖
            2: stone 👊
            3: paper ✋
        """)

        user_choice=int(input())
        if user_choice == 1:
            os.system('clear')
            if ale == 1:
                print('______________________________Tie 🤨______________________________\n\n\n\n')
                print('Scissors was chosen by the opponent 🖖')
                print('You chose scissors 🖖')
       
            elif ale == 2 :
                print('______________________________You lost 🤕______________________________\n\n\n\n')
                print('Stone was chosen by the opponent 👊')
                print('You chose scissors 🖖')
                heart_user-=1
            
            elif ale == 3:
                print('______________________________Won 😁______________________________\n\n\n\n')
                print('Paper was chosen by the opponent ✋')
                print('You chose scissors 🖖')
                heart_pc-=1
                


        elif user_choice == 2:
            os.system('clear')
            if ale == 1:
                print('______________________________Won 😁______________________________\n\n\n\n')
                print('Scissors was chosen by the opponent 🖖')
                print('You chose stone 👊')
                heart_pc-=1
       
            elif ale == 2 :
                print('______________________________Tie 🤨______________________________\n\n\n\n')
                print('Stone was chosen by the opponent 👊')
                print('You chose stone 👊')
            
            elif ale == 3:
                print('______________________________You lost 🤕______________________________\n\n\n\n')
                print('Paper was chosen by the opponent ✋')
                print('You chose stone 👊')
                heart_user-=1
                


            
        elif user_choice == 3:
            os.system('clear')
            if ale == 1:
                print('______________________________You lost 🤕______________________________\n\n\n\n')
                print('Scissors was chosen by the opponent 🖖')
                print('You chose paper ✋')
                heart_user-=1
       
            elif ale == 2 :
                print('______________________________Won 😁______________________________\n\n\n\n')
                print('Stone was chosen by the opponent 👊')
                print('You chose paper ✋')
                heart_pc-=1
            
            elif ale == 3:
                print('______________________________Tie 🤨______________________________\n\n\n\n')
                print('Paper was chosen by the opponent ✋')
                print('You chose paper ✋')

        else:
            os.system('clear')
            print('Enter a valid number 😵‍💫')

        if heart_pc == 1 and heart_user == 3 :
            print('Won the play 🤓') 
            print('You have '+str(heart_user)+' lives 💖')
            print('Your opponent has '+str(heart_pc)+' lives 🖤🖤🖤')
            break
        elif heart_pc == 3 and heart_user == 1:
            print('You lose the play ☠️☠️☠️')
            print('You have '+str(heart_user)+' lives 🖤🖤🖤')
            print('Your opponent has '+str(heart_pc)+' lives 💜')
            break
        elif heart_pc == 0:
            print('Won the play 🤓')
            print('You have '+str(heart_user)+' lives 💖')
            print('Tu oponente tiene '+str(heart_pc)+' lives 🖤🖤🖤')
            break
        elif heart_user == 0:
            print('You lose the play ☠️☠️☠️')
            print('You have '+str(heart_user)+' lives 🖤🖤🖤')
            print('Your opponent has '+str(heart_pc)+' lives 💜')
            break


if __name__ == '__main__':
    run()