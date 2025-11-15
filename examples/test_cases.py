import unittest
from src.grammar_parser import parse_grammar
from src.classifier import classify_grammar
from src.visualizer import visualize_grammar

class TestChomskyClassifierAI(unittest.TestCase):

    def test_regular_grammar(self):
        grammar = "S → aA | b\nA → a | b"
        parsed_grammar = parse_grammar(grammar)
        classification = classify_grammar(parsed_grammar)
        self.assertEqual(classification, "Tipo 3: Gramática Regular")
        visualize_grammar(parsed_grammar)

    def test_context_free_grammar(self):
        grammar = "S → aSb | ab"
        parsed_grammar = parse_grammar(grammar)
        classification = classify_grammar(parsed_grammar)
        self.assertEqual(classification, "Tipo 2: Gramática Libre de Contexto")
        visualize_grammar(parsed_grammar)

    def test_context_sensitive_grammar(self):
        grammar = "S → aAB\nA → a | b\nB → b"
        parsed_grammar = parse_grammar(grammar)
        classification = classify_grammar(parsed_grammar)
        self.assertEqual(classification, "Tipo 1: Gramática Sensible al Contexto")
        visualize_grammar(parsed_grammar)

    def test_recursively_enumerable_grammar(self):
        grammar = "S → aS | bS | ε"
        parsed_grammar = parse_grammar(grammar)
        classification = classify_grammar(parsed_grammar)
        self.assertEqual(classification, "Tipo 0: Gramática Recursivamente Enumerable")
        visualize_grammar(parsed_grammar)

if __name__ == '__main__':
    unittest.main()