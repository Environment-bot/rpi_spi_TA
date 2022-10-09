import threading
import logging
import time

def createLogger():
    formatt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=formatt, level=logging.INFO,
                        datefmt="%H:%M:%S")
    

def printInThread(sleep:int=4)->None:
    logging.info(f"Thread sleep {sleep}s has been started")
    time.sleep(sleep)
    logging.info(f"Thread with Sleep time {sleep}s has passed on thread")

def threadone()->None:
    
    pass


def main():
    createLogger()
    thred = threading.Thread(target=printInThread, args=(1,))
    
    logging.info("created thread but not started")
    thred.start()
    logging.info("Started thread and now waiting it to end")
    thred.join()
    logging.info("all done")

if __name__ == "__main__":
    main()

