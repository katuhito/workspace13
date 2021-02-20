import queue

q = queue.Queue()

# キューに追加
q.put(3)
q.put(5)
q.put(2)

# キューから取り出し
temp = q.get()
print(temp)

temp = q.get()
print(temp)

# キューに追加
q.put(4)

# キューから取り出し
temp = q.get()
print(temp)

