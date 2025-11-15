import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from typing import Dict, Tuple, List
from learning_agent import LearningAgent
from classifier import ChomskyClassifier

class IntelligentPredictor:
    """Predictor que combina reglas + aprendizaje"""
    
    def __init__(self):
        self.learning_agent = LearningAgent()
        self.confidence_threshold = 0.7
    
    def predict_with_confidence(self, productions, classifier_result: Dict) -> Dict:
        """Predecir clasificación con nivel de confianza"""
        
        confidence = self._calculate_confidence(productions, classifier_result)
        similar_patterns = self._find_similar_patterns(productions)
        
        return {
            'type': classifier_result['type'],
            'name': classifier_result['name'],
            'confidence': confidence,
            'similar_examples': similar_patterns,
            'reasoning': self._generate_reasoning(classifier_result, confidence)
        }
    
    def _calculate_confidence(self, productions, result: Dict) -> float:
        """Calcular confianza (0-1)"""
        num_justifications = len(result['justification'])
        base_confidence = min(num_justifications * 0.25, 1.0)
        
        if result['type'] == 2:  # Type 2 es común, menos confianza
            base_confidence *= 0.9
        
        return round(base_confidence, 2)
    
    def _find_similar_patterns(self, productions) -> List:
        """Encontrar patrones similares en memoria"""
        memories = self.learning_agent.memory['classifications']
        
        similar = []
        for mem in memories[-10:]:  # Últimas 10 clasificaciones
            similar.append({
                'grammar_sample': mem['grammar'][:50],
                'type': mem['classification'],
                'timestamp': mem['timestamp']
            })
        
        return similar
    
    def _generate_reasoning(self, result: Dict, confidence: float) -> str:
        """Generar explicación de la predicción"""
        if confidence > 0.9:
            level = "muy alta"
        elif confidence > 0.7:
            level = "alta"
        else:
            level = "moderada"
        
        reasoning = f"Clasificación con confianza {level} ({confidence*100}%)\n"
        reasoning += f"Justificaciones: {len(result['justification'])}\n"
        
        return reasoning