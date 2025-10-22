import time

start = time.perf_counter_ns()
print(f"Model load time: {(time.perf_counter_ns() - start) / 1e6:.0f} ms")