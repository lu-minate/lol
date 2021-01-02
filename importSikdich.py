from greatest import findmax
arr = []
for i in range(3):
    ele = input("Enter a number: ")
    arr.append(ele)
print(f'the max among {arr} is {findmax(arr)}')
