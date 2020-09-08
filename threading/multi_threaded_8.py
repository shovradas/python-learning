import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_something(seconds):
    print(f'Going to sleep for {seconds} second(s) ...')
    time.sleep(seconds) # Lets assume that we are doing some task
    return f'Done with sleeping! -- {seconds}'

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
    secs = [1, 4, 3, 2, 5]
    results = executor.map(do_something, secs) # map will return the result sequentially
    for result in results:
        print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')