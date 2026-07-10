from social_media.classifier.discourse_element_classifier_protocol import DiscourseElementClassifierProtocol 
from social_media.classifier.classification_diagnostic_data import ClassificationDiagnosticData 
from social_media.classifier.classifier_codomain import ClassifierCodomain 
from social_media.domain.discourse_element import DiscourseElement

from llms_kgs.llms import LLMProtocol



class DiscourseElementClassifier(DiscourseElementClassifierProtocol):


    def __init__(self, llm: LLMProtocol, system_template: str):
       
        self._system_prompt = system_template.format(schema = ClassifierCodomain.model_json_schema())
        self._llm = llm


    def classify(self, discourse_element: DiscourseElement) -> ClassificationDiagnosticData:
        
        llm_invocation_data = self._llm.call(system = self._system_prompt, prompt = discourse_element.get_content())  
        classifier_result = ClassifierCodomain.model_validate_json(llm_invocation_data.raw_answer)

        return ClassificationDiagnosticData(discourse_element=discourse_element,
                llm_invocation_data=llm_invocation_data, classifier_result=classifier_result)     
