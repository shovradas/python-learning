import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def do_something(seconds):
    print(f'Going to sleep for {seconds} second ...')
    time.sleep(1) # Lets assume that we are doing some task
    return f'Done with sleeping! -- {seconds}'

if __name__ == '__main__':  # Needed for windows
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        secs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # Depending on the availability of CPU cores execution finish order may vary
        results = executor.map(do_something, secs) # But map will return the result in execution start order

        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')