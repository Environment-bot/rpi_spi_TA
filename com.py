import typing
import spidev

class Communication(typing.Protocol):

    bits_per_word : int =0
    cshigh : int = 0
    loop :bool = False
    no_cs : bool = False
    lsbfirst : bool = False
    max_speed_hz : int = 5000
    mode : int = 0
    threewire :bool = False

    

    def openConnection(self) -> None:
        ...
    
    def closeConnection(self, n : bytearray) -> None:
        ...

    def Write(self, list : list[bytes]) -> None:
        ...

    def WriteToBuffer(self, list : list[bytes]) -> None:
        ...

    def ReadBuffer() -> None:
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
        

    def WriteToBuffer(list : list[bytes]) -> None:
        ...

    def ReadBuffer() -> None:
        ...
        