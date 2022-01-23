
def remove_duplicates(list_nu):

    for single_digit in list_nu:

        if list_nu.count(single_digit) == 1:

            return print(single_digit)


# list_nu = [1,1,2,2,3,3,4,4,5]

list_nu = [1,2,3,4,1,3,4]

remove_duplicates(list_nu)



