import abc


class BaseCipher(abc.ABC):
    def __init__(self, key):
        self.key = key

    def encrypt(self, message: str) -> str:
        raise NotImplementedError

    def decrypt(self, coded_message: str) -> str:
        raise NotImplementedError
