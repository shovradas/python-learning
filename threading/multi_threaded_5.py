import time
from concurrent.futures import ThreadPoolExecutor

def do_something(seconds):
    print(f'Going to sleep for {seconds} second(s) ...')
    time.sleep(seconds) # Lets assume that we are doing some task
    return 'Done with sleeping!'

start = time.perf_counter()

with ThreadPoolExecutor() as executor:  # Using ThreadPoolExecutor instead of manual list
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')