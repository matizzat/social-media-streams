from social_media.stream.constant_protocol import ConstantProtocol 
from social_media.domain.user import User
from typing import Optional

import datetime as dt



class DiscourseElement(ConstantProtocol): 


    def __init__(self,
            discourse_id: str,
            creation_date: dt.datetime,
            content: str,
            sender: User,
            answers_to: Optional["DiscourseElement"]):

        self._creation_date = creation_date
        self._discourse_id = discourse_id 
        self._answers_to = answers_to
        self._content = content  
        self._sender = sender

    
    def has_id(self, discourse_id: str) -> bool:

        return self._discourse_id == discourse_id 

    
    def is_equal_to(self, other: "DiscourseElement") -> bool:

        return other.has_id(self._discourse_id) 


    def get_span_of_days_from_reference_date(self, reference_date: dt.datetime):

        delta: dt.timedelta = self._creation_date - reference_date
        return delta.days 


    def get_content(self) -> str:

        return self._content 


    def get_sender_id(self) -> str:

        return self._sender.get_id() 
