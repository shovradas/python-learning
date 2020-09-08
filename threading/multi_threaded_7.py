import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_something(seconds):
    print(f'Going to sleep for {seconds} second(s) ...')
    time.sleep(seconds) # Lets assume that we are doing some task
    return f'Done with sleeping! -- {seconds}'

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
    secs = [1, 4, 3, 2, 5]
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in as_completed(results):
        print(f.result())  # returns when the thread execution is complete

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')