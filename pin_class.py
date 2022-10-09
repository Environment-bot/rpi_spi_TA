
from pinDataClass import PinData, outputMode



class pin_class:

    def __init__(self, pinData : PinData) -> None:
        self._pindata : PinData = pinData
    
    def getPinData(self)->PinData:
        return self._pindata

    def setPinData(self, pin : int, mode : outputMode, info : str =""):
        self._pindata.pin = pin
        self._pindata.mode = mode
        self._pindata.info = info


