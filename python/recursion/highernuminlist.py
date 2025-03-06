def higher(list):
    if len(list) == 0:
        return list[0]
    else:
        new_list = list
        if list[0] < list[1]:
            new_list.append(list[1::])
        else:
            del list[1]
            new_list.apped(list)
        higher(new_list)
    
print(higher([1,2,3,4]))