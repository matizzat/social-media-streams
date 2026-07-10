from typing import Protocol



class ConstantProtocol(Protocol):


    def is_equal_to(self, other: "ConstantProtocol") -> bool:

        ... 
