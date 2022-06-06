
# python three practice

#1

import random
import os
import time

print("You are a warrior looking for treasures.")
dragon_choice= [1,2]
os.system("clear")
count = 0
while True:
    os.system("clear")
    random_dragon = random.choice(dragon_choice)
    user_choice = int(input("""
    You find 2 caves through which you want to enter
    1: Clean cave seems safe 💫
    2: Dark cave and that gives a bad 😟 

    """))
    if user_choice > 2:
        print("Invalid key 😠")
        time.sleep(2)
        os.system("clear")
    elif user_choice == random_dragon:
        count = count + 100
        print("A dragon appears and gives you his treasure 😃🐉")
        print('You have '+str(count)+' points')
        time.sleep(2)
        os.system("clear")
    elif user_choice != random_dragon:
        print("A dragon apeears and you lost me 💀")
        print('You have '+str(count)+' points')
        print("\nTry again: press key 'Enter'")
        print("Exit game: press key 'E'")
        exit_user=input('Enter key: ')
        count = 0
        if exit_user == 'e' or exit_user == 'E':
            os.system("clear")
            break
        time.sleep(1)
        os.system("clear")

#2

import random
import os
try:
    os.system("clear")
    k=0
    user = int(input('Tell me the length of the chain: '))
    if user >= 10 or user <= 0: print('Error 😐')
    else:
        user_input = input('Guess the chain between the numbers 1 and ' +str(user)+': ')
        num = [i for i in range(1,user+1)]
        random.shuffle(num)
        while True:
            numbers_user = [int(k) for k in user_input]
            count = 0
            for j in range (len(num)):
                if numbers_user[j] == num[j]:
                    count += 1
            if count == user:
                number_cute = "".join(map(str,numbers_user))
                print('With '+number_cute+' have you guessed '+str(count)+' values.')
                print('Congratulations, you win 😆')
                break
            else:
                number_cute = "".join(map(str,numbers_user))
                print('With '+number_cute+' have you guessed '+str(count)+' values.')
                user_input= input('Try to guess the string: ')
                os.system("clear")


except ValueError:
    print("You must put numbers 😐")

#3

user_word_one = input('Enter the first word: ')
user_word_two = input('Enter the second word: ')

one_first=user_word_one[len(user_word_one)-1]
two_first=user_word_two[len(user_word_two)-1]
one_second=user_word_one[len(user_word_one)-2]
two_second=user_word_two[len(user_word_two)-2]
one_third=user_word_one[len(user_word_one)-3]
two_third=user_word_two[len(user_word_two)-3]
if one_first == two_first and one_second == two_second:
    print('The words rhyme a bit')
elif one_first == two_first and one_second == two_second and one_third == two_third:
    print('The word rhyme')
else:
    print('The words dont rhyme')

#4


dollars = int(input ("How many dollars: "))
interest = float(input ("How much interest: "))
years = int(input ("Number of years: "))
x =int(dollars * ((1 + interest/100) ** years))
print("\nAfter "+ str(years) + " years, at "+ str(interest)+ "% interest, you will have earned $"+ str(x))