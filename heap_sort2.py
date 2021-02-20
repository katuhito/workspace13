def heapify(data, i):
    left = 2 * i + 1 #左下の位置
    right = 2 * i + 2 #右下の位置
    size = len(data) - 1
    min = i
    # 左下のほうが小さいとき
    if left < size and data[min] > data[left]:
        min = left
        # 右下のほうが小さいとき
        if right <= size and data[min] > data[right]:
            min = right
    # 交換が発生するとき
    if min != i:
        data[i], data[min] = data[min], data[i]
        # ヒープ再構成
        heapify(data, min)

data = [6,15,4,2,8,5,11,9,7,13]
# ヒープを構成
for i in reversed(range(len(data) // 2)):
    # 葉ノード以外を処理
    heapify(data, i)

# ソートを実行
sorted_data = []
for _ in range(len(data)):
    # 最後のノードと先頭を入れ替え
    data[0], data[-1] = data[-1], data[0]
    # 最小のノードを取り出してソート済みにする
    sorted_data.append(data.pop())
    # ヒープを再構成
    heapify(data, 0)

print(sorted_data)
