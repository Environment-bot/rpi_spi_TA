import sys
sys.path.append("C:\Code\RPI4-BlinkLed")
import buffer
from typing import List
import pytest



DATA : list[int] = [0,1,2,3,4,5,6,7,8,9,10]


class Testfifo_tests:
    
    # Common functions
    
    fifo : buffer.fifo_proto = None

    def create_fifo_without_maxlen(self) -> None:
        self.fifo =  buffer.fifo()
        
    def create_fifo_with_maxlen(self,maxlen : int) -> None:
        self.fifo = buffer.fifo(maxlen=maxlen)

    # ---------------------------    
    # Tests begins
    # ---------------------------  
    def test_fifo_put_with_empty_value(self)-> None:
        self.create_fifo_without_maxlen()
        with pytest.raises(buffer.none_value_exception):
            self.fifo.put(None)

    def test_fifo_clear_empty_fifo_exception(self)->None:
        self.create_fifo_without_maxlen()
        with pytest.raises(buffer.empty_fifo_exception):
            self.fifo.clear()

    def test_add_and_get(self)->None:
        self.create_fifo_without_maxlen()
        # insert data to fifo
        for item in DATA:
            self.fifo.put(item=item)
        # assert that data comes out as expected
        for index in range(0, 5):
            # print(index)
            assert self.fifo.get() == DATA[index]
        # insert data to fifo
        self.fifo.put(999)
        #check that data is still coming in order
        for index in range(5,11):
            assert self.fifo.get() == DATA[index]
        assert self.fifo.get() == 999
    def test_add_list_and_get(self)->None:
        self

    def test_add_list_of_stuff(self):
        self.create_fifo_without_maxlen()
        # insert data to fifo
        for item in DATA:
            self.fifo.put(item=item)
        # assert that data comes out as expected
        for index in range(0, 5):
            # print(index)
            assert self.fifo.get() == DATA[index]
        # insert data to fifo
        self.fifo.put(999)
        #check that data is still coming in order
        for index in range(5,11):
            assert self.fifo.get() == DATA[index]
        assert self.fifo.get() == 999
    def test_fifo_clear(self):
        #create empty fifo
        self.create_fifo_without_maxlen()
        #add items to it
        [self.fifo.put(data) for data in DATA]
        #check that there is data
        assert self.fifo.len() == len(DATA)
        #clear out fifo
        self.fifo.clear()
        assert self.fifo.len() == 0

    def test_fifo_get_from_empty_error_rise(self):
        #create empty fifo
        self.create_fifo_without_maxlen()
        #try to get value from empty fifo
        with pytest.raises(buffer.empty_fifo_exception):
            self.fifo.get()


# Runner
def main():
    pass

if __name__ == "__main__":
    main()