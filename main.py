# main.py
import multiprocessing
from distributed_lock import DistributedLock
from file_operations import file_op

def main():
    num_procs = 3
    attempts = 5

    lock = DistributedLock(num_procs)
    wait_counter = multiprocessing.Value('i', 0)

    processes = [multiprocessing.Process(target=file_op, args=(i, attempts, lock, wait_counter)) for i in range(num_procs)]
    [p.start() for p in processes]
    [p.join() for p in processes]

if __name__ == "__main__":
    main()
