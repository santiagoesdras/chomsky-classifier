from typing import List, Dict
from grammar_parser import Production
import re

class ChomskyClassifier:
    
    def __init__(self, productions: List[Production]):
        self.productions = productions
    
    def classify(self) -> Dict:
        
        if self._is_type_3():
            return {
                'type': 3,
                'name': 'TIPO 3 - Regular',
                'justification': self._get_type3_justification()
            }
        elif self._is_type_2():
            return {
                'type': 2,
                'name': 'TIPO 2 - Libre de Contexto',
                'justification': self._get_type2_justification()
            }
        elif self._is_type_1():
            return {
                'type': 1,
                'name': 'TIPO 1 - Sensible al Contexto',
                'justification': self._get_type1_justification()
            }
        else:
            return {
                'type': 0,
                'name': 'TIPO 0 - Recursivamente Enumerable',
                'justification': self._get_type0_justification()
            }
    
    def _is_type_3(self) -> bool:
        for prod in self.productions:
            right = prod.right
            
            non_terminal_count = sum(1 for c in right if c.isupper())
            
            if non_terminal_count > 1:
                return False
            
            if non_terminal_count == 1:
                nt_pos = None
                for i, c in enumerate(right):
                    if c.isupper():
                        nt_pos = i
                        break
                
                if nt_pos not in [0, len(right) - 1]:
                    return False
        
        return True
    
    def _is_type_2(self) -> bool:
        for prod in self.productions:
            if len(prod.left) != 1 or not prod.left.isupper():
                return False
        
        return True
    
    def _is_type_1(self) -> bool:
        for prod in self.productions:
            if len(prod.left) > len(prod.right) and prod.right != 'ε':
                return False
        
        return True
    
    def _get_type3_justification(self) -> List[str]:
        return [
            "Todas las producciones son lineales (un no-terminal al inicio o final)",
            "Puede ser reconocida por un Autómata Finito Determinista (AFD)",
            "Es un subconjunto del Tipo 2 (Libre de Contexto)"
        ]
    
    def _get_type2_justification(self) -> List[str]:
        return [
            "Lado izquierdo: exactamente un símbolo no-terminal",
            "No es Tipo 3 (tiene producciones no-lineales)",
            "Puede ser reconocida por un Autómata con Pila (AP)"
        ]
    
    def _get_type1_justification(self) -> List[str]:
        return [
            "Satisface la restricción: |lado izquierdo| <= |lado derecho|",
            "No es Tipo 2 (lado izquierdo tiene múltiples símbolos)",
            "Puede ser reconocida por Máquina Turing Lineal Acotada (MTLA)"
        ]
    
    def _get_type0_justification(self) -> List[str]:
        return [
            "No satisface restricciones de Tipo 1-3",
            "Puede tener producciones sin restricción",
            "Solo es reconocible por Máquina de Turing"
        ]