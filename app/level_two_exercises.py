from functools import reduce

# python one practice

#1

def max_list(a): 
    num_max = a[0]
    for num in a :
        if num_max <= num:
            num_max = num
        else:
            num_max = num_max
    
    return num_max

sol = max_list([4,5,4,2,11,10])
print(sol)

#2

def max_len(a):
    num_max = len(a[0])
    num_show = a[0]
    for stg in a:
        if num_max <= len(stg):
            num_max = len(stg)
            num_show = stg
        else:
            num_max = num_max
            num_show = num_show
    
    return num_show

sol = max_len(['then','key','do'])
print(sol)

#3

def more(a,b):
    save=[]
    for i in a:
        if b <= len(i):
            save.append(i)
    
    return save

arg_a = ['ball','by','love','baby','are']
arg_b = 3
sol= more(arg_a,arg_b)
print(sol)

#4

def mayus(a):
    count = 0
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in a:
        for k in mayusculas:
            if i == k:
                count += 1
    return count


sol = mayus('MAus')
print(sol)

# 5

def bina(b):
    count = len(b)
    full = list(map(lambda x: int(x),b))[::-1]
    nums = [2**i for i in range(0,count)]
    product = [x*y for x,y in zip(full,nums)]
    sum = reduce(lambda x,y: x + y,product)
    return sum

sol = bina('10000111')
print(sol)

#6

user = input('Enter the year: ')
year = int(user)
while user:

    user_name = []
    user_age = []
    user_one_name= input('Enter your name: ')
    user_one_age = int(input('Enter your age: '))
    user_two_name= input('Enter your name: ')
    user_two_age =int( input('Enter your age: '))
    user_three_name= input('Enter your name: ')
    user_three_age = int(input('Enter your age: '))
    user_age.append(user_one_age)
    user_name.append(user_one_name)
    user_age.append(user_two_age)
    user_name.append(user_two_name)
    user_age.append(user_three_age)
    user_name.append(user_three_name)
        
    print(user_name)
    print(user_age)
    user = input('You want to exit the program press "Enter" or else type something: ')
    while user:

        next = input('Type -yes- if you want to pass the year if you don t press "Enter": ')
        if next == 'yes':
            year +=1
            user_one_age += 1
            user_two_age += 1
            user_three_age += 1
            user_age.insert(0,user_one_age)
            user_age.insert(1,user_two_age)
            user_age.insert(2,user_three_age)
            print("In the year "+str(year)+' '+str(user_name[0])+" have "+str(user_age[0]))
            print("In the year "+str(year)+' '+str(user_name[1])+" have "+str(user_age[2]))
            print("In the year "+str(year)+' '+str(user_name[1])+" have "+str(user_age[2]))

            
        back = input('Type -no- if you want to pass the year if you don t press "Enter":')
        if back == 'no':
            year -=1
            user_one_age -= 1
            user_two_age -= 1
            user_three_age -= 1
            user_age.insert(0,user_one_age)
            user_age.insert(1,user_two_age)
            user_age.insert(2,user_three_age)
            print("In the year "+str(year)+' '+str(user_name[0])+" have "+str(user_age[0]))
            print("In the year "+str(year)+' '+str(user_name[1])+" have "+str(user_age[2]))
            print("In the year "+str(year)+' '+str(user_name[1])+" have "+str(user_age[2]))

        user = input('You want to exit the program press "Enter" or else type something: ')
    
#7

def age(a):
    count=0
    for i in a:
        if i >= 18:
            count += 1

    return count

sol = (10,12,15,16,18,20,19,16,15,32)
print(age(sol))

#8

def search(b):
    user = input('Enter letter for search: ').lower()
    lower = [i.lower() for i in b]
    search = [k for k in lower if k[0] == user]
    if search == []:
        print('Dont there nothing')
    else:
        convert = [j.capitalize() for j in search]
        print("Name that were found")
        for result in convert:
            print('--'+result)

insert_name=['Anabel','Melisa','Andree','Suny','Harvey']     
search(insert_name)

#9

def count_vocal(a):
    vocal_a=0
    vocal_e=0
    vocal_i=0
    vocal_o=0
    vocal_u=0
    lower = [i.lower() for i in a]  
    for k in lower:
        if k == 'a' or k == 'á':
            vocal_a += 1
        if k == 'e' or k == 'é':
            vocal_e += 1
        if k == 'i' or k == 'í':
            vocal_i += 1
        if k == 'o' or k == 'ó':
            vocal_o += 1
        if k == 'u' or k == 'ú':
            vocal_u += 1

    print('Hay',str(vocal_a),'vocales "a"')
    print('Hay',str(vocal_e),'vocales "e"')
    print('Hay',str(vocal_i),'vocales "i"')
    print('Hay',str(vocal_o),'vocales "o"')
    print('Hay',str(vocal_u),'vocales "u"')
    

                
count_vocal("Hello, this can be inproved")

#10

def leap_year(a):
    if a % 4 == 0 :
        if a % 100 != 0:
            print('Yes, it s a leap year')
        elif  a % 100 == 0 and a % 400 == 0  :
            print('Yes, it s a leap year')
        else:
            print('Its not a leap year')
    else:
        print('Its not a leap year')

leap_year(2024)
