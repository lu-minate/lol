'''enter garayko numbers lai words ma convert garne'''
numbers = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '0': "zero"
}

num = input("phone: ",)
for i in num:

    '''
    check = numbers.get(i, "!") 
    print(check,  end=" ")
    '''
    print(numbers[i], end= " ")