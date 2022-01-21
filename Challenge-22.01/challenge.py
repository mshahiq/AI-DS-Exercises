def print_me(array):

    for x in array: 
        if x == 3:
            array.remove(x)
            array.insert((x-1),"Strive")

        elif x == 5:
            array.remove(x)
            array.insert((x-2),"School")

        elif x == 30:
            array.remove(x)
            array.insert((x-3),"Strive School")
        
    return array

    
print(print_me(([1,2,3,5,10,15,30])))