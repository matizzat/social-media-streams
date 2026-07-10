from constant_protocol import ConstantProtocol



class Predicate(ConstantProtocol):


    def __init__(self, name: str):  

        self._name = name 


    def has_name(self, name: str) -> bool:
        
        return self._name == name 


    def is_equal_to(self, other: "Predicate") -> bool: 

        return other.has_name(self._name)

