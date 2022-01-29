# def print_pyramid(height):
    
#     for elements_in_line in range(0,height,1):
    
#         print(((elements_in_line+1)*'#') )

# print_pyramid(5)


class print_pyramid:

    def __init__(self,height) -> None:
        self.height = height

    def print_lines(self):
    
        for elements_in_line in range(0,self.height,1):
    
            print(((elements_in_line+1)*'#') )


print_hash = print_pyramid(5)
print_hash.print_lines()
