def sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        f = lst[-1] + lst[-2]
        newlist = lst[:-2:]
        newlist.append(f)
        sum(newlist)

print(sum([1,2,3,4]))
