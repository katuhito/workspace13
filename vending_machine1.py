# 投入する金額を受け取る
insert_price = input('insert: ')

# 商品の金額を受け取る
product_price = input('product: ')

# 型を変換しておつりを計算
change = int(insert_price) - int(product_price)

print(change)


