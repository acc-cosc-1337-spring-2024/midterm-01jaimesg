
def get_bonus_pay_amount(ratio):

    result = ""
    if (ratio <= 1999 and ratio >= 1500):
        result1= ratio * .08
        return int(result1)
    elif (ratio <= 1499 and ratio >= 1000):
        result2= ratio * .07
        return int(result2)
    elif (ratio <= 999 and ratio >= 500):
        result3= ratio * .06
        return int(result3)
    elif (ratio <= 499 and ratio >= 0):
        result4= ratio * .05
        return int(result4)

    else:
        return 'invalid arguments'

    return result