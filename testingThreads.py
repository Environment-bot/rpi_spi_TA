from cmath import log
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

    
def testEventToNotifyThread(lock : threading.Lock, 
                            data : ourdataclass,
                            event : threading.Event
                            )->None:

    asd : int = 0
    
    while True:
        if event.is_set():
            logging.info("event recived")
            with aquireLock(lock=lock, timeout=5) as lock:
                if lock:
                    asd = data.number
                else:
                    logging.error("Error in reading data after event")

        logging.info("turning led state")
        time.sleep(2)

        if asd == 15:
            logging.info(f"value reached value: {asd=}")
            break


        




def main():
    event = threading.Event()
    lock = threading.Lock()
    ourdata = ourdataclass()
    # thread : list[threading.Thread] = []
    createLogger()
    thread = threading.Thread(target=testEventToNotifyThread, args=(lock, ourdata, event))
    thread.start()
    
    # for i in range(1, 10):
    #     logging.info(f"thread {i} started")
    #     threading.Thread(target=tryingToAddNumber, args=(lock, ourdata)).start()
    

    
    logging.info("Started thread")

    with aquireLock(lock=lock, timeout=10) as lock:
        if lock:
            ourdata.number=15
        else:
            logging.error("failed to chainge ourdata value")
    
    time.sleep(10)
    logging.info("trying to notify thread")
    event.set()
    logging.info("waiting to other thread to break out")
    thread.join()
    
    logging.info(f"in main after .join || {ourdata.number} ||")
    logging.info("all done")

if __name__ == "__main__":
    main()

