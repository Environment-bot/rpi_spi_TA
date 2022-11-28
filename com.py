import queue
import typing
import buffer
import enum

class com_state(enum.Enum):
    CONNECTED = enum.auto()
    DISCONNECTED = enum.auto()
    CONNECTING = enum.auto()
    ERROR = enum.auto()
    IDLE = enum.auto()
    


class Communication(typing.Protocol):

    # _buffer : buffer.fifo_proto
    state : com_state

    def openConnection(self) -> None:
        ...
    
    def closeConnection(self) -> None:
        ...

    def Write(self, list : list[bytes]) -> None:
        ...

    def ReadBuffer(self) -> bytes:
        ...
    def setup(self, **kwargs)->None:
        ...

class spi_settings(enum.Enum):
    MAX_SPEED_HZ = "max_speed_hz"
    BITS_PER_WORD = "bits_per_word"
    CSHIGH = "cshigh"
    LOOP = "loop"
    NO_CS = "no_cs"
    LSB_FIRST = "lsbfirst"
    MODE = "mode"
    THREEWIRE = "threewire"
    READ0 = "read0"


# Wrapper class for spidev
class SPICom():
    state : com_state = com_state.IDLE

    def __init__(self, dev : int, bus : int, spidev ) -> None:
        self.dev = dev
        self.bus = bus
        self.spidev = spidev

    def openConnection(self) -> None:
        if self.dev == None: raise ValueError(self.dev)
        if self.bus == None: raise ValueError(self.bus)
        try:
            self.spidev.open(self.bus, self.dev)
        except Exception as e:
            print(e)
            self.state = com_state.ERROR        
        self.state = com_state.CONNECTED

    def closeConnection(self) -> None:
        if self.state != com_state.CONNECTED: raise RuntimeError("Please connect before disconnecting")
        self.spidev.close()
        self.state = com_state.DISCONNECTED

    def Write(self, list : list[bytes]) -> None:
        if self.state != com_state.CONNECTED: raise RuntimeError("Please connect before writting to bus")
        self.spidev.writebytes2(list)

    def ReadBuffer(self) -> bytes:
        if self.state != com_state.CONNECTED: raise RuntimeError("Please connect before reading from bus")
        return bytes(9999)

    def setup(self, **kwargs)->None:
        """Possible values:
                    "max_speed_hz"  : int
                    "bits_per_word" : unknown
                    "cshigh"        : bool
                    "loop"          : bool 
                    "no_cs"         : bool
                    "lsbfirst"      : bool
                    "mode"          : byte eg. (0b01)
                    "threewire"     : Unknown
                    "read0"         : bool
        """
        for key , item in kwargs.items():
            if key == spi_settings.MAX_SPEED_HZ:
                self.spidev.max_speed_hz = item
            elif key == spi_settings.MODE:
                self.spidev.mode = item
            elif key == spi_settings.BITS_PER_WORD:
                self.spidev.bits_per_word = item
            elif key == spi_settings.CSHIGH:
                self.spidev.cshigh = item
            elif key == spi_settings.LOOP:
                self.spidev.loop = item
            elif key == spi_settings.NO_CS:
                self.spidev.no_cs = item
            elif key == spi_settings.LSB_FIRST:
                self.spidev.lsbfirst = item
            elif key == spi_settings.THREEWIRE:
                self.spidev.threewire = item
            elif key == spi_settings.READ0:
                self.spidev.read0 = item
            else:
                raise Exception(f"unknown setting {key}:{item}")
            

