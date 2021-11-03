import unittest
import random

from src.cryptography import SimpleSubstitutionCipher


class TestSimpleSubstitution(unittest.TestCase):
    def test_with_caesar_key(self):
        alphabet_values = list(range(97, 97+26))
        key = {chr(i): chr(i+1) for i in alphabet_values}
        cipher = SimpleSubstitutionCipher(key)
        expected_code = "BCDEFG"
        message = "abcdef"
        coded_message = cipher.encrypt(message)
        assert coded_message == expected_code

        decoded_messaage = cipher.decrypt(coded_message)
        expected_message = message
        assert decoded_messaage == expected_message

    def test_with_random_key(self):
        alphabet_values = list(range(97, 97+26))
        shuffled_alphabet_values = random.sample(alphabet_values, len(alphabet_values))
        key = {chr(i): chr(j) for i, j in zip(alphabet_values, shuffled_alphabet_values)}
        cipher = SimpleSubstitutionCipher(key)
        message = "abcdef"
        expected_code = "".join(key[char] for char in message).upper()
        coded_message = cipher.encrypt(message)
        assert coded_message == expected_code

        decoded_messaage = cipher.decrypt(coded_message)
        expected_message = message
        assert decoded_messaage == expected_message

    def test_with_normal_sentence_and_random_key(self):
        alphabet_values = list(range(97, 97+26))
        shuffled_alphabet_values = random.sample(alphabet_values, len(alphabet_values))
        key = {chr(i): chr(j) for i, j in zip(alphabet_values, shuffled_alphabet_values)}
        cipher = SimpleSubstitutionCipher(key)
        message = "I want to eat pizza!"
        processed_message = "".join(filter(str.isalpha, message.lower()))
        expected_code = "".join(key[char] for char in processed_message).upper()
        coded_message = cipher.encrypt(message)
        assert coded_message == expected_code

        decoded_messaage = cipher.decrypt(coded_message)
        expected_message = "iwanttoeatpizza"
        assert decoded_messaage == expected_message