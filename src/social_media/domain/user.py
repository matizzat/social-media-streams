from social_media.stream.constant_protocol import ConstantProtocol 


class User(ConstantProtocol):


    def __init__(self, user_id: str):

        self._id = user_id


    def has_id(self, user_id: str) -> bool:

        return self._id == user_id


    def is_equal_to(self, user: "User") -> bool:

        return user.has_id(self._id)


    def get_id(self) -> str:

        return self._id 
