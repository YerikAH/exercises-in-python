# python four practice


#1

import random
import os

#1: White
#2: Red
#3: Blue
#4: Green
#5: Yellow
      
os.system("clear")
user_money = int(input('Enter the total amount of the purchase: '))
if user_money >= 100:
  random_ball = [1,2,3,4,5]
  ball_choice = random.choice(random_ball)
  data=[ 
      ["Ball white", "it doesn't have"],
      ["Ball red", "10 percent"],
      ["Ball blue", "20 percent"],
      ["Ball green", "25 percent"],
      ["Ball yellow","50 percent"],
    ]
  print ("\n {:<25} {:<25}".format('COLOR','DISCOUNT') ,"\n")
  for one in data:
    color_one , discount_one = one
    print ("{:<25} {:<25}".format( color_one, discount_one))
  if ball_choice == 1:
    print("Randomly you got the ball white")
    print("We are sorry you did not win any discount")
    print("Your new total due "+str(user_money))
  elif ball_choice == 2:
    p = float(0.1)
    s = user_money * p
    r = user_money - s
    print("Randomly you got the ball red")
    print("Congratulations, you have won a 10 percent discount")
    print("Your new total due "+str(r))
  elif ball_choice == 3:
    p = float(0.2)
    s = user_money * p
    r = user_money - s
    print("Randomly you got the ball blue")
    print("Congratulations, you have won a 20 percent discount")
    print("Your new total due "+str(r))
  elif ball_choice == 4:
    p = float(0.25)
    s = user_money * p
    r = user_money - s
    print("Randomly you got the ball green")
    print("Congratulations, you have won a 25 percent discount")
    print("Your new total due "+str(r))
  elif ball_choice == 5:
    p = float(0.5)
    s = user_money * p
    r = user_money - s
    print("Randomly you got the ball yellow")
    print("Congratulations, you have won a 50 percent discount")
    print("Your new total due "+str(r))
else:
  print('Sorry, do not enter the promotion')

#2

print('Choose the desired product:')
print("""

PRODUCT                          PRICE

T-shirt.......................... 25
Belt............................. 10
Shoes............................ 150
Pants............................ 300
Socks............................ 15
Skirts........................... 34
Caps............................. 75
Sweater.......................... 88
Tie.............................. 91
Jacket........................... 500




PRODUCT                          CODE

T-shirt.......................... 1
Belt............................. 2 
Shoes............................ 3 
Pants............................ 4
Socks............................ 5
Skirts........................... 6 
Caps............................. 7
Sweater.......................... 8
Tie.............................. 9
Jacket........................... 10

""")

# var price
t_shirt = 25
belt = 10
shoes = 150
pants = 300
socks = 15
skirts = 34
caps = 75
sweater = 88
tie = 91
jacket = 500
i=0
codes = []
shop_one = [] 
total = 0
try:

  user_obj = int(input("How many object buy? "))
  while i < user_obj:
    user_code = int(input("Enter code: "))
    if user_code == 1:
      user_uni_shirt = int(input('How many units of T-shirt?: '))
      shirt_pay= user_uni_shirt * t_shirt
      total = total + shirt_pay
      shop_one.append(user_uni_shirt)
      codes.append(user_code)
    elif user_code == 2:
      user_uni_belt = int(input('How many units of belt?: '))
      belt_pay = user_uni_belt * belt
      total = total + belt_pay
      shop_one.append(user_uni_belt)
      codes.append(user_code)
    elif user_code == 3:
      user_uni_shoes = int(input('How many units of shoes?: '))
      shoes_pay= user_uni_shoes * shoes
      total = total + shoes_pay
      shop_one.append(user_uni_shoes)
      codes.append(user_code)
    elif user_code == 4:
      user_uni_pants = int(input('How many units of pants?: '))
      pants_pay = user_uni_pants * pants
      total = total + pants_pay
      shop_one.append(user_uni_pants)
      codes.append(user_code)
    elif user_code == 5:
      user_uni_socks =int( input('How many units of socks?: '))
      socks_pay = user_uni_socks * socks
      total = total + socks_pay
      shop_one.append(user_uni_socks)
      codes.append(user_code)
    elif user_code == 6:
      user_uni_skirts = int(input('How many units of skirts?: '))
      skirts_pay = user_uni_skirts * skirts
      total = total + skirts_pay
      shop_one.append(user_uni_skirts)
      codes.append(user_code)
    elif user_code == 7:
      user_uni_caps = int( input('How many units of caps?: '))
      caps_pay = user_uni_caps * caps
      total = total + caps_pay
      shop_one.append(user_uni_caps)
      codes.append(user_code)
    elif user_code == 8:
      user_uni_sweater = int(input('How many units of sweater?: '))
      sweater_pay = user_uni_sweater * sweater
      total = total + sweater_pay
      shop_one.append(user_uni_sweater)
      codes.append(user_code)
    elif user_code == 9:
      user_uni_tie = int(input('How many units of tie?: '))
      tie_pay = user_uni_tie * tie
      total = total + tie_pay
      shop_one.append(user_uni_tie)
      codes.append(user_code)
    elif user_code == 10:
      user_uni_jacket = int(input('How many units of jacket?: '))
      jacket_pay = user_uni_jacket * jacket
      total = total + jacket_pay
      shop_one.append(user_uni_jacket)
      codes.append(user_code)
    else:
      print('Invalid code, Try again')
      i-=1
    
    print('The total to pay is '+str(total))
    i+=1

  while True:
    user_pay = int(input('Enter your money: '))
    rsd = user_pay - total
    if user_pay < total or rsd < 0:
      print('Don t have enough money')
      user_pay = int(input('Enter your money: '))
    else:
      print('Successful purchase')
      print('You returned $'+str(rsd))
      break
except ValueError:
  print('Only numbers are allowed')

#3

print("""
Category           Price      Code     Day of delay  

Favorites           $2.50      1          $0.50
New                 $3.00      2          $0.75
Premieres           $3.50      3          $1.00
Super premieres     $4.00      4          $1.50
""")
total = 0
back = 0
while True:
  try:
    user_gnre = int(input("Enter the movie category code: "))
    if user_gnre >= 5 or user_gnre <= 0: print("Choose the correct code")
    user_back = int(input("Enter the number of days of delay of the return: "))
    if user_gnre == 1:
      back = user_back * 0.5
      total = 2.5 + back  
      break
    elif user_gnre == 2:
      back = user_back * 7.5
      total += 3.0 + back
      break
    elif user_gnre == 3:
      back = user_back * 1.0
      total += 3.5 + back
      break
    elif user_gnre == 4:
      back = user_back * 1.5
      total += 4.0 + back
      break

  except ValueError:
    print("Insert number, try again")
print("The total to pay is $"+str(total))
