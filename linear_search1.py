data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
found = False #処理状況を管理する(初期値はFalse)

for i in range(len(data)):
    if data[i] == 40: #見つけたい値と一致したか
        print(i)
        found = True #見つかったことを処理状況としてセット
        break

if not found: #見つからなかった場合
    print('Not Found')


