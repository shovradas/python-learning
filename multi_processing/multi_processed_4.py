import time
from multiprocessing import Process

def do_something(seconds):
    print(f'Going to sleep for {seconds} second ...')
    time.sleep(1) # Lets assume that we are doing some task
    print(f'Done with sleeping!')

if __name__ == '__main__':  # Needed for windows
    start = time.perf_counter()

    processes = []
    for _ in range(10):
        p = Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')