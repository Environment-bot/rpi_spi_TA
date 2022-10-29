import dataclasses
import datetime
from typing import List
from .. import com 
import pytest


REAL_SYSTEM_IN_USE : bool = False
TESTED_OBJ : com.Communication = None

@dataclasses.dataclass

class data_format:
    data : bytes
    timestamp : datetime.datetime



def test_com(testobj : com.Communication)-> None:
    pass

def test_write_to_buffer(testobj : com.Communication)-> None:
    pass

def test_read_from_buffer()->None:
    pass

def test_write()-> None:
    pass

def test_open_connection(testobj : com.Communication, sys : bool=False)->None:
    pass

def test_close_connection()->None:
    pass

def connect(testobj : com.Communication)-> None:
    pass

def close(testobj : com.Communication)-> None:
    pass

def dataprep()-> List[data_format]:
    lista : List[data_format] = []
    for i in range(0,6):
        lista.append(data_format.data, data_format.)
    lista.append("0x00F")
    return lista
