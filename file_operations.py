# file_operations.py
import time
from queue import Empty

def file_op(pid, attempts, lock, wait_counter):
    fname = "shared_file.txt"

    for _ in range(attempts):
        ts = lock.get_ts(pid) + 1
        lock.request(pid, ts)

        while True:
            try:
                response = lock.queue.get(timeout=1)
                if response[2] == ts:
                    break
                else:
                    lock.queue.put(response)
            except Empty:
                pass

        print(f"P{pid} locked attempt {_} -> counter: {response[1]}.")
        with open(fname, "r+") as f:
            content = f.read().strip()
            counter = int(content) + 1 if content else 1
            print(f"P{pid} released the lock.")
            print(f"P{pid} locked attempt {_ + 1} -> counter: {counter}.")
            f.seek(0)
            f.write(str(counter))
            f.truncate()
            time.sleep(0.5)  # Simulate some processing time
        lock.release(pid)

        # Increment wait_counter each time the process has to wait for the lock
        if _ > 0:
            wait_counter.value += 1

    print(f"P{pid} took an average of {wait_counter.value/attempts:.1f} attempts to access the file.")
