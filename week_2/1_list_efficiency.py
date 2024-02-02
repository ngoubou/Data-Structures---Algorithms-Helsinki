"""Compare the efficiency of two list methods."""

import time

n = 10**5

test_list = []

start_time = time.time()
for i in range(1,n+1): # sourcery skip
    test_list.append(i)
end_time = time.time()
print("time for additions:", round(end_time - start_time, 5), "s")


start_time = time.time()
for i in range(1,n+1): # sourcery skip
    test_list.pop()
end_time = time.time()
print("time for deletions:", round(end_time - start_time, 5), "s")

