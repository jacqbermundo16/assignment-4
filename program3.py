# Create a program which you will enter the amount of money you have , it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.
def getMoneyAndApplePrice():
    money_ = int(input("How much money do you have? "))
    applePrice_ = int(input("How much does each apple costs? "))
    return money_, applePrice_

def computeMaxApplesAndPrice(_money, _applePrice):
    _maxApples = int(_money // _applePrice)
    _totalAppleCost = int(_maxApples * _applePrice)
    _change = int(_money - _totalAppleCost)
    return _maxApples, _totalAppleCost, _change

def display(maxApples_, change_):
    print(f"You can buy {maxApples_} apples and your change is {change_} pesos.")
# steps
#1 ask for money and price of each apple
money, applePrice = getMoneyAndApplePrice()

#2 compute for max no. of apples and change
maxApples, totalAppleCost, change = computeMaxApplesAndPrice(money, applePrice)

#3 display the output
display(maxApples, change)