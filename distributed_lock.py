# distributed_lock.py
import multiprocessing
from queue import Empty

class DistributedLock:
    def __init__(self, num_procs):
        self.num_procs = num_procs
        self.timestamp = multiprocessing.Array('i', [0] * num_procs)
        self.queue = multiprocessing.Queue()

    def get_ts(self, pid):
        return self.timestamp[pid]

    def update_ts(self, pid):
        self.timestamp[pid] += 1

    def request(self, pid, ts):
        for i in range(self.num_procs):
            if i != pid:
                self.queue.put((i, pid, ts))

    def release(self, pid):
        self.update_ts(pid)
