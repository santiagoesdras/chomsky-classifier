from typing import List
from grammar_parser import Production

class Explainer:
    
    def __init__(self, productions: List[Production], grammar_type: int):
        self.productions = productions
        self.grammar_type = grammar_type
    
    def generate_detailed_explanation(self) -> str:
        
        explanation = f"{'='*60}\n"
        explanation += f"ANÁLISIS DETALLADO DE GRAMÁTICA - TIPO {self.grammar_type}\n"
        explanation += f"{'='*60}\n\n"
        
        explanation += "PRODUCCIONES:\n"
        for i, prod in enumerate(self.productions, 1):
            explanation += f"  {i}. {prod}\n"
        
        explanation += f"\n{'='*60}\n"
        explanation += "ANÁLISIS POR TIPO:\n"
        explanation += f"{'='*60}\n\n"
        
        if self.grammar_type == 3:
            explanation += self._explain_type3()
        elif self.grammar_type == 2:
            explanation += self._explain_type2()
        elif self.grammar_type == 1:
            explanation += self._explain_type1()
        else:
            explanation += self._explain_type0()
        
        return explanation
    
    def _explain_type3(self) -> str:
        return """
TIPO 3 - GRAMÁTICA REGULAR
──────────────────────────

Características:
* Producciones lineales: A → aB | a | ε
* Reconocida por: Autómata Finito (AFD/AFN)
* Complejidad: O(n) - lineal

Propiedades:
- Determinista
- Sin memoria
- Aplicaciones: Expresiones regulares, tokens

Ejemplo de Derivación:
S ⇒ aA ⇒ ab

Lenguajes Expresables:
- Patrones simples: a*b
- Identificadores: [a-zA-Z][a-zA-Z0-9]*
- Números: [0-9]+
"""
    
    def _explain_type2(self) -> str:
        return """
TIPO 2 - GRAMÁTICA LIBRE DE CONTEXTO
─────────────────────────────────────

Características:
* Un no-terminal en lado izquierdo: A → β
* Reconocida por: Autómata con Pila (AP)
* Complejidad: O(n^3) - cúbica (CYK)

Propiedades:
- Con memoria (pila)
- Balanceo de símbolos
- Aplicaciones: Lenguajes de programación

Ejemplo de Derivación:
S ⇒ aSb ⇒ aaSbb ⇒ aaabbb

Lenguajes Expresables:
- Paréntesis balanceados: ()
- Expresiones aritméticas: a + b * c
- Estructura de programas
"""
    
    def _explain_type1(self) -> str:
        return """
TIPO 1 - GRAMÁTICA SENSIBLE AL CONTEXTO
────────────────────────────────────────

Características:
* Restricción: |lado izquierdo| <= |lado derecho|
* Reconocida por: Máquina Turing Lineal Acotada (MTLA)
* Complejidad: PSPACE

Propiedades:
- Dependencia del contexto
- Mayor poder expresivo
- Aplicaciones: Algunos lenguajes naturales

Ejemplo de Restricción:
S → aAbc | abc      (1 <= 4, 1 <= 3)
Ab → bA             (2 <= 2)

Lenguajes Expresables:
- a^n b^n c^n (aproximación)
- Dependencias contextuales
"""
    
    def _explain_type0(self) -> str:
        return """
TIPO 0 - GRAMÁTICA RECURSIVAMENTE ENUMERABLE
──────────────────────────────────────────────

Características:
* Sin restricciones
* Reconocida por: Máquina de Turing
* Complejidad: Indecidible (Problema del Halting)

Propiedades:
- Poder computacional máximo
- Puede no terminar
- Aplicaciones: Problemas teóricos

Ejemplo:
S → AB
AB → BA            (Reescritura sin restricción)

Lenguajes Expresables:
- Todos los lenguajes recursivamente enumerables
- Problemas computables y no-computables
"""