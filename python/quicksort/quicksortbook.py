def quickshort(array):
    if len(array) <  2:
        return array
    else:
        pivo = array[0]
        lowers = [i for i in array[1:] if i <= pivo]
        upers = [i for i in array[1:] if i > pivo]
        return quickshort(lowers) + [pivo] + quickshort(upers)
    
print(quickshort([1,9,4,3,7,9,2,3,1,0,9]))