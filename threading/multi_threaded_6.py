import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_something(seconds):
    print(f'Going to sleep for {seconds} second(s) ...')
    time.sleep(seconds) # Lets assume that we are doing some task
    return 'Done with sleeping!'

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]
    for f in as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')