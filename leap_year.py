def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400!= 0:
            return False
        else:
            return True
    else:
        return False

for i in range(1950, 2051):
    print(str(i) + '' + str(is_leap_year(i)))

