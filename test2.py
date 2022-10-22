
import dataclasses
import datetime
import types


@dataclasses.dataclass
class data_format:
    data : bytes
    timestamp : datetime.datetime

def test_list()-> None:
    lista : list[data_format] = []
    for i in range(0,6):
        data = data_format(data=bytes(f"0x00{i}"),timestamp=None)
        
        lista.append(data)

def main()-> None:
    test_list()

if __name__ == "__main__":
    main()