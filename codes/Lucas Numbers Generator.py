
import time
import sys
import resource

def lucas_sequence(n):
    if n == 0:
        return [2]
    if n == 1:
        return [2, 1]
    seq = [2, 1]
    for i in range(2, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


start_time = time.time()
result = lucas_sequence(10)
end_time = time.time()
runtime = end_time - start_time
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
print(f"Result: {result}, Runtime: {runtime:.6f}s, Memory: {mem_usage} bytes")