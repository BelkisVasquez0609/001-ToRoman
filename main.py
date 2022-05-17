
#Method Validator... Validate Range of numbers, Not null, The valid input
def Validator(InputTest):
    Result = ""

    if not InputTest:
        Result = "You must fill in the field to perform the conversion"
        return Result
    else:
        # Remove the dot (.) to validate that this string is a number
        if InputTest.replace('.', '', 1).isnumeric():
            #Convert to float the string and round to int.
            InputTest = round(float(InputTest))
            if 0 <= InputTest > 5000:
                Result = "The number entered is out of range"
                return Result
            else:
                Result = "The Result is valid"
                return Result
        else:
            Result = "Invalid Input"
            return Result
#Method to say if i want to continue on the program.
def Convertions(Continue):
    Result = ""
    if not Continue:
        Result = "You must fill in the field to perform the conversion"
        return Result
    elif Continue.isnumeric():
        Result = "Invalid Entry"
        return Result
    else:
        Result = "Valid Entry"
        return Result

