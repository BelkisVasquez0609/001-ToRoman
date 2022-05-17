import os


# Method to convert
def ConvertToRoma(number):
    romans = ""
    th = ["", "M", "MM", "MMM", "I!V", "!V"]
    h = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    t = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    u = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    romans += th[int((number / 1000) % 10)]
    romans += h[int((number / 100) % 10)]
    romans += t[int((number / 10) % 10)]
    romans += u[int(number % 10)]

    return romans


# Method Main
if __name__ == '__main__':
    ContinueP = "S"

    print("Welcome to the app to convert decimals and arabic numbers to romans")

    while ContinueP == "S":
        Stay = True
        print("Press 'Enter' to continue...")
        pEnter = input()

        if pEnter != "":
            print("Press 'Enter' to continue...")
            ContinueP = "S"
            os.system("cls")
        else:
            print("Please,enter a number arabic or decimal to convert : ")
            numberArabic = input()

            if not numberArabic:
                print("You must fill in the field to perform the conversion")
            elif numberArabic.replace('.', '', 1).isnumeric():
                numberArabic = round(float(numberArabic))
                if numberArabic > 5000 or numberArabic <= 0:
                    print(" Invalid input: The number entered is out of range.")
                else:
                    resultRoman = ConvertToRoma(numberArabic)
                    print(resultRoman)
            else:
                print("Invalid Entry.")
            while Stay:
                print("If you want to continue enter ('S'), else press any key")
                ContinueP = input().upper()

                if not ContinueP:
                    print("You must fill in the field")
                    Stay = True
                    ContinueP = "S"
                elif ContinueP.isnumeric():
                    Stay = True
                    ContinueP = "S"
                else:
                    Stay = False


print("See you later")
input()