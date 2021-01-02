numbers = [5, 2, 5, 2, 2]
for i in numbers:
    for j in range(i):
        print("x", end="")
    print()

'''
same mathi ko jastai chalcha but same line
ma print garnu ko lagi extra end="" lekhi
ranu pardaina so beginners le pani bujcha
for i in numbers:
    output = ""
    for j in range(i):
        output += "x"        
    print(output)

'''