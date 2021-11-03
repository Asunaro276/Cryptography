import unittest

from src.cryptanalysis import CaesarAnalyzer
from src.cryptography import CaesarCipher


class TestCaesar(unittest.TestCase):
    def test_in_slide_1(self):
        key = 1
        cipher = CaesarCipher(key)
        message = "abcdef"
        coded_message = cipher.encrypt(message)
        expected_messaage = cipher.decrypt(coded_message)

        analyzer = CaesarAnalyzer()
        analyzed_message = analyzer.brute_force(coded_message)
        assert expected_messaage in analyzed_message

    def test_slide_26(self):
        key = 26
        cipher = CaesarCipher(key)
        message = "abcdef"
        coded_message = cipher.encrypt(message)
        expected_messaage = cipher.decrypt(coded_message)

        analyzer = CaesarAnalyzer()
        analyzed_message = analyzer.brute_force(coded_message)
        assert expected_messaage in analyzed_message

    def test_with_normal_sentence(self):
        key = 3
        cipher = CaesarCipher(key)
        message = "I want to eat pizza!"
        coded_message = cipher.encrypt(message)
        expected_messaage = cipher.decrypt(coded_message)

        analyzer = CaesarAnalyzer()
        analyzed_message = analyzer.brute_force(coded_message)
        assert expected_messaage in analyzed_message

