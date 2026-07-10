from social_media.classifier.classifier_codomain import ClassifierCodomain 
from social_media.domain.discourse_element import DiscourseElement
from llms_kgs.llms import LLMInvocationData

from dataclasses import asdict, dataclass, field
from typing import List, Optional



@dataclass
class ClassificationDiagnosticData:


    discourse_element: DiscourseElement = field(default_factory=DiscourseElement)
    llm_invocation_data: Optional[LLMInvocationData] = None  
    classifier_result: Optional[ClassifierCodomain] = None 


    def is_a_positive_classification(self) -> bool:

        if(self.classifier_result == None):
            return False

        return self.classifier_result.classification 

