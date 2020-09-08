from threading import Thread
import time

def do_something(seconds):
    print(f'Going to sleep for {seconds} second(s) ...')
    time.sleep(seconds) # Lets assume that we are doing some task
    print('Done with sleeping!')

start = time.perf_counter()

threads = []
for _ in range(10):
    t = Thread(target=do_something, args=[2]) # Passing arguments to function
    t.start()
    threads.append(t)

for t in threads:
    t.join()

finish = time.perf_counter()  # Gets executed after all threads finish
print(f'Finished in {round(finish-start, 2)} seconds')