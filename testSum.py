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
