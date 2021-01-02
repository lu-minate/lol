'''print the largest element from the given list'''
def findmax(arr):
    # arr = [1, 42, 2, 64, 78, 34]
    '''temp = 0 
        maile paila esto garay ko thiye but 
        list ko 1st element lai greatest sochera garyo
        vane ramro hune raicha
    '''
    maximum = arr[0]
    for item in arr:
        if item > maximum:
            maximum = item
    print(maximum)



def pr():
    print('lol')
