from typing import List


class CaesarAnalyzer:
    def brute_force(self, coded_message: str) -> List[str]:
        NUM_ALPHABET = 26
        coded_message_list = list(filter(str.isalpha, coded_message.lower()))
        all_analyzed_messages = []
        for num_slide in range(NUM_ALPHABET):
            analyzed_message_list = []
            for char in coded_message_list:
                char_value = ord(char)
                analyzed_char_value = (char_value % 97 + num_slide) % 26 + 97
                analyzed_char = chr(analyzed_char_value)
                analyzed_message_list.append(analyzed_char)
            analyzed_message = "".join(analyzed_message_list)
            all_analyzed_messages.append(analyzed_message)
        return all_analyzed_messages

