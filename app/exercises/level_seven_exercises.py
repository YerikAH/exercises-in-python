import random

# 1

def adition_list(list_num):
  result = []
  count = 0
  for num in list_num:
    count = count + num
    result.append(count)
  return result

result_def = adition_list([1,2,3])
print(result_def)

#2

first_list = []
second_list = []
list_original = [1,2,3,4,5,6]
def delete_list(list_num):
  first_list = delete_list_too(list_num)
  second_list = delete_list_too(first_list)
  print(first_list)
  print(second_list)
  print(list_original)

def delete_list_too(list_num):
  delete_first = list_num[1:len(list_num)]
  delete_end = delete_first[0:len(delete_first)-1]
  return delete_end

delete_list(list_original)

#3

list_original = [1,2,5]
def sort_list(list_num):
  list_original_sort = sorted(list_num)
  k = 0
  for i in list_num:
    element_list_sort = list_original_sort[k]
    if element_list_sort != i:
      return False
    k = k + 1

result_def = sort_list(list_original)
if result_def == None:
  print(True)
else:
  print(False)

#4

def dupli(list_num):
  set_list = set(list_num)
  return len(set_list) < len(list_num)


def generate_random_list():
  random_list = []

  for i in range(23):
    random_number = random.randint(1, 100)
    random_list.append(random_number)

  return random_list

list_random_23 = generate_random_list()
print(dupli(list_random_23))

#5

list_original = [1,2,3,4,5,5,1]
def no_dupli(list_num):
  list_no_duplicate = list(set(list_num))
  print(list_no_duplicate)

no_dupli(list_original)

#6

def read_words_from_file(filename):
  with open(filename, "r") as file:bras
    words = []
    for line in file:
      line_words = line.split(" ")
      words.extend(line_words)

  return words

print(read_words_from_file("/app/assets/file_text_seven.txt"))

#7

def invert(list_original):
  word_invert = []
  k = 0
  for i in list_original:
    if i[::-1] == list_original[k]:
      word_invert.append(i)
    k = k + 1
  return word_invert

print(invert(["hola","mundo","español","somos","ana","reconocer"]))

#8

def bisect(lst, word):
  left = 0
  right = len(lst) - 1

  while left <= right:
    mid = (left + right) // 2

    if lst[mid] == word:
      return mid

    elif word < lst[mid]:
      right = mid - 1

    else:
      left = mid + 1

  return "Not found word"

