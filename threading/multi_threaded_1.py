from threading import Thread
import time

def do_something():
    print('Going to sleep for 1 second ...')
    time.sleep(1) # Lets assume that we are doing some task
    print('Done with sleeping!')

start = time.perf_counter()
t1 = Thread(target=do_something)
t2 = Thread(target=do_something)
t1.start()
t2.start()
finish = time.perf_counter()  # Gets executed right after the thread starts
print(f'Finished in {round(finish-start, 2)} seconds')