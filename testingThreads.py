import contextlib 
import threading
import logging
import time
import dataclasses

def createLogger()->None:
    formatt = "[%(asctime)s] - [%(threadName)13s] - [%(name)8s] - [%(levelname)8s] -- %(message)s (%(filename)s:%(lineno)s)"
    logging.basicConfig(format=formatt, level=logging.INFO,
                        datefmt="%H:%M:%S")
    

def printInThread(sleep:int=4)->None:
    logging.info(f"Thread sleep {sleep}s has been started")
    time.sleep(sleep)
    logging.info(f"Thread with Sleep time {sleep}s has passed on thread")

@dataclasses.dataclass
class ourdataclass:
    number : int = 1

@contextlib.contextmanager
def aquireLock(lock : threading.Lock, timeout : int):
    try:
        yield  lock.acquire(timeout=timeout)
    finally:
        lock.release()    


def tryingToAddNumber(lock : threading.Lock, data : ourdataclass)->None:
    with aquireLock(lock=lock, timeout=10) as lock:
        if lock:
            logging.info(f"before add || {data.number} ||")
            data.number += 1
            logging.info(f"after add  || {data.number} ||")
            time.sleep(1)
        else:
            logging.error(f"Failed to aquire lock")

    





def main():
    lock = threading.Lock()
    ourdata = ourdataclass()
    thread : list[threading.Thread] = []
    createLogger()
    for i in range(1, 10):
        logging.info(f"thread {i} started")
        threading.Thread(target=tryingToAddNumber, args=(lock, ourdata)).start()
    

    
    logging.info("Started thread and now waiting it to end")
    # for i in thread:
    #     i.join()

    logging.info(f"in main after .join || {ourdata.number} ||")
    logging.info("all done")

if __name__ == "__main__":
    main()

