import os
import random

def run(): 
    allData = []
    with open("./lista.txt","r",encoding="utf-8") as data:
        for i in data:
            x = i.replace("\n","")
            allData.append(x)
    random_word=random.choice(allData).lower()
    att = ["_"] * len(random_word)
    while True:
        os.system('clear')
        for c in att :
            print(c, end=" ")
        user = input('Enter a character: ')
        for k ,cha in enumerate(random_word):
            if cha == user:
                att[k] = user
        if "_" not in att : 
            os.system('clear')
            print("Ganaste, la palabra correcta era: "+ random_word)
            input()
            break

if __name__ == '__main__':
    run() 