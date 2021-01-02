import random


class Dice:
    def roll(self):
        num = {random.randint(1, 6), random.randint(1, 6)}
        return num


ob = Dice()
number = ob.roll()
# print(number)

list = [1, 2]
list2 = {1, 2}
try:
    list[0] = 3
except TypeError:
    print("tuple list []")
try:
    list2[0] = 3
except TypeError:
    print("tuple list 2 {}")
# print(list, list2)