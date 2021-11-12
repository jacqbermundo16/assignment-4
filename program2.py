# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format
# The total amount is ___ .

def askQuantOfApplesAndOranges():
    appleQuant_ = int(input('How many apples do you want to buy? '))
    orangeQuant_ = int(input('How many oramges do you want to buy? '))
    return appleQuant_, orangeQuant_

def computeTotal(_appleQuant, _orangeQuant):
    _apples = int(_appleQuant * 20)
    _oranges = int(_orangeQuant * 25)
    _totalCost = int(_apples + _oranges)
    return _apples, _oranges, _totalCost

def display(totalCost_):
    print(f"The total amount is {totalCost_}.")


# steps
#1 Ask for number of apples and oranges you want to buy.
appleQuant, orangeQuant = askQuantOfApplesAndOranges()

#2 compute for the total amount of apples and oranges 
apples, oranges, totalCost = computeTotal(appleQuant, orangeQuant)

#3 Display the output
display(totalCost)

