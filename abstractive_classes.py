"""Package for all abstract classes"""
from abc import ABC, abstractmethod


class Validator(ABC):
    """Abstract class of validator"""
    @abstractmethod
    def validate(self) -> bool:
        """Abstact method to validate class and return boolean value"""
