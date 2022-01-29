# def remove_duplicates(list_numbers):

#     for single_digit in list_numbers:

#         if list_numbers.count(single_digit) == 1:

#             return print(single_digit)


# # list_numbers = [1,1,2,2,3,3,4,4,5]

# list_numbers = [1,2,3,4,1,3,4]

# remove_duplicates(list_numbers)

class remove_duplicates:

    def __init__(self,list_of_numbers) -> None:
        self.list_of_numbers = list_of_numbers

    def detect_duplicates(self):
    
        for single_digit in self.list_of_numbers:

            if self.list_of_numbers.count(single_digit) == 1:

                return single_digit

removal_of_duplicate_values = remove_duplicates([1,2,3,4,1,3,4])
print(removal_of_duplicate_values.detect_duplicates())
