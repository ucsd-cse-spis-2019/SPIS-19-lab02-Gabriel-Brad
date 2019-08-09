def sumTwo (a,b):
        c = a + b 
        return c

def getNumber():
    symbols = input("Enter a digit: ")
    number = int(symbols)
    if number < 0:
        return number
    while True:
        symbols = input("Enter a digit: ")
        number1 = int(symbols)
        if number1 < 0:
            return number
        else:
            number = number * 10 + number1 


x = sumTwo (3,5)
print(x)

print(getNumber())

def sumDigits():
                while True:
                        number = int(input("Please enter a number: "))
                        if number > 0: 
                                quotient = number % 10
                                Onestorage = quotient
                                difference = number - quotient
                                divide = diffreence//10
                                twosome = divide % 10 
                                Twostorage = twosome 
                                selfo = divide - twosome
                                final = selfo//10
                                Threestorage = final 
                                digitsum = Threestorage + Twostorage + Onestorage
                                return digitsum
print(sumDigits())                        
