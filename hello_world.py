sam_age = int(input("What is sam's age?\n"))


print("Sam's age is:", sam_age)

print("same's age type", type(sam_age))



def add(num1, num2):
  return num1 + num2

def different_add(*to_sum):
  our_sum = 0
  for num in to_sum:
    our_sum = our_sum + num
  return our_sum

def different_add_list(to_sum):
  our_sum = 0
  for num in to_sum:
    our_sum = our_sum + num
  return our_sum

def only_add_odd_numbers(*args):
  our_sum = 0
  for num in args:
    remainder = (num % 2)
    is_odd = remainder == 1
    if is_odd:
      our_sum = our_sum + num
  return our_sum

def add_numbers_till_age(age):
   return sum(range(1, age + 1)) 

# print(add(1, 2))
# print("different_add", different_add(1, 2, 3, 4))
# print("only_add_odd_numbers", only_add_odd_numbers(1, 2, 3, 4))
print("add_numbers_till_age", add_numbers_till_age(sam_age))
print("summing until sam's age", sum(range(1, sam_age + 1)))
print("add_numbers_till_age", add_numbers_till_age(sam_age + 26))
   
class Car:
  num_wheeel = 4

  def __init__(self, brand):
    self.brand = brand
  
  def honk(self):
    return "honk"


bmw = Car("bmw")
print(bmw.brand)
print(bmw.num_wheeel)
print(bmw.honk())
