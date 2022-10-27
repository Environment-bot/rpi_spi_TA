
from ctypes import sizeof
import dataclasses
import datetime
import sys
import types
import time
import collections


@dataclasses.dataclass
class data_format:
    data : bytes
    timestamp : float

def int_to_bytes(integer : int)->bytes:
    return integer.to_bytes(4, sys.byteorder)

def test_list()-> list[data_format]:
    lista : list[data_format] = []
    for i in range(0,100):
        data = data_format(data=int_to_bytes(i),timestamp=time.time_ns())        
        lista.append(data)
    return lista
    # print(lista)
    # print(lista[98].data.hex())
    # print(int.from_bytes(lista[98].data, byteorder=sys.byteorder,signed=True))

def fifo_test(lista : list[data_format] )->None:
    que : collections.deque[data_format] = collections.deque()
    #add data to queue
    [que.appendleft(data) for data in lista]
    print(que.count(int_to_bytes(6)))
    data = que.pop().data
    print(data)
    print(que.popleft())
    que.clear()
    





def main()-> None:
    asd =  test_list()
    fifo_test(lista=asd)

if __name__ == "__main__":
    main()