import collections
from typing import Any, overload, Protocol


class none_value_exception(Exception):
    pass
class empty_fifo_exception(Exception):
    pass

class fifo_proto(Protocol):
    @overload
    def __init__(self) -> None:
        """fifo has no max length"""
        ...
    @overload
    def __init__(self, maxlen : int) -> None:
        """adding max length for fifo"""
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
        """fifo has no max length"""
        ...
    @overload
    def __init__(self, maxlen : int) -> None:
        """adding max length for fifo"""
        ...

    def __init__(self, maxlen = None):
        if maxlen == None:
            self.que = collections.deque()
        else:
            self.que = collections.deque(maxlen=maxlen)    
        
    
    def put(self, item : Any)-> None:
        if item == None: raise none_value_exception("Item in put is Empty")
        self.que.appendleft(item)

    def get(self)->Any:
        self.__is_fifo_empty()
        return self.que.pop()
    
    def clear(self)->None:
        self.__is_fifo_empty()
        self.que.clear()

    def __is_fifo_empty(self):
        if not bool(self.que)  : raise empty_fifo_exception("Fifo empty")

    def len(self)->int:
        return len(self.que)

