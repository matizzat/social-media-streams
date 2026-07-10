from pydantic import BaseModel

class ClassifierCodomain(BaseModel):

    explanation: str
    classification: bool
