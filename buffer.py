
import dataclasses
import collections
from typing import Any, overload, Protocol


class none_value_exception(Exception):
    pass
class empty_fifo_exception(Exception):
    pass

class fifo_proto(Protocol):
    @overload
    def __init__(self) -> None:
        ...
    @overload
    def __init__(self, maxlen : int) -> None:
        ...
    def put(self, item : Any):
        ...
    def get(self)-> Any:
        ...
    def clear(self)->None:
        ...
    def len(self)-> int:
        ...

class fifo:
    @overload
    def __init__(self) -> None:
        self.que = collections.deque()
    @overload
    def __init__(self, maxlen : int) -> None:
        self.que = collections.deque(maxlen=maxlen)
    
    def put(self, item : Any)-> None:
        if item == None: raise Exception("Item in put is Empty")
        self.que.appendleft(item)

    def get(self)->Any:
        self.__is_fifo_empty()
        return self.que.pop()
    
    def clear(self)->None:
        self.__is_fifo_empty()
        self.que.clear()

    def __is_fifo_empty(self):
        if self.que == None: raise Exception("Fifo empty")

@dataclasses.dataclass
class combuffer:
    in_buffer  = fifo_proto()
    out_buffer = fifo_proto()