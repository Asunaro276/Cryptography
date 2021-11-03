from typing import Dict

from .cipher_base import BaseCipher


class SimpleSubstitutionCipher(BaseCipher):
    def __init__(self, key: Dict):
        super(SimpleSubstitutionCipher, self).__init__(key)
        self.swapped_key = {v: k for k, v in key.items()}

    def encrypt(self, message: str) -> str:
        message_list = list(filter(str.isalpha, message.lower()))
        coded_message_list = []
        for char in message_list:
            coded_char = self.key[char]
            coded_message_list.append(coded_char)
        coded_message = "".join(coded_message_list).upper()
        return coded_message

    def decrypt(self, coded_message: str) -> str:
        coded_message_list = list(filter(str.isalpha, coded_message.lower()))
        decoded_message_list = []
        for char in coded_message_list:
            decoded_char = self.swapped_key[char]
            decoded_message_list.append(decoded_char)
        decoded_message = "".join(decoded_message_list)
        return decoded_message

