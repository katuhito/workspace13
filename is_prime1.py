# 平方根を求めるのに使う数学モジュールを読み込む
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))) + 1): #平方根を計算
        if n % i == 0: #割り切れるか判定
            return False #割り切れれば素数ではない
    return True #いずれの数でも割りきれなかったときは素数
