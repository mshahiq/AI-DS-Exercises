# def strive_school_challenge(input_list):

#     output_list = []

#     for i in input_list:
#         if (i%3==0) and (i%5==0):
#             output_list.append("Strive School")
#         elif (i%3==0):
#             output_list.append("Strive")
#         elif (i%5==0):
#             output_list.append("School")
#         else:
#             output_list.append(i)                     #d_on: number not divisible by 3 neither by 5
#     return output_list

# input_list = [1,2,3,9,15,21,25,30]

# print(strive_school_challenge(input_list))

class strive_school_challenge:

    def __init__(self,input_list) -> None:
        self.input_list = input_list

    def strive_3_school_5(self):

        output_list = []
    
        for i in self.input_list:
            if (i%3==0) and (i%5==0):
                output_list.append("Strive School")
            elif (i%3==0):
                output_list.append("Strive")
            elif (i%5==0):
                output_list.append("School")
            else:
                output_list.append(i)                     #d_on: number not divisible by 3 neither by 5
        return output_list

divisibility_test_of_3_5_3and5 = strive_school_challenge([1,2,3,9,15,21,25,30])
print(divisibility_test_of_3_5_3and5.strive_3_school_5())



