def is_valid_bnf(grammar):
    # Check if the grammar is in valid BNF format
    # A valid BNF production should be of the form: <non-terminal> ::= <expression>
    for production in grammar:
        if '::=' not in production:
            return False
        left, right = production.split('::=', 1)
        if not left.strip().startswith('<') or not left.strip().endswith('>'):
            return False
    return True

def is_valid_automaton(automaton):
    # Validate the structure of the automaton
    # Check for required fields and correct format
    required_fields = ['states', 'alphabet', 'transitions', 'start_state', 'accept_states']
    for field in required_fields:
        if field not in automaton:
            return False
    return True

def validate_input(input_data, input_type):
    # Validate input data based on its type (grammar or automaton)
    if input_type == 'grammar':
        return is_valid_bnf(input_data)
    elif input_type == 'automaton':
        return is_valid_automaton(input_data)
    else:
        raise ValueError("Invalid input type. Expected 'grammar' or 'automaton'.")