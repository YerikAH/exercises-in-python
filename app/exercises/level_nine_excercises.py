# 1
country = ['Canada', 'USA', 'Mexico', 'Australia']

for i, pais in enumerate(country):
  print(f"{i}: {pais}")

#2
for i in range(0,101):
  print(i)

#3

num = int(input("Enter a number: "))

for i in range(1, 15):
  print(f"{num} x {i} = {num * i}")

#4

for i in range(10, 0, -1):
  print(i)

#5

count = 0
for i in range(2, 101, 2):
  count += 1
print(count)

#6

total = 0
for i in range(100, 201):
    total += i
print(total)

#7

num = int(input("Enter a number: "))

num_str = str(num)
digits = len(num_str)

print(f"The numbe {num} have {digits} digit")

#8

def fibonacci(n):
  a, b = 0, 1

  for i in range(n):
    print(a)
    a, b = b, a + b

fibonacci(10)

#9

list_original = ['a', 'b', 'c', 'd', 'e', 'f']

for i, element in enumerate(list_original):
  if i % 2 == 0:
    print(element)
#10

count = 0
validate = False
for i in range(10):
  if validate == True:
    count = count - 1
    print("*" * count)
  else:
    count = count + 1
    print("*" * count)
    if(count >= 5):
      validate = True
  
#11

for i in range(5):
  for j in range(5-i):
    print(5-j, end='')
  print()

#12

def prime_numbers(n):
  count = 0
  for i in range(2, n+1):
    is_prime = True

    for j in range(2, i):
      if i % j == 0:
        is_prime = False
        break

      if is_prime:
        print(i)
        count += 1

  print(f"There {count} numbers between 0 and {n}")

prime_numbers(100)
