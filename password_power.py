"""Check if your password is strong."""
from abstractive_classes import Validator


class StrongPassword(Validator):
    """Checking password strong"""
    def __init__(self, password) -> None:
        self.password = password

    def _has_acceptable_length(self) -> bool:
        return len(self.password) >= 8

    def _has_number(self) -> bool:
        for letter in self.password:
            try:
                int(letter)
                return True
            except ValueError:
                continue

        return False

    def _has_special_sign(self) -> bool:
        for letter in self.password:
            if letter in '!@#$%^&*()_+=-`~/?.,<>':
                return True

        return False

    def _has_lower_and_higher_letter(self) -> bool:
        return self.password != self.password.lower() and self.password != self.password.upper()

    def validate(self) -> bool:
        """validate password"""
        return all([
            self._has_acceptable_length(),
            self._has_number(),
            self._has_special_sign(),
            self._has_lower_and_higher_letter()
        ])

    def check_strong(self) -> float:
        """returns percentage value"""
        checklist = [
            self._has_acceptable_length(),
            self._has_number(),
            self._has_special_sign(),
            self._has_lower_and_higher_letter()
        ]

        return round(sum(checklist)/len(checklist) * 100, 1)
