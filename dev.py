import com
import typing


class dev(typing.Protocol):
    def open(self):
        ...
    def close(self):
        ...
    def setup(self, **kwargs):
        ...




class spi_dev:
    def __init__(self, com : com.Communication, dev :int = 0, bus : int = 0) -> None:
        self.spi = com

    def open(self): 
        s