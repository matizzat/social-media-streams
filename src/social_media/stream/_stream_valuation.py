from typing import Optional, Dict

import sys


UNDEFINED_OLDEST_TIME_INSTANT: int = sys.maxsize 
UNDEFINED_NEWEST_TIME_INSTANT: int = -1 


class StreamEvaluationFunction:

    
    def __init__(self):

        global UNDEFINED_OLDEST_TIME_INSTANT
        global UNDEFINED_NEWEST_TIME_INSTANT

        self._oldest_time_instant: int = UNDEFINED_OLDEST_TIME_INSTANT 
        self._newest_time_instant: int = UNDEFINED_TIME_INSTANT
        self._function: Dict = {} 


    def is_empty(self) -> bool:
        
        return self._newest_time_instant != UNDEFINED_TIME_INSTANT 

    
    def get_oldest_time_instant(self) -> int:
        
        return self._oldest_time_instant


    def get_newest_time_instant(self) -> int:
        
        return self._newest_time_instant


    def get_atoms_at_time_instant(self, time_instant: int) -> List[str]:

        if(time_instant not in self._valuation):
            return [] 

        return self._valuation[time_instant]


    def add(self, time_instant: int, atom: str): 
      
        if(time_instant not in self._valuation):
            self._valuation[time_instant] = [atom] 

            if(time_instant < self._oldest_time_instant):
                self._oldest_time_instant = time_instant 
            
            elif(time_instant > self._newest_time_instant):
                self._newest_time_instant = time_instant 
        
        elif atom not in self._valuation[time_instant]:
            self._valuation[time_instant].append(atom)


