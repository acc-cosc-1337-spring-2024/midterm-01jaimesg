
def get_miles_per_hour(num):
    ratio = .621371

    result = ""
    if (num <= 60 and num >= 0):
        result1= num * ratio
        return float(result1)


    else:
        return 'invalid arguments'

    return result