import unittest
import string_utils


class TestStringUtils(unittest.TestCase):

    def test_str_len(self):
        test_cases = [
            (7, "roberto"),
            (4, "yoda")
        ]
        for expected, word in test_cases:
            with self.subTest(f"{word} -> {expected}"):
                self.assertEqual(expected, string_utils.str_len(word))

    def test_first_char(self):
        test_cases = [
            ("r", "roberto"),
            ("y", "yoda")
        ]
        for expected, word in test_cases:
            with self.subTest(f"{word} -> {expected}"):
                self.assertEqual(expected, string_utils.first_char(word))

    def test_last_char(self):
        test_cases = [
            ("o", "roberto"),
            ("a", "yoda")
        ]
        for expected, word in test_cases:
            with self.subTest(f"{expected} -> {word}"):
                self.assertEqual(expected, string_utils.last_char(word))

    def test_input_has_substring(self):
        test_cases = [
            ("Roberto", "Rob", True),
            ("Yoda", "Dark", False)
        ]
        for word, substring, expected in test_cases:
            with self.subTest(f"{word}, {substring} -> {expected}"):
                self.assertEqual(expected, string_utils.input_has_substring(word, substring))

    def test_substring(self):
        test_cases = [
            ("roberto", 0, 3, "rob"),
            ("yoda", 2, 4, "da")
        ]
        for str_in, start, stop, expected in test_cases:
            with self.subTest(f"{str_in}, {start}, {stop} -> {expected}"):
                self.assertEqual(expected, string_utils.substring(str_in, start, stop))

    def test_opposite_case(self):
        test_cases = [
            ("Rob", "rOB"),
            ("yoda", "YODA")
        ]
        for str_in, str_out in test_cases:
            with self.subTest(f"{str_in} -> {str_out}"):
                self.assertEqual(str_out, string_utils.opposite_case(str_in))


if __name__ == '__main__':
    unittest.main()
