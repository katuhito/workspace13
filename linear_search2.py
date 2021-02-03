def linear_search(data, value): #リストから求める値の位置を検索する関数を定義
    for i in range(len(data)):
        if data[i] == value: #ほしい値が見つかった場合
            return i
            return -1

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(linear_search(data, 40))
