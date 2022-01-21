def try_me(lst):

    for i in lst:

        if (i%3==0) and (i%5==0):
            d_35 = print("Strive School")
        elif (i%3==0):
            d_3 = print("Strive")
        elif (i%5==0):
            d_5 = print("School")
        else:
            d_on = print(i)                     #d_on: number not divisible by 3 neither by 5

    return d_35,d_3,d_5,d_on

lst = [3,3,3,9,15,25,1,2,2,30,54]

try_me(lst)