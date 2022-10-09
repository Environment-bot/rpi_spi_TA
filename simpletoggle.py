from gpiozero import LED
# import threading
import concurrent.futures


class simpletoggle:
    def __init__(self, pin:int=1) -> None:
        self._led = LED(pin=pin)
        self._thread = 

    def initalizeThreadBlinker() -> None:
        with concurrent.futures.ThreadPoolExecutor() as excecutor:
            # TODO: Add thread creator here and start it.