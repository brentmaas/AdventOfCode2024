import os
import subprocess
import time

t0 = time.time()
for day in range(1, 26):
    if os.path.isfile(f"day{day}/part1.py"):
        t1 = time.time()
        subprocess.check_call(["python", "part1.py"], stdout=subprocess.DEVNULL, cwd=f"day{day}")
        print(f"Day{day} part 1: {time.time()-t1:.3f}s")
    if os.path.isfile(f"day{day}/part2.py"):
        t1 = time.time()
        subprocess.check_call(["python", "part2.py"], stdout=subprocess.DEVNULL, cwd=f"day{day}")
        print(f"Day{day} part 2: {time.time()-t1:.3f}s")
print(f"Total: {time.time()-t0:.3f}s")
