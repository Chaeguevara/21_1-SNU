import time
t_start = time.perf_counter()
for i in range(1000):
    # print(i)
    pass
t_end = time.perf_counter()
print (t_end-t_start)*1000