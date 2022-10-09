from dataclasses import dataclass
from enum import Enum


class outputMode(Enum):
    SPI = 1
    OUTPUT = 2
    INPUT = 3
    UART = 4

@dataclass
class PinData:
    pin : int
    mode : outputMode
    info : str
