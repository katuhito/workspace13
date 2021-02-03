n = 18

result = ''

while n > 0:
    # あまりを文字列の左側に追加していく
    result = str(n % 2) + result
    # 2で割った商を再度代入する
    n //= 2


print(result)
