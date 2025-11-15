# automata_analyzer.py

import json

def parse_automaton(automaton_definition):
    """
    Parses an automaton definition from a JSON string or dictionary.
    
    Args:
        automaton_definition (str or dict): The automaton definition in JSON format or as a dictionary.
        
    Returns:
        dict: Parsed automaton components including states, alphabet, transitions, start state, and accept states.
    """
    if isinstance(automaton_definition, str):
        automaton_definition = json.loads(automaton_definition)
    
    required_keys = ['states', 'alphabet', 'transitions', 'start_state', 'accept_states']
    for key in required_keys:
        if key not in automaton_definition:
            raise ValueError(f"Missing required key: {key}")
    
    return automaton_definition

def classify_automaton(automaton):
    """
    Classifies the given automaton according to the Chomsky hierarchy.
    
    Args:
        automaton (dict): The parsed automaton definition.
        
    Returns:
        str: The type of the automaton (Type 0, 1, 2, or 3).
    """
    if 'transitions' not in automaton:
        raise ValueError("Automaton must have transitions to classify.")
    
    # Example classification logic (to be expanded)
    if is_finite_automaton(automaton):
        return "Type 3: Regular"
    elif is_pushdown_automaton(automaton):
        return "Type 2: Context-Free"
    elif is_linear_bounded_automaton(automaton):
        return "Type 1: Context-Sensitive"
    else:
        return "Type 0: Recursively Enumerable"

def is_finite_automaton(automaton):
    # Placeholder for actual logic to determine if the automaton is finite
    return True

def is_pushdown_automaton(automaton):
    # Placeholder for actual logic to determine if the automaton is a pushdown automaton
    return False

def is_linear_bounded_automaton(automaton):
    # Placeholder for actual logic to determine if the automaton is linear bounded
    return False

def analyze_automaton(automaton_definition):
    """
    Analyzes the automaton and classifies it.
    
    Args:
        automaton_definition (str or dict): The automaton definition in JSON format or as a dictionary.
        
    Returns:
        dict: Analysis result containing the classification and the automaton details.
    """
    automaton = parse_automaton(automaton_definition)
    classification = classify_automaton(automaton)
    
    return {
        "classification": classification,
        "automaton": automaton
    }