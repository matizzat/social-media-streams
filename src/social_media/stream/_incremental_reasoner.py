from laser.evalunit.program import Program

from stream_valuation import StreamValuation
from typing import List, Set


class IncrementalReasoner:


    def __init__(self, rules: List, stream_valuation: StreamValuation):

        self._stream_valuation = stream_valuation
        self._rules = rules 


    def get_stream_valuation(self) -> StreamValuation: 

        return self._stream_valuation 


    def get_result_set_union(lower_bound: int, upper_bound: int) -> Set:
        
        result_set = set() 
        program = Program(self._rules, self._stream_valuation)  
        
        for i in range(self._stream_valuation.get_oldest_time(), lower_bound):
            program.evaluate(i)

        for i in range(lower_bound, upper_bound):
            result_set
            


        

            
