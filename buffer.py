
from ast import Break
import dataclasses
import collections
from typing import Any, overload, Protocol


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
        if self.que == None: raise Exception("Fifo empty")
        return self.que.pop()


@dataclasses.dataclass
class combuffer:
    in_buffer  = fifo_proto()
    out_buffer = fifo_proto()