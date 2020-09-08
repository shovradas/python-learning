from threading import Thread
import time

def do_something():
    print('Going to sleep for 1 second(s) ...')
    time.sleep(1) # Lets assume that we are doing some task
    print('Done with sleeping!')

start = time.perf_counter()
t1 = Thread(target=do_something)
t2 = Thread(target=do_something)
t1.start()
t2.start()
t1.join()
t2.join()
finish = time.perf_counter()  # Gets executed after t1 & t2 finishes
print(f'Finished in {round(finish-start, 2)} seconds')