

import spidev
from dataclasses import dataclass
from datetime import date
import threading
import enum
import dataclasses
import contextlib

from testingThreads import aquireLock

class spiState(enum.Enum):
    WRITESPI = 1
    READSPI = 2


@contextlib.contextmanager
def aquireLock(lock : threading.Lock, timeout : int):
    try:
        yield  lock.acquire(timeout=timeout)
    finally:
        lock.release()    

@dataclasses.dataclass
class pipeline:
    Intquenue : list[int] = []
    time : list[date] = []
    state : spiState = spiState.READSPI




class writter:
    def __init__(self, data : pipeline, lock : threading.Lock) -> None:
        self.data = data
        self.lock = lock
    


class
        



class spirunner:
    def __init__(self, 
                thread : threading.Thread,
                event : threading.Event,
                pipeline : pipeline):
        self.thread = thread
        self.event = event
        self.pipeline = pipeline

    def run(self):
        self.thread.start()

    def 