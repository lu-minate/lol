# in a list find the 2 largest numbers and print their sum
arr = []
arrCopy = arr.copy()
length = int(input("enter a number: "))
i = 0


def high(array):
    num1 = array[0]
    num2 = array[1]
    for i in range(length):
        if array[i] >= num1:
            num1 = array[i]
            array[i] = 0
    for i in range(length):
        if num2 <= arr[i] <= num1:
            num2 = arr[i]

    return num1+num2


for i in range(0, length):
    try:
        arr.append(int(input('enter a number: ')))
    except ValueError:
        print("number not valid")
    arrCopy = arr.copy()
sumOfTheMax = high(arr)
print(arrCopy[:])
print(sumOfTheMax)
