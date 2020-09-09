import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def do_something(seconds):
    print(f'Going to sleep for {seconds} second ...')
    time.sleep(1) # Lets assume that we are doing some task
    return f'Done with sleeping!'

if __name__ == '__main__':  # Needed for windows
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]        
        for f in as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')