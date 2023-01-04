
# python one practice

#1

def compare(a,b):
    if a > b:
        return a
    return b

sol = compare(1,2)
print(sol)

#2

def max_three(a,b,c):
    if a > b and a > c:
        return a
    else :
        if b > c:
            return b
        return c 
    
sol = max_three(3,4,5)
print(sol)

#3

def count(a):
    count_sum = 0
    for i in a:
        count_sum += 1
    
    print(count_sum)

count([1,2,3,4,5,6,7,8,9])

#4

def vocal(a):
    true = 0
    false = 0
    vocal = ['a','e','i','o','u','A','E','I','O','U','Á','É','Í','Ó','Ú']
    for i in vocal:
        if i == a:
            true += 1
        else:
            false += 1
    if true == 1:
        return True
    else:
        return False

sol = vocal('b')
print(sol)

#5

def sum_multi(a):
    count_sum = 0
    count_multi = 1
    for i in a:
        count_sum = i + count_sum
    for i in a:
        count_multi = i * count_multi
    print(count_sum)
    print(count_multi)
    
sum_multi([1,2,3,4])

#6

def reverse(a):
    x = a[::-1]
    return x

sol = reverse('keys')
print(sol)

#7

def reverse(a):
    x = a[::-1].lower()
    y = a.lower()
    if x == y:
        return "Is palindrome"
    else:
        return "Is not a palindrome"        

sol = reverse('Ana')
print(sol)

#8

def sup(a,b):
    count_true = 0
    count_false = 0
    for i in a:
        for k in b:
            if i == k:
                count_true +=1
            else:
                count_false += 1
    if count_true > 0:
        return True
    else:
        return False

sol= sup([1,2,3,4,5],[6,7,8,9,10])
print(sol)

#9

def generate(a,b):
    return a * b
sol = generate(5,'y')
print(sol)

#10

def process(a):
    for i in a:
        print("*" * i)

process([5,2,10,4,10,3,2,12])