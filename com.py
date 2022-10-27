import queue
import typing
import spidev

class Communication(typing.Protocol):

  
    

    def openConnection(self) -> None:
        ...
    
    def closeConnection(self, n : bytearray) -> None:
        ...

    def Write(self, list : list[bytes]) -> None:
        ...

    def WriteToBuffer(self, list : list[bytes]) -> None:
        ...

    def ReadBuffer() -> bytes:
        ...
    

# Wrapper class for spidev
class SPICom():
    def __init__(self, dev : int, bus : int, spidev : spidev.Spidev) -> None:
        self.dev = dev
        self.bus = bus
        self.spidev = spidev
        
        

    def openConnection(self) -> None:
        self.spidev.open(self.bus, self.dev)
    
    def closeConnection(self, n : bytearray) -> None:
        self.spidev.close()

    def Write(list : list[bytes]) -> None:
        ...

    def WriteToBuffer(list : list[bytes]) -> None:
        ...

    def ReadBuffer() -> None:
        ...
        