from social_media.classifier.discourse_element_classifier_protocol import DiscourseElementClassifierProtocol
from social_media.classifier.classification_diagnostic_data import ClassificationDiagnosticData 
from social_media.domain.discourse_element import DiscourseElement
from social_media.domain.user import User 

from social_media.laser.stream.teststream import TestStream
from social_media.laser.evalunit.program import Program

from typing import List, Tuple, Dict

import datetime as dt


"""This is not the most polished implementation in the world!"""

class IncrementalReasoner:


    def __init__(self, reference_date: dt.datetime, classifier: DiscourseElementClassifierProtocol, win_size: int):

        self._reference_date = reference_date  
        self._classifier = classifier
        
        self._positive_classifications: List = []
        self._evaluation_function: Dict = {} 
        self._number_of_positives: int = 0

        self._rules = ["alarm(X, Y, Z) :- time_win(" + str(win_size) + ", 0, 1, @(T1,depressed(X, Y))) and time_win(" + str(win_size) + ", 0, 1, @(T2,depressed(X, Z))) and COMP(<, T1, T2)"]


    def interpret_discourse_element(self, discourse_element: DiscourseElement): 
        
        diagnostic_data = self._classifier.classify(discourse_element) 

        if(diagnostic_data.is_a_positive_classification()): 

            atom = "depressed(" + discourse_element.get_sender_id() + ", " + str(self._number_of_positives) + ")"
            scaled_time_instant = discourse_element.get_span_of_days_from_reference_date(self._reference_date) 

            if(scaled_time_instant not in self._evaluation_function):
                self._evaluation_function[scaled_time_instant] = [atom]  

            else:
                self._evaluation_function[scaled_time_instant].append(atom) 
            
            self._positive_classifications.append(diagnostic_data)
            self._number_of_positives += 1


    def get_alarming_users(self, date: dt.datetime) -> List[Tuple[User, List[ClassificationDiagnosticData]]]: 
            
        delta: dt.timedelta = date - self._reference_date 
        scaled_time_instant = delta.days

        _temp = {} 
        for i in range(scaled_time_instant+1):

            if i not in self._evaluation_function: 
                _temp[i] = []

            else: 
                _temp[i] = self._evaluation_function[i] 

        stream = TestStream(_temp, 0, scaled_time_instant) 

        program = Program(self._rules, stream)     
        for i in range(scaled_time_instant):
            program.evaluate(i) 

        result_list = [] 
        results_found, laser_result_set = program.evaluate(scaled_time_instant)

        if results_found == False:
            return [] 

        for atom in laser_result_set[scaled_time_instant]:
            pred, args = atom[:-1].split("(")
       
            constants = [] 
            for arg in args.split(","):
                constants.append(arg)
      
            result = (User(constants[0]), [
                self._positive_classifications[int(constants[1])],
                self._positive_classifications[int(constants[2])]]) 

            result_list.append(result) 

        return result_list 


    def get_evaluation_function(self) -> Dict:

        return self._evaluation_function
