
def calculatePower(base, power):

    # base case
    if (power < 1):
        return 1
    else:
    # recursive case
        return base * calculatePower(base, power - 1)


if __name__ == "__main__":

    print(calculatePower(2, 2))