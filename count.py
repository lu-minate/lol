# count the number of times a character appears in a string
string = input("enter a string: ")
char = input("enter a character: ")
count = 0
for i in string:
    if i is char:
        count += 1
print(count)
