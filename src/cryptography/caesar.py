from .simple_substitution import SimpleSubstitutionCipher


class CaesarCipher(SimpleSubstitutionCipher):
    def __init__(self, key: int):
        alphabet_values = list(range(97, 97+26))
        key_dict = {chr(i): chr(97 + (i - 97 + key) % 26) for i in alphabet_values}
        super(CaesarCipher, self).__init__(key_dict)
