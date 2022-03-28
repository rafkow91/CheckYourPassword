from hashlib import sha1
from abstractive_classes import Validator

URL_ADDRESS = 'https://api.pwnedpasswords.com/range/'


class HashPassword(Validator):
    def __init__(self, password) -> None:
        self.password = password
        self.hashed_password = None

    def hash_password(self):
        hashed_password = sha1(self.password.encode())
        self.hashed_password = hashed_password.hexdigest()
        return self.hashed_password

    def validate(self):
        try:
            len(self.hashed_password)
        except TypeError:
            self.hash_password()

        return len(self.hashed_password) == 40
