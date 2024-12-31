import threading

n = 0


def foo():
    global n
    n += 1


threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)  # 预期输出 100，但有时会输出 99 或 98
