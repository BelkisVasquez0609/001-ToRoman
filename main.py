def Validator(InputTest):
    Result = ""

    if not InputTest:
        Result = "You must fill in the field to perform the conversion"
        return Result
    else:
        if InputTest.replace('.', '', 1).isnumeric():
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

