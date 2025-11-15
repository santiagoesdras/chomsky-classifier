import os
from typing import List
from grammar_parser import Production
import re

class GrammarVisualizer:
    def __init__(self, output_dir=None):
        if output_dir is None:
            output_dir = os.path.join(os.getcwd(), 'output', 'diagrams')
        
        self.output_dir = output_dir
        
        # Crear directorio si no existe
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)
        except Exception as e:
            print(f"Warning: Could not create directory {output_dir}: {e}")
            # Usar directorio temporal como fallback
            self.output_dir = os.path.join(os.getcwd(), 'temp_diagrams')
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir, exist_ok=True)
    
    def create_production_graph(self, productions: List[Production], filename='production_graph'):
        """Create text-based graph of productions"""
        try:
            import graphviz
            dot = graphviz.Digraph(filename=filename, directory=self.output_dir, format='png')
            dot.attr(rankdir='LR')
            dot.attr('node', shape='box', style='filled', fillcolor='lightblue')
            
            non_terminals = set()
            for prod in productions:
                non_terminals.add(prod.left)
            
            for nt in non_terminals:
                dot.node(nt, nt)
            
            for prod in productions:
                for match in re.finditer(r'[A-Z_][a-zA-Z0-9_]*', prod.right):
                    nt = match.group()
                    if nt in non_terminals and nt != prod.left:
                        label = prod.right[:15] + "..." if len(prod.right) > 15 else prod.right
                        dot.edge(prod.left, nt, label=label)
            
            dot.render(view=False, cleanup=True)
            return os.path.join(self.output_dir, f"{filename}.png")
        except Exception as e:
            print(f"Error creating graph: {e}")
            return None
    
    def create_chomsky_hierarchy_diagram(self, current_type, filename='hierarchy'):
        """Visualize Chomsky hierarchy"""
        try:
            import graphviz
            dot = graphviz.Digraph(filename=filename, directory=self.output_dir, format='png')
            dot.attr(rankdir='TB')
            
            types = [
                ('Type0', 'TIPO 0\nRecursivamente\nenumerable\n(Máquina Turing)', 0),
                ('Type1', 'TIPO 1\nSensible al\ncontexto\n(MT Acotada)', 1),
                ('Type2', 'TIPO 2\nLibre de\ncontexto\n(Autómata Pila)', 2),
                ('Type3', 'TIPO 3\nRegular\n(Autómata Finito)', 3)
            ]
            
            for key, label, type_num in types:
                color = 'lightcoral' if type_num == current_type else 'lightgray'
                dot.node(key, label, style='filled', fillcolor=color, shape='box')
                
            # Add edges to show hierarchy
            dot.edge('Type0', 'Type1')
            dot.edge('Type1', 'Type2')
            dot.edge('Type2', 'Type3')
            
            dot.render(view=False, cleanup=True)
            return os.path.join(self.output_dir, f"{filename}.png")
        except Exception as e:
            print(f"Error creating hierarchy: {e}")
            return None
    
    def create_simple_tree(self, productions: List[Production], filename='tree'):
        """Create simple derivation tree"""
        try:
            import graphviz
            dot = graphviz.Digraph(filename=filename, directory=self.output_dir, format='png')
            dot.attr(rankdir='TB')
            
            dot.node('root', 'S (Símbolo inicial)', shape='ellipse', style='filled', fillcolor='lightgreen')
            
            for i, prod in enumerate(productions):
                node_id = f"prod_{i}"
                dot.node(node_id, str(prod), shape='box', style='filled', fillcolor='lightyellow')
                dot.edge('root' if i == 0 else f"prod_{i-1}", node_id)
            
            dot.render(view=False, cleanup=True)
            return os.path.join(self.output_dir, f"{filename}.png")
        except Exception as e:
            print(f"Error creating tree: {e}")
            return None