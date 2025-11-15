import unittest
from src.converters import regex_to_afd, afd_to_regex, afd_to_grammar, grammar_to_afd

class TestConverters(unittest.TestCase):

    def test_regex_to_afd(self):
        regex = "(a|b)*abb"
        expected_afd = {
            # Define the expected AFD structure here
        }
        result = regex_to_afd(regex)
        self.assertEqual(result, expected_afd)

    def test_afd_to_regex(self):
        afd = {
            # Define a sample AFD structure here
        }
        expected_regex = "(a|b)*abb"
        result = afd_to_regex(afd)
        self.assertEqual(result, expected_regex)

    def test_afd_to_grammar(self):
        afd = {
            # Define a sample AFD structure here
        }
        expected_grammar = "S → aA | bB\nA → b\nB → a"
        result = afd_to_grammar(afd)
        self.assertEqual(result, expected_grammar)

    def test_grammar_to_afd(self):
        grammar = "S → aA | bB\nA → b\nB → a"
        expected_afd = {
            # Define the expected AFD structure here
        }
        result = grammar_to_afd(grammar)
        self.assertEqual(result, expected_afd)

if __name__ == '__main__':
    unittest.main()