def binarie_search(list,item):
    min = 0
    max = len(list) -1
    counter = 0
    while min<=max:
        counter += 1
        midle = int((min+max)/2)
        kick = list[midle]
        if kick == item:
            print(f'number of attempts {counter}')
            print(f'target is:')
            return kick
        if kick > item:
            print(f'{kick} is too high')
            max = midle - 1
        else:
            print(f'{kick} is too low')
            min = midle + 1
    return('fodeo number not founded in the list')

test_list = list(range(1,100))
print(binarie_search(test_list,1))
