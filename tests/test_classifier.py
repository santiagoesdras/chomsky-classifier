import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from grammar_parser import GrammarParser
from classifier import ChomskyClassifier

class TestClassifier(unittest.TestCase):

    def test_regular_grammar_type3(self):
        """Test Type 3 Regular Grammar"""
        grammar = "S → aA\nA → b"
        parser = GrammarParser()
        parser.parse_grammar(grammar)
        classifier = ChomskyClassifier(parser.productions)
        result = classifier.classify()
        self.assertEqual(result['type'], 3)

    def test_context_free_grammar_type2(self):
        """Test Type 2 Context-Free Grammar"""
        grammar = "S → aSb | ab"
        parser = GrammarParser()
        parser.parse_grammar(grammar)
        classifier = ChomskyClassifier(parser.productions)
        result = classifier.classify()
        self.assertEqual(result['type'], 2)

    def test_context_sensitive_grammar_type1(self):
        """Test Type 1 Context-Sensitive Grammar"""
        grammar = "S → aAbc | abc\nAb → bA"
        parser = GrammarParser()
        parser.parse_grammar(grammar)
        classifier = ChomskyClassifier(parser.productions)
        result = classifier.classify()
        self.assertIn(result['type'], [0, 1])  # Puede ser ambos

    def test_empty_grammar(self):
        """Test empty grammar handling"""
        grammar = ""
        parser = GrammarParser()
        parser.parse_grammar(grammar)
        valid, errors = parser.validate_grammar()
        self.assertFalse(valid)

if __name__ == '__main__':
    unittest.main()