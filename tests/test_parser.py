import unittest
from src.grammar_parser import GrammarParser

class TestGrammarParser(unittest.TestCase):

    def setUp(self):
        self.parser = GrammarParser()

    def test_valid_bnf(self):
        bnf_input = "S -> aA | b\nA -> b"
        result = self.parser.parse(bnf_input)
        self.assertTrue(result)

    def test_invalid_bnf_missing_arrow(self):
        bnf_input = "S aA | b\nA -> b"
        with self.assertRaises(ValueError):
            self.parser.parse(bnf_input)

    def test_invalid_bnf_empty_production(self):
        bnf_input = "S -> \nA -> b"
        with self.assertRaises(ValueError):
            self.parser.parse(bnf_input)

    def test_valid_bnf_multiple_rules(self):
        bnf_input = "S -> aA | b\nA -> b | aS"
        result = self.parser.parse(bnf_input)
        self.assertTrue(result)

    def test_invalid_bnf_non_terminal_on_right(self):
        bnf_input = "S -> aA | b\nA -> a"
        result = self.parser.parse(bnf_input)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()