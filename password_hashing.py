from hashlib import sha1
from abstractive_classes import Validator




class HashPassword(Validator):
    def __init__(self, password: str, hashed_password: str = None) -> None:
        self.password = password
        self.hashed_password = hashed_password

    def hash_password(self):
        self.hashed_password = sha1(self.password.encode()).hexdigest()
        return self.hash_password

    def validate(self):
        try:
            len(self.hashed_password)
        except TypeError:
            self.hash_password()

        return len(self.hashed_password) == 40
