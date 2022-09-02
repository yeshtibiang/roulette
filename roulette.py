from random import randint

playerTotalMoney = 50000
print("======Roulette Game=====")
print("This is a roulette game where you bet a number between 0 and 49")
print("welcome player 1, you have " + str(playerTotalMoney) + "$.")

while playerTotalMoney > 0:
    numberBet = int(input("Bet a number between 0 and 49: "))
    if numberBet < 0 or numberBet > 49:
        continue

    amountBet = int(input("Enter the amount of money to bet: "))
    if amountBet < 0 or amountBet > playerTotalMoney:
        print("You don't have that money, try again in the next round")
        continue
    randNumber = randint(0,49)
    if numberBet == randNumber :
        amountBet *= 50
        playerTotalMoney += amountBet
        print("Congratulation you have won " + str(amountBet) + ", your total money = " + str(playerTotalMoney))
        playAgain = int(input("Bet again ? (enter any number for yes and 0 for no):"))
        if playAgain != 0:
            continue
        else:
            exit(1)
    else:
        playerTotalMoney -= amountBet
        print("You have lost " + str(amountBet) + ", your total money = " + str(playerTotalMoney))
        if playerTotalMoney > 0:
            print("sorry try again in the next round")

if playerTotalMoney == 0:
    print("sorry you lost the game")