from social_media.classifier.discourse_element_classifier_protocol import DiscourseElementClassifierProtocol
from social_media.classifier.classification_diagnostic_data import ClassificationDiagnosticData 
from social_media.classifier.classifier_codomain import ClassifierCodomain 

from social_media.domain.discourse_element import DiscourseElement

from lorem_text import lorem 

import random



class MockClassifier(DiscourseElementClassifierProtocol): 


    def __init__(self, cutoff: float):

        self._cutoff = cutoff


    def classify(self, discourse_element: DiscourseElement) -> ClassificationDiagnosticData:

        classifier_result = ClassifierCodomain(explanation = lorem.sentence(), classification = random.random() < self._cutoff)

        return ClassificationDiagnosticData(discourse_element=discourse_element,
                llm_invocation_data=None, classifier_result=classifier_result)
