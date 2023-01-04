#1

def count_dig(num):
  convert_string = str(num)
  return len(convert_string)

result = count_dig(1500)
print(result)

#2

def adition_four_position(N):
  result = 0
  for i in range(N):
      if i % 4 == 0:
          result += i**2
  print(result)

adition_four_position(15)

#3

for i in range (0,11):
  result = ""
  for k in range(1,11):
    result = result + str(k)
  print(result)
    
#4

def table_product(num):
  for i in range (0,15):
    print(f"{num} x {i} = {num * i}")

table_product(5)

#5
def indentify_adition(num_1,num_2):
  adition_numbers= num_1 + num_2
  if adition_numbers % 2 != 0:
    print("Impar")
  else:
    print("Par")


indentify_adition(5,5)

#6

def digit_par(num):
  convert_string = str(num)
  for i in convert_string:
    convert_number = int(i)
    if convert_number % 2 == 0:
      print(f"Par: {i}")
    

digit_par(15780)

#7

clave_main = "186424752186214789212555"
clave_1 = ""
clave_2 = ""

def discoverd(x,clave_2,clave_1):
  for i in x:
    convert_number = int(i)
    if convert_number % 2 != 0:
      clave_2 = f"{clave_2}{i}"
    else:
      clave_1 = f"{clave_1}{i}" 
  print(clave_1)
  print(clave_2)
  

discoverd(clave_main,clave_2,clave_1)
