def divisibi(array):
    
    Strive_School = "Strive School"
    Strive        = "Strive"
    School        = "School"

    for number in array:

        if((number%3==0) & (number%5==0)):
            
            return Strive_School

        elif number % 3 == 0:
            
            return Strive

        elif number % 5 == 0:
            
            return School

        return array