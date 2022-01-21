def print_me(array):

    for x in array: 
        
        if x%3 == 0 and x%5 == 0:
            array.remove(x)
            array.insert((x-3),"Strive School")

        elif x%3 == 0:
            array.remove(x)
            array.insert((x-1),"Strive")

        elif x%5 == 0:
            array.remove(x)
            array.insert((x-2),"School")       
    return array

    
print(print_me(([1,2,3,5,15])))