from typing import List, Tuple, Dict
import re

class Production:
    """Representa una producción gramatical"""
    def __init__(self, left: str, right: str):
        self.left = left.strip()
        self.right = right.strip()
    
    def __str__(self):
        return f"{self.left} → {self.right}"
    
    def __repr__(self):
        return f"Production('{self.left}', '{self.right}')"

class GrammarParser:
    """Parser para gramáticas en notación BNF"""
    
    def __init__(self):
        self.productions: List[Production] = []
        self.terminals = set()
        self.non_terminals = set()
    
    def parse_grammar(self, grammar_text: str):
        """Parsear texto de gramática"""
        self.productions = []
        self.terminals = set()
        self.non_terminals = set()
        
        lines = grammar_text.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Soportar → y ->
            if '→' in line:
                parts = line.split('→')
            elif '->' in line:
                parts = line.split('->')
            else:
                continue
            
            if len(parts) != 2:
                continue
            
            left = parts[0].strip()
            right_part = parts[1].strip()
            
            # Procesar alternativas (|)
            alternatives = right_part.split('|')
            
            for alt in alternatives:
                alt = alt.strip()
                prod = Production(left, alt)
                self.productions.append(prod)
                
                # Extraer terminales y no-terminales
                self.non_terminals.add(left)
                
                # Identificar símbolos en el lado derecho
                for char in alt:
                    if char.isupper() or char == '_':
                        # Es parte de un no-terminal
                        pass
                    elif char not in ' |()[]{}':
                        self.terminals.add(char)
    
    def validate_grammar(self) -> Tuple[bool, List[str]]:
        """Validar que la gramática sea válida"""
        errors = []
        
        if not self.productions:
            errors.append("No hay producciones definidas")
            return False, errors
        
        # Verificar que el símbolo inicial existe
        if 'S' not in self.non_terminals and not self.non_terminals:
            errors.append("Falta el símbolo inicial S")
        
        # Verificar que cada producción tiene izquierda y derecha
        for prod in self.productions:
            if not prod.left:
                errors.append(f"Producción sin lado izquierdo: {prod}")
            if not prod.right:
                errors.append(f"Producción sin lado derecho: {prod}")
        
        return len(errors) == 0, errors