def gengo(y):
    if y < 1868:
        return ''
    elif y < 1912:
        return '明治' + str(y - 1867) + '年'
    elif y < 1926:
        return '大正' + str(y - 1911) + '年'
    elif y < 1989:
        return '昭和' + str(y - 1925) + '年'
    elif y < 2019:
        return '平成' + str(y - 1988) + '年'
    else:
        return '令和' + str(y - 2018) + '年'

for y in range(1868, 2020):
    print(str(y) + ':' + str(gengo(y)))
