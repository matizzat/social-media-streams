from constant_protocol import ConstantProtocol
from predicate import Predicate

from typing import Tuple



class Atom:


    def __init__(self, predicate: Predicate, constants: Tuple[ConstantProtocol]): 

        self._number_of_constants = len(constants)  

        self._predicate = predicate 
        self._constants = constants  

    
    def has_as_predicate(self, predicate: Predicate) -> bool: 

        return self._predicate.is_equal_to(predicate) 

   
    def has_as_constants(self, constants: Tuple[ConstantProtocol]) -> bool: 
       
        if self._number_of_constants != len(constants):
            return False

        for i in range(self._number_of_constants):
            
            if not self._constants[i].is_equal_to(constants[i]):
                return False 
        
        return True 


    def is_equal_to(self, atom: "Atom") -> bool:  

        if not atom.has_as_predicate(self._predicate):
            return False 
    
        if not atom.has_as_constants(self._constants):
            return False 

        return True
