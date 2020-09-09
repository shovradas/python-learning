import time
from multiprocessing import Process

def do_something():
    print('Going to sleep for 1 second ...')
    time.sleep(1) # Lets assume that we are doing some task
    print('Done with sleeping!')

if __name__ == '__main__':  # Needed for windows
    start = time.perf_counter()

    p1 = Process(target=do_something)
    p2 = Process(target=do_something)

    p1.start()
    p2.start()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')