from hashlib import sha1

from abstractive_classes import Validator

URL_ADDRESS = 'https://api.pwnedpasswords.com/range/'

class PwnedPassword(Validator):
    def __init__(self, password: str = None, control_data: dict = None) -> None:
        self.password = password
        self.control_data = control_data
        self.hashed_pass = sha1(self.password.encode()).hexdigest()
        self.hashed_pass = self.hashed_pass.hash_password()

    def __str__(self) -> str:
        return f'{self.password} -> {self.hashed_pass}'

    def validate(self) -> bool:
        return self._check() == 0 if self.control_data != None else None

    def _check(self) -> list:
        try:
            return int(self.control_data.get(self.hashed_pass, 0))
        except AttributeError:
            return None
    