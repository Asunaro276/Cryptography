import unittest

from src.cryptography import CaesarCipher


class TestCaesar(unittest.TestCase):
    def test_in_slide_1(self):
        key = 1
        cipher = CaesarCipher(key)
        expected_code = "BCDEFG"
        message = "abcdef"
        coded_message = cipher.encrypt(message)
        assert coded_message == expected_code

        decoded_messaage = cipher.decrypt(coded_message)
        expected_message = message
        assert decoded_messaage == expected_message

    def test_slide_26(self):
        key = 26
        cipher = CaesarCipher(key)
        expected_code = "ABCDEF"
        message = "abcdef"
        coded_message = cipher.encrypt(message)
        assert coded_message == expected_code

        decoded_messaage = cipher.decrypt(coded_message)
        expected_message = message
        assert decoded_messaage == expected_message

    def test_with_normal_sentence(self):
        key = 3
        cipher = CaesarCipher(key)
        expected_code = "LZDQWWRHDWSLCCD"
        message = "I want to eat pizza!"
        coded_message = cipher.encrypt(message)
        assert coded_message == expected_code

        decoded_messaage = cipher.decrypt(coded_message)
        expected_message = "iwanttoeatpizza"
        assert decoded_messaage == expected_message
