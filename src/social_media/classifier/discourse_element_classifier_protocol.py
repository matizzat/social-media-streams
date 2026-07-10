from social_media.classifier.classification_diagnostic_data import ClassificationDiagnosticData
from social_media.domain.discourse_element import DiscourseElement
from typing import Protocol

class DiscourseElementClassifierProtocol(Protocol): 

    def classify(self, discourse_element: DiscourseElement) -> ClassificationDiagnosticData: 
        ... 
