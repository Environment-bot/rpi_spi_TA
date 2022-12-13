import com
import typing
import buffer


class dev(typing.Protocol):
    def __init__(self, com : com.Communication, **kwargs) -> None:
        ...
    def open(self) -> None:
        ...
    def close(self) -> None:
        ...
    def setup(self, **kwargs) -> None:
        ...
    def send(self, values : list[bytes]) -> None:
        ...
    def read(self) -> bool:
        ...


class spi_dev(com.SPICom):
    def __init__(self, dev: int, bus: int, spidev) -> None:
        super().__init__(dev, bus, spidev)
        self.fifo = buffer.fifo()

    def open(self): 
        super().openConnection()

    def send(self, values : list[bytes]):
        self.fifo.put(super().Write(values))

    def read(self, len : int) -> bool:
        self.fifo.put(super().ReadBuffer(len))

    def close(self):
        super().closeConnection()

    def setup(self, **kwargs):
        super().setup(kwargs=kwargs)


