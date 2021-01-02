month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
accept = int(input("> "))
if 0 < accept <= 12:
    print(month[accept])
else:
    print("enter number > 0 and < 12")
