import json
import os
from datetime import datetime
from typing import Dict, List

class LearningAgent:
    
    def __init__(self, memory_file='learning_memory.json'):
        self.memory_file = memory_file
        self.memory = self._load_memory()
        self.classification_history = []
    
    def _load_memory(self) -> Dict:
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return self._init_memory()
        return self._init_memory()
    
    def _init_memory(self) -> Dict:
        return {
            'classifications': [],
            'patterns': {},
            'confidence_scores': {},
            'last_updated': None
        }
    
    def record_classification(self, grammar: str, classification: int, confidence: float):
        record = {
            'timestamp': datetime.now().isoformat(),
            'grammar': grammar,
            'classification': classification,
            'confidence': confidence,
            'pattern_features': self._extract_features(grammar)
        }
        
        self.memory['classifications'].append(record)
        self.classification_history.append(record)
        
        self._update_patterns(record)
        self._save_memory()
    
    def _extract_features(self, grammar: str) -> Dict:
        lines = grammar.split('\n')
        production_lines = [l for l in lines if '→' in l or '->' in l]
        
        features = {
            'num_productions': len(production_lines),
            'avg_production_length': sum(len(l) for l in production_lines) / len(production_lines) if production_lines else 0,
            'has_epsilon': 'ε' in grammar,
            'has_context': any(len(l.split('→')[0] if '→' in l else l.split('->')[0]) > 1 for l in production_lines),
            'max_left_side_length': max(
                (len(l.split('→')[0]) if '→' in l else len(l.split('->')[0])) 
                for l in production_lines
            ) if production_lines else 0
        }
        return features
    
    def _update_patterns(self, record: Dict):
        features = record['pattern_features']
        classification = record['classification']
        
        pattern_key = f"type_{classification}"
        if pattern_key not in self.memory['patterns']:
            self.memory['patterns'][pattern_key] = []
        
        self.memory['patterns'][pattern_key].append(features)
    
    def _save_memory(self):
        self.memory['last_updated'] = datetime.now().isoformat()
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(self.memory, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save memory: {e}")
    
    def get_learning_insights(self) -> Dict:
        total_classifications = len(self.memory['classifications'])
        
        insights = {
            'total_classifications': total_classifications,
            'patterns_discovered': len(self.memory['patterns']),
            'type_distribution': {},
            'common_features': {}
        }
        
        for record in self.memory['classifications']:
            t = record['classification']
            key = f'type_{t}'
            insights['type_distribution'][key] = insights['type_distribution'].get(key, 0) + 1
        
        return insights