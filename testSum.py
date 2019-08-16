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
                                divide = difference//10
                                twosome = divide % 10 
                                Twostorage = twosome 
                                selfo = divide - twosome
                                final = selfo//10
                                Threestorage = final 
                                digitsum = Threestorage + Twostorage + Onestorage
                                return digitsum
print(sumDigits())                        

def convertWageMtoW(): 
        country = input("Please enter a country: ")
        mwage = float(input("Enter the Men's Wage: "))
        region = ["United States", "Korea", "Japan", "Finland", "Germany"]
        if country == region[0]:
                wage_gap = 0.182
                ratio = 1 - wage_gap
                return mwage * wage_gap
        elif country == region[1]:
                wage_gap = 0.346
                ratio = 1 - wage_gap
                return mwage * ratio
        elif country == region[2]:
                wage_gap = 0.245
                ratio = 1 - wage_gap
                return mwage * ratio
        elif country == region[3]:
                wage_gap = 0.177
                ratio = 1 - wage_gap
                return mwage * ratio
        elif country == region[4]:
                wage_gap = 0.162
                ratio = 1 - wage_gap
                return mwage * ratio
        
        
