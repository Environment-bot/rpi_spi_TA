import queue
import dataclasses

@dataclasses.dataclass
class combuffer:
    in_buffer  = queue.Queue()
    out_buffer = queue.Queue()

    

