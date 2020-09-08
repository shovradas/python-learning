from threading import Thread
import time

def do_something():
    print('Going to sleep for 1 second ...')
    time.sleep(1) # Lets assume that we are doing some task
    print('Done with sleeping!')

start = time.perf_counter()

threads = []
for _ in range(10):
    t = Thread(target=do_something)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

finish = time.perf_counter()  # Gets executed after all threads finish
print(f'Finished in {round(finish-start, 2)} seconds')