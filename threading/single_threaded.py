import time

def do_something():
    print('Going to sleep for 1 second ...')
    time.sleep(1) # Lets assume that we are doing some task
    print('Done with sleeping!')

start = time.perf_counter()
do_something()
do_something()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')