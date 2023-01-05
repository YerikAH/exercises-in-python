import math

# 1
class RomanConverter:
  def to_roman(self, number):
    roman_digits = [
      ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), 
      ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), 
      ('V', 5), ('IV', 4), ('I', 1)
    ]

    roman_number = ''

    for rd, value in roman_digits:
      while number >= value:
        roman_number += rd
        number -= value

    return roman_number


converter = RomanConverter()
roman_number = converter.to_roman(2023)
print(roman_number) 

# 2

class RomanConverter:
  def to_int(self, roman_number):
    roman_digits = {
      'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 
      'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 
      'V': 5, 'IV': 4, 'I': 1
    }

    result = 0

    i = 0
    while i < len(roman_number):
      if i+1 < len(roman_number) and roman_number[i:i+2] in roman_digits:
        result += roman_digits[roman_number[i:i+2]]
        i += 2
      elif roman_number[i] in roman_digits:
        result += roman_digits[roman_number[i]]
        i += 1
      else:
        raise ValueError("The roman numeral is invalid")

    return result

converter = RomanConverter()
number = converter.to_int("MMXXIII")
print(number)  

# 3

class ParenthesisValidator:
  def is_valid(self, s):
    stack = []

    pairs = {
      "(": ")",
      "{": "}",
      "[": "]"
    }

    for c in s:
      if c in pairs:
        stack.append(c)
      elif len(stack) > 0 and c == pairs[stack[-1]]:
        stack.pop()
      else:
        return False

    if len(stack) > 0:
      return False

    return True

validator = ParenthesisValidator()

s = "([)["
if validator.is_valid(s):
  print(f"The string {s} is valid")
else:
  print(f"The string {s} is not valid")

# 4
class SubsetGenerator:
  def unique_subsets(self, lst):
    if len(lst) == 0:
      return [[]]

    last = lst[-1]

    subsets = self.unique_subsets(lst[:-1])

    result = []
    for subset in subsets:
      result.append(subset)
      result.append(subset + [last])

    return result


generator = SubsetGenerator()
subsets = generator.unique_subsets([4, 5, 6])
print(subsets)

# 5

class PairFinder:
  def find_pair(self, numbers, target):
    num_indices = {n: i for i, n in enumerate(numbers)}

    for i, n in enumerate(numbers):
      missing = target - n
      if missing in num_indices and num_indices[missing] != i:
        return i, num_indices[missing]

    return None


finder = PairFinder()
pair = finder.find_pair([10, 20, 10, 40, 50, 60, 70], 50)
print(pair)  

# 6

class ZeroSumFinder:
  def find_zero_sum(self, numbers):
    numbers.sort()

    result = []

    for i in range(len(numbers)):
      target = -numbers[i]
      start = i + 1
      end = len(numbers) - 1

      while start <= end:
        if numbers[start] + numbers[end] == target:
          result.append([numbers[i], numbers[start], numbers[end]])
          start += 1
          end -= 1
        elif numbers[start] + numbers[end] < target:
          start += 1
        else:
          end -= 1

    return result

finder = ZeroSumFinder()
result = finder.find_zero_sum([-25, -10, -7, -3, 2, 4, 8, 10])
print(result) 


# 7

class PowerCalculator:
  def pow(self, x, n):
    if n == 0:
      return 1
    elif n < 0:
      return 1 / self.pow(x, -n)
    elif n % 2 == 0:
      return self.pow(x, n // 2) * self.pow(x, n // 2)
    else:
      return x * self.pow(x, n - 1)

calculator = PowerCalculator()
result = calculator.pow(2, -3)
print(result)  

# 8
 
class WordReverser:
  def reverse(self, string):
    words = string.split()[::-1]
    return " ".join(words)

reverser = WordReverser()
result = reverser.reverse("Mi Diario Python")
print(result)

# 9

class StringPrinter:
  def __init__(self):
    self.string = ""

  def get_string(self):
    self.string = input("Ingrese una cadena: ")

  def print_string(self):
    print(self.string.upper())

printer = StringPrinter()
printer.get_string()
printer.print_string() 

# 10

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

rectangle = Rectangle(5, 10)
print(rectangle.area())  

# 11

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius ** 2

  def perimeter(self):
    return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.area())
print(circle.perimeter())  