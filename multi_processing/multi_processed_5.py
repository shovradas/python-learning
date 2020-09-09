import time
from concurrent.futures import ProcessPoolExecutor

def do_something(seconds):
    print(f'Going to sleep for {seconds} second ...')
    time.sleep(1) # Lets assume that we are doing some task
    return f'Done with sleeping!'

if __name__ == '__main__':  # Needed for windows
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        
        print(f1.result())
        print(f2.result())    

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')