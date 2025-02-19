def binarie_search(list,item):
    min = 0
    max = len(list) -1
    while min<=max:
        midle = int((min+max)/2)
        kick = list[midle]
        if kick == item:
            return midle
        if kick > item:
            max = midle - 1
        else:
            min = midle + 1
    return None
test_list = list(range(1,100))

print(binarie_search(test_list,66))
