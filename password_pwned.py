"""Checking if password was leaked"""
from hashlib import sha1
from requests import get

from abstractive_classes import Validator


class PwnedPassword(Validator):
    """_summary_

    Args:
        Validator (_type_): _description_

    Returns:
        _type_: _description_
    """
    URL_ADDRESS = 'https://api.pwnedpasswords.com/range/'

    def __init__(self, password: str = None) -> None:
        self.password = password
        self.hashed_pass = sha1(self.password.encode()).hexdigest()

        self._get_control_data()

    def __str__(self) -> str:
        return f'{self.password} -> {self.hashed_pass}'

    def _get_control_data(self) -> dict:
        url = PwnedPassword.URL_ADDRESS+self.hashed_pass[:5]
        with get(url) as content:
            content = content.text.split('\r\n')
        control_data = [line.split(':') for line in content]
        self.control_data = {}
        for item in control_data:
            self.control_data[item[0]] = int(item[1])

    def count_leaks(self) -> int:
        """Count how many password leaks"""
        try:
            return int(self.control_data.get(self.hashed_pass[5:].upper(), 0))
        except AttributeError:
            return None

    def validate(self) -> bool:
        return self.count_leaks() <= 0 if self.control_data is not None else None
