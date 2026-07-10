from social_media.domain.discourse_element import DiscourseElement 
from social_media.domain.user import User  

from operator import attrgetter
from typing import List

import datetime as dt 
import json
import os 

class DiscourseElementProvider:

    @staticmethod
    def transform_dataset_to_discourse_element_list(dataset_path: str) -> List[DiscourseElement]:
      
        discourse_elements = [] 

        for filename in os.listdir(dataset_path):
            
            if filename.startswith("subject_"):
            
                with open(dataset_path + '/' + filename, 'r') as f:
                    discussions = json.load(f)

                for discussion in discussions:
                    
                    submission = discussion['submission']
                    comments = discussion['comments'] 

                    submission_discourse_element = DiscourseElement(
                            creation_date = dt.datetime.fromisoformat(submission['created_utc'][0:10]),
                            content = submission['title'] + '\n' + submission['body'],  
                            discourse_id = submission['submission_id'],
                            sender = User(submission['user_id']),
                            answers_to = None)

                    discourse_elements.append(submission_discourse_element)
                    

                    for comment in comments:
                        
                        comment_discourse_element = DiscourseElement(
                            creation_date = dt.datetime.fromisoformat(comment['created_utc'][0:10]),
                            content = comment['body'],  
                            discourse_id = comment['comment_id'],
                            sender = User(comment['user_id']),
                            answers_to = None)
                        
                        discourse_elements.append(comment_discourse_element)

        return sorted(discourse_elements, key=attrgetter("_creation_date"))
