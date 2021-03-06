text = list('SHOEISHA SESSHOP') #テキストをリストに変換
pattern = list('SHA') #パターンをリストに変換

for i in range(len(text)):
    match = True #一致しているものとして探索開始
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False #一致しなかった
            break
    if match: #全ての文字が一致していれば出力
        print(i)
        break
