def higher(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] < lst[1]:
            return higher(lst[1:])
        else:
            return higher([lst[0]] + lst[2:])

print(higher([1, 2, 3, 4]))