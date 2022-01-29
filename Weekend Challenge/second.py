# def print_reverse_pyramid(height):

#     for elements_in_line in range(height,0,-1):
    
#         print((' '*(elements_in_line-1)) + ((height-elements_in_line+1)*'#') )

# print_reverse_pyramid(5)


class print_reverse_pyramid:

    def __init__(self,height) -> None:
        self.height = height

    def print_lines(self):
    
        for elements_in_line in range(self.height,0,-1):
    
            print((' '*(elements_in_line-1)) + ((self.height-elements_in_line+1)*'#') )

print_hash_reverse = print_reverse_pyramid(5)
print_hash_reverse.print_lines()
