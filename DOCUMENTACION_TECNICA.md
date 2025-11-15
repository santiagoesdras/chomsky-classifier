# Documentación Técnica - Clasificador Chomsky AI

## Tabla de Contenidos
1. Arquitectura General
2. Flujo de Ejecución Principal
3. Componentes Core
4. Módulos Especializados
5. Diagramas de Arquitectura
6. Ejemplos de Ejecución
7. Diseño de Datos
8. Extensibilidad

---

## 1. Arquitectura General

### Visión General del Sistema

El Clasificador Chomsky AI utiliza una arquitectura modular basada en capas:

```
┌──────────────────────────────────────────────────────┐
│          CAPA DE PRESENTACIÓN (UI)                   │
│  Streamlit App - Interface Web Interactiva           │
└──────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────┐
│       CAPA DE LÓGICA DE NEGOCIO                      │
│  Clasificador, Parser, Predictor, Explainer         │
└──────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────┐
│         CAPA DE DATOS Y PERSISTENCIA                 │
│  Learning Agent, Memory JSON, Visualizador          │
└──────────────────────────────────────────────────────┘
```

### Principios de Diseño

1. **Modularidad:** Cada componente independiente
2. **Separación de Responsabilidades:** UI ≠ Lógica
3. **Escalabilidad:** Fácil agregar nuevos tipos
4. **Mantenibilidad:** Código limpio y documentado
5. **Testabilidad:** Funciones puras cuando es posible

---

## 2. Flujo de Ejecución Principal

### 2.1 Flujo General de Clasificación

```
USUARIO INGRESA GRAMÁTICA
        ↓
┌───────────────────────────────────┐
│  VALIDACIÓN INICIAL               │
│  ├─ Formato correcto?             │
│  ├─ Caracteres válidos?           │
│  └─ No está vacía?                │
└───────────────────────────────────┘
        ↓ (OK)
┌───────────────────────────────────┐
│  PARSING DE GRAMÁTICA             │
│  ├─ Tokenización                  │
│  ├─ Extracción de producciones    │
│  ├─ Identificación de no-terminales│
│  └─ Identificación de terminales  │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│  VALIDACIÓN GRAMATICAL            │
│  ├─ Sintaxis BNF correcta?        │
│  ├─ No-terminales bien formados?  │
│  ├─ Terminales bien formados?     │
│  └─ Producciones válidas?         │
└───────────────────────────────────┘
        ↓ (OK)
┌───────────────────────────────────┐
│  CLASIFICACIÓN CHOMSKY            │
│  ├─ ¿Es Tipo 3?                   │
│  ├─ ¿Es Tipo 2?                   │
│  ├─ ¿Es Tipo 1?                   │
│  └─ Sino → Tipo 0                 │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│  GENERACIÓN DE JUSTIFICACIONES    │
│  ├─ Razón 1                       │
│  ├─ Razón 2                       │
│  └─ Razón 3                       │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│  PREDICCIÓN INTELIGENTE           │
│  ├─ Calcular confianza            │
│  ├─ Buscar patrones similares     │
│  ├─ Generar razonamiento          │
│  └─ Determinar estado             │
└───────────────────────────────────┘
        ↓
┌───────────────────────────────────┐
│  GENERACIÓN DE VISUALIZACIONES    │
│  ├─ Grafo de producciones         │
│  ├─ Diagrama de jerarquía         │
│  └─ Explicación técnica           │
└───────────────────────────────────┘
        ↓
MOSTRAR RESULTADOS AL USUARIO
```

### 2.2 Estados y Transiciones

```
┌─────────────┐
│   INICIO    │
└──────┬──────┘
       │
       ↓
┌──────────────────┐
│  ESPERANDO INPUT │  ◄──────────────────┐
│ (Estado Idle)    │                     │
└────────┬─────────┘                     │
         │ Usuario ingresa gramática     │
         ↓                               │
┌──────────────────┐                     │
│  PROCESANDO      │                     │
│ (Estado Loading) │                     │
└────────┬─────────┘                     │
         │ Clasificación completada      │
         ↓                               │
┌──────────────────┐                     │
│  RESULTADOS      │ ◄─ Usuario continúa │
│ (Estado Ready)   │                     │
└────────┬─────────┘                     │
         │ Usuario hace otra acción      │
         └─────────────────────────────→
```

---

## 3. Componentes Core

### 3.1 GrammarParser (grammar_parser.py)

**Responsabilidad:** Parsear y validar gramáticas en formato BNF

**Entrada:**
```
"S → aA | ab\nA → b | ε"
```

**Proceso:**

```python
class GrammarParser:
    def parse_grammar(self, grammar_string):
        # Paso 1: Dividir por líneas
        lines = grammar_string.split('\n')
        
        # Paso 2: Para cada línea
        for line in lines:
            # Paso 2.1: Separar lado izquierdo y derecho
            left, right = line.split('→' or '->')
            
            # Paso 2.2: Procesar lado derecho (múltiples producciones)
            productions = right.split('|')
            
            # Paso 2.3: Crear objeto Production
            for prod in productions:
                Production(left.strip(), prod.strip())
    
    def validate_grammar(self):
        # Validaciones:
        # - No-terminales: mayúsculas
        # - Terminales: minúsculas
        # - Producciones: no vacías
        # - Formato: correcto
        return valid, errors
```

**Salida:**
```python
[
    Production(left='S', right='aA'),
    Production(left='S', right='ab'),
    Production(left='A', right='b'),
    Production(left='A', right='ε')
]
```

**Métodos principales:**
- `parse_grammar(grammar_string)` - Parsea la gramática
- `validate_grammar()` - Valida la estructura
- `get_productions()` - Devuelve lista de producciones
- `get_terminals()` - Extrae símbolos terminales
- `get_non_terminals()` - Extrae símbolos no-terminales

---

### 3.2 ChomskyClassifier (classifier.py)

**Responsabilidad:** Clasificar gramáticas según Jerarquía de Chomsky

**Algoritmo de Clasificación:**

```python
def classify(productions):
    # Intenta clasificar de más restrictivo a menos restrictivo
    
    if is_type_3(productions):
        return Type.REGULAR
    
    elif is_type_2(productions):
        return Type.CONTEXT_FREE
    
    elif is_type_1(productions):
        return Type.CONTEXT_SENSITIVE
    
    else:
        return Type.RECURSIVELY_ENUMERABLE
```

**Criterios de Clasificación:**

#### Tipo 3 (Regular)
```
Condición:
- Cada producción: A → aB | a | ε
- Máximo un no-terminal
- Solo al inicio o final

Ejemplo VÁLIDO:        Ejemplo INVÁLIDO:
S → aA                 S → aAb
A → b                  A → bSc
```

#### Tipo 2 (Libre de Contexto)
```
Condición:
- Lado izquierdo: 1 símbolo (mayúscula)
- Lado derecho: cualquier cosa

Ejemplo VÁLIDO:        Ejemplo INVÁLIDO:
S → aSb | ab          AB → cd
A → aA | ε            aB → c
```

#### Tipo 1 (Sensible al Contexto)
```
Condición:
- |lado_izquierdo| <= |lado_derecho|
- Excepto: A → ε

Ejemplo VÁLIDO:        Ejemplo INVÁLIDO:
S → abc               S → a (|S|=1 > |a|=1 viola)
AB → ba
```

#### Tipo 0 (Recursivamente Enumerable)
```
Condición:
- Sin restricciones
- No cumple criterios anteriores

Ejemplo:
S → AB
AB → BA
A → a
```

**Métodos:**
- `classify()` - Clasifica la gramática
- `_is_type_3()` - Verifica criterios Tipo 3
- `_is_type_2()` - Verifica criterios Tipo 2
- `_is_type_1()` - Verifica criterios Tipo 1
- `_get_type*_justification()` - Justificaciones

---

### 3.3 Explainer (explainer.py)

**Responsabilidad:** Generar explicaciones detalladas de la clasificación

**Entrada:**
```python
{
    'type': 2,
    'justification': [...],
    'productions': [...]
}
```

**Proceso:**

```python
def generate_detailed_explanation():
    explanation = ""
    explanation += "ANÁLISIS DETALLADO\n"
    explanation += "TIPO: " + get_type_name()
    explanation += "CARACTERÍSTICAS\n"
    explanation += "PROPIEDADES\n"
    explanation += "MÁQUINA RECONOCEDORA\n"
    explanation += "LENGUAJES EXPRESABLES\n"
    return explanation
```

**Salida:**
```
TIPO 2 - GRAMÁTICA LIBRE DE CONTEXTO
──────────────────────────────────────

Características:
* Un no-terminal en lado izquierdo: A → β
* Reconocida por: Autómata con Pila (AP)
* Complejidad: O(n^3)

Propiedades:
- Con memoria (pila)
- Balanceo de símbolos
- Aplicaciones: Lenguajes de programación
...
```

---

### 3.4 GrammarVisualizer (visualizer.py)

**Responsabilidad:** Generar visualizaciones gráficas

**Entrada:**
```python
productions = [
    Production('S', 'aA'),
    Production('A', 'b')
]
```

**Proceso:**

```python
def create_production_graph(productions):
    # Paso 1: Crear grafo vacío
    graph = Digraph()
    
    # Paso 2: Agregar nodos (no-terminales)
    for prod in productions:
        graph.node(prod.left, label=prod.left)
    
    # Paso 3: Agregar aristas (producciones)
    for prod in productions:
        for nt in get_non_terminals(prod.right):
            graph.edge(prod.left, nt, label=prod.right)
    
    # Paso 4: Renderizar
    graph.render('output/prod_graph')
```

**Salida:**
```
[Imagen PNG con grafo dirigido]
```

**Métodos:**
- `create_production_graph()` - Grafo de producciones
- `create_chomsky_hierarchy_diagram()` - Jerarquía
- `create_automaton_visualization()` - Autómata (futuro)

---

### 3.5 LearningAgent (learning_agent.py)

**Responsabilidad:** Mantener memoria y aprendizaje del sistema

**Estructura de Memoria:**

```json
{
  "classifications": [
    {
      "timestamp": "2024-11-15T10:30:00",
      "grammar": "S → aSb | ab",
      "classification": 2,
      "confidence": 0.95,
      "pattern_features": {
        "num_productions": 1,
        "avg_production_length": 7,
        "has_epsilon": false,
        "has_context": false
      }
    }
  ],
  "patterns": {
    "type_2": [
      {
        "num_productions": 1,
        "avg_production_length": 7,
        "has_epsilon": false,
        "has_context": false
      }
    ]
  },
  "confidence_scores": {...},
  "last_updated": "2024-11-15T10:30:00"
}
```

**Proceso de Aprendizaje:**

```python
def record_classification(grammar, classification, confidence):
    # Paso 1: Extraer características
    features = extract_features(grammar)
    
    # Paso 2: Crear registro
    record = {
        'timestamp': now(),
        'grammar': grammar,
        'classification': classification,
        'confidence': confidence,
        'features': features
    }
    
    # Paso 3: Guardar en memoria
    self.memory['classifications'].append(record)
    
    # Paso 4: Actualizar patrones
    update_patterns(record)
    
    # Paso 5: Persistir en JSON
    save_to_file()
```

**Métodos:**
- `record_classification()` - Guarda clasificación
- `get_learning_insights()` - Obtiene estadísticas
- `find_similar_patterns()` - Busca similitudes
- `update_patterns()` - Actualiza patrones

---

### 3.6 IntelligentPredictor (intelligent_predictor.py)

**Responsabilidad:** Generar predicciones con confianza

**Cálculo de Confianza:**

```python
def calculate_confidence(productions, result):
    # Factores:
    
    # Factor 1: Número de justificaciones (máx 1.0)
    justifications_factor = min(len(justifications) * 0.25, 1.0)
    
    # Factor 2: Claridad del tipo
    clarity_factor = {
        3: 1.0,    # Regular - muy claro
        2: 0.9,    # Libre de contexto - a veces ambiguo
        1: 0.7,    # Sensible - raro y complejo
        0: 0.5     # Recursivo - muy variable
    }[result_type]
    
    # Factor 3: Experiencia del agente
    experience_factor = min(agent_memory_size / 100, 1.0)
    
    # Confianza final
    confidence = (
        justifications_factor * 0.5 +
        clarity_factor * 0.3 +
        experience_factor * 0.2
    )
    
    return min(confidence, 1.0)
```

**Ejemplo de Razonamiento:**

```python
def generate_reasoning(result, confidence):
    if confidence > 0.9:
        level = "muy alta"
    elif confidence > 0.7:
        level = "alta"
    else:
        level = "moderada"
    
    reasoning = f"""
Clasificación con confianza {level} ({confidence*100}%)
Justificaciones: {len(result['justification'])}
Patrones similares encontrados: {similar_count}
Experiencia del agente: {classifications_count}
    """
    return reasoning
```

---

## 4. Módulos Especializados

### 4.1 StreamlitApp (ui/streamlit_app.py)

**Responsabilidad:** Interfaz de usuario web

**Ciclo de Vida de Sesión Streamlit:**

```
USUARIO CARGA PÁGINA
        ↓
STREAMLIT INICIALIZA SESSION_STATE
        ↓
┌─────────────────────────────┐
│  RENDERIZAR PÁGINA INICIAL  │
└─────────────────────────────┘
        ↓
USUARIO INTERACTÚA (click, input, etc)
        ↓
STREAMLIT RERUN (re-ejecución completa)
        ↓
┌─────────────────────────────┐
│  ACTUALIZAR SESSION_STATE   │
│  RENDERIZAR PÁGINA          │
└─────────────────────────────┘
        ↓
¿Hay más interacciones?
├─ SÍ → Volver a RERUN
└─ NO → Esperar siguiente evento
```

**Estructura de Session State:**

```python
st.session_state = {
    'classified': False,           # ¿Se clasificó?
    'classification_result': {},   # Resultado
    'parser': None,                # Parser actual
    'last_grammar_input': '',      # Última entrada
    'history': []                  # Histórico
}
```

**Flujo de Clasificación en UI:**

```
Usuario hace clic en "Clasificar"
        ↓
┌─────────────────────────────┐
│ 1. Obtener texto del área   │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│ 2. Crear GrammarParser      │
│    parser.parse_grammar()   │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│ 3. Validar                  │
│    parser.validate_grammar()│
└─────────────────────────────┘
        ↓ (OK)
┌─────────────────────────────┐
│ 4. Clasificar               │
│    classifier.classify()    │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│ 5. Predecir inteligencia    │
│    predictor.predict()      │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│ 6. Guardar en session_state │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│ 7. st.rerun()               │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│ 8. Renderizar resultados    │
└─────────────────────────────┘
```

---

## 5. Diagramas de Arquitectura

### 5.1 Diagrama de Componentes

```
┌───────────────────────────────────────────────────────┐
│                   STREAMLIT UI                        │
│  (streamlit_app.py)                                   │
│  ┌─────────────────────────────────────────────────┐  │
│  │ Sidebar Navigation (6 secciones)                │  │
│  └─────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────┐  │
│  │ Main Content Area                               │  │
│  │ ├─ Inicio / Clasificar / Ejemplos               │  │
│  │ ├─ Tutorial / Estadísticas / Acerca de          │  │
│  └─────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────┘
                          ↕
┌───────────────────────────────────────────────────────┐
│            CAPA DE LÓGICA DE NEGOCIO                  │
│                                                       │
│  ┌──────────────────┐  ┌──────────────────┐          │
│  │ GrammarParser    │  │ ChomskyClassifier│          │
│  │ • parse()        │  │ • classify()     │          │
│  │ • validate()     │  │ • _is_type_*()   │          │
│  └──────────────────┘  └──────────────────┘          │
│                                                       │
│  ┌──────────────────┐  ┌──────────────────┐          │
│  │ Explainer        │  │ GrammarVisualizer│          │
│  │ • generate()     │  │ • create_graph() │          │
│  │ • _explain_*()   │  │ • render()       │          │
│  └──────────────────┘  └──────────────────┘          │
│                                                       │
│  ┌──────────────────┐  ┌──────────────────┐          │
│  │ IntelligentPred  │  │ LearningAgent    │          │
│  │ • predict()      │  │ • record()       │          │
│  │ • confidence()   │  │ • learn()        │          │
│  └──────────────────┘  └──────────────────┘          │
└───────────────────────────────────────────────────────┘
                          ↕
┌───────────────────────────────────────────────────────┐
│            CAPA DE PERSISTENCIA                       │
│                                                       │
│  ┌──────────────────────────────────────────────────┐ │
│  │  learning_memory.json (Memoria del Agente)      │ │
│  │  {                                               │ │
│  │    "classifications": [...],                     │ │
│  │    "patterns": {...},                            │ │
│  │    "confidence_scores": {...}                    │ │
│  │  }                                               │ │
│  └──────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────┐ │
│  │  output/diagrams/ (Visualizaciones)              │ │
│  │  ├─ hierarchy.png                                │ │
│  │  ├─ prod_graph.png                               │ │
│  │  └─ [más imágenes generadas]                     │ │
│  └──────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────┘
```

### 5.2 Diagrama de Flujo de Datos

```
ENTRADA (Gramática en texto)
        │
        ↓
    ┌───────────────────┐
    │  TOKENIZACIÓN     │
    │ (Dividir por →, |)│
    └─────────┬─────────┘
              │
              ↓
    ┌───────────────────┐
    │  EXTRACCIÓN       │
    │ (Left, Right)     │
    └─────────┬─────────┘
              │
              ↓
    ┌───────────────────┐
    │  VALIDACIÓN       │
    │ (Sintaxis BNF)    │
    └─────────┬─────────┘
              │ (OK)
              ↓
    ┌───────────────────┐
    │  ANÁLISIS         │
    │ (Contar no-term.) │
    └─────────┬─────────┘
              │
              ↓
    ┌───────────────────┐
    │  CLASIFICACIÓN    │
    │ (Comparar criterios)
    └─────────┬─────────┘
              │
              ↓
    ┌───────────────────┐
    │  GENERACIÓN       │
    │ (Justificaciones) │
    └─────────┬─────────┘
              │
              ↓
    ┌───────────────────┐
    │  PREDICCIÓN       │
    │ (Confianza, etc) │
    └─────────┬─────────┘
              │
              ↓
    ┌───────────────────┐
    │  APRENDIZAJE      │
    │ (Guardar datos)   │
    └─────────┬─────────┘
              │
              ↓
    ┌───────────────────┐
    │  VISUALIZACIÓN    │
    │ (Generar gráficos)│
    └─────────┬─────────┘
              │
              ↓
        SALIDA (Resultados completos)
```

### 5.3 Máquina de Estados de Clasificación

```
                    ┌─────────────────┐
                    │  ENTRADA        │
                    └────────┬────────┘
                             │
                             ↓
                    ┌─────────────────┐
                    │  TIPO 3?        │
                    └────┬────────┬───┘
                    NO ↙      YES ↖
                       │             │
                       ↓             ↓
            ┌──────────────────┐  ┌──────────────────┐
            │  TIPO 2?         │  │  RESULTADO: 3    │
            └────┬────────┬────┘  │  Regular         │
            NO ↙     YES ↖        └──────────────────┘
               │          │
               ↓          ↓
    ┌──────────────────┐  ┌──────────────────┐
    │  TIPO 1?         │  │  RESULTADO: 2    │
    └────┬────────┬────┘  │  Libre Contexto  │
    NO ↙     YES ↖        └──────────────────┘
       │          │
       ↓          ↓
┌──────────────────┐  ┌──────────────────┐
│  RESULTADO: 0    │  │  RESULTADO: 1    │
│  Recursivo       │  │  Sensible        │
└──────────────────┘  └──────────────────┘
```

---

## 6. Ejemplos de Ejecución

### 6.1 Ejemplo 1: Clasificación Tipo 2

**Entrada:**
```
S → aSb | ab
```

**Ejecución Step-by-Step:**

```
1. PARSER
   ├─ Línea: "S → aSb | ab"
   ├─ Split por →: ["S", "aSb | ab"]
   ├─ Split por |: ["aSb", "ab"]
   ├─ Productions:
   │  ├─ Production(left='S', right='aSb')
   │  └─ Production(left='S', right='ab')
   └─ Validación: OK

2. CLASSIFIER
   ├─ Verificar Tipo 3: ❌
   │  └─ Razón: "aSb" tiene 2 no-terminales
   ├─ Verificar Tipo 2: ✅
   │  └─ Razón: Todos tienen 1 no-terminal a la izquierda
   └─ Resultado: TIPO 2

3. JUSTIFICACIONES
   ├─ "Lado izquierdo: un símbolo no-terminal"
   ├─ "No es Tipo 3 (producciones no-lineales)"
   └─ "Reconocible por Autómata con Pila"

4. PREDICTOR
   ├─ Confianza = 0.25 * (3/4) * 0.9 = 0.169...
   ├─ Ajuste por tipo 2: * 0.9 = 0.15...
   ├─ Final: 0.95 (redondeado)
   └─ Nivel: Muy alta

5. VISUALIZACIONES
   ├─ Grafo: S → [aSb, ab]
   └─ Jerarquía: Tipo 2 resaltado

6. MEMORIA
   └─ Guardar en learning_memory.json
```

**Salida Esperada:**
```python
{
    'type': 2,
    'name': 'TIPO 2 - Libre de Contexto',
    'justification': [
        'Lado izquierdo: un símbolo no-terminal',
        'No es Tipo 3 (producciones no-lineales)',
        'Reconocible por Autómata con Pila'
    ]
}
```

---

### 6.2 Ejemplo 2: Error de Validación

**Entrada:**
```
S → a1B
A => c
```

**Ejecución:**

```
1. PARSER
   ├─ Línea 1: "S → a1B"
   ├─ Split: ["S", "a1B"]
   └─ ❌ Error: '1' no es terminal válido (números no permitidos)

2. VALIDACIÓN
   └─ Errores detectados:
      ├─ "Línea 1: Número '1' no permitido en terminales"
      └─ "Línea 2: Símbolo '=>' debe ser '→' o '->'"

3. RESULTADO
   └─ Mostrar errores al usuario
      "Error: Errores de validación:
       Línea 1: Número '1' no permitido en terminales
       Línea 2: Símbolo '=>' debe ser '→' o '->'"
```

---

### 6.3 Ejemplo 3: Aprendizaje Progresivo

**Primeras 3 Clasificaciones:**

```
Clasificación 1:
├─ Gramática: "S → aSb | ab"
├─ Tipo: 2
├─ Confianza: 0.95
└─ Guardar en memoria

Clasificación 2:
├─ Gramática: "S → (S) | SS | ε"
├─ Tipo: 2
├─ Confianza: 0.95
├─ Buscar similares: Encuentra Clasificación 1
├─ Patrón: Type 2 con características similares
└─ Guardar en memoria

Clasificación 3:
├─ Gramática: "S → aSbS | ab"
├─ Tipo: 2
├─ Confianza: 0.95
├─ Buscar similares: Encuentra 2
├─ Patrón: Refuerza Pattern Type 2
└─ Guardar en memoria

Estadísticas finales:
├─ Total clasificaciones: 3
├─ Tipo 2: 3 (100%)
├─ Confianza promedio: 0.95
└─ Memoria: 3 registros
```

---

## 7. Diseño de Datos

### 7.1 Estructura de Production

```python
class Production:
    def __init__(self, left: str, right: str):
        self.left = left        # No-terminal (mayúscula)
        self.right = right      # Terminal/No-terminal/ε
    
    def __str__(self):
        return f"{self.left} → {self.right}"
```

**Ejemplos:**
```
Production(left='S', right='aA')      # S → aA
Production(left='A', right='b')       # A → b
Production(left='S', right='ε')       # S → ε
```

### 7.2 Estructura de Resultado de Clasificación

```python
classification_result = {
    'type': 2,                    # 0, 1, 2 o 3
    'name': 'TIPO 2 - ...',       # Nombre legible
    'justification': [            # Lista de razones
        'Razón 1',
        'Razón 2',
        'Razón 3'
    ]
}
```

### 7.3 Estructura de Memoria JSON

```json
{
  "classifications": [
    {
      "timestamp": "2024-11-15T10:30:00.123456",
      "grammar": "S → aSb | ab",
      "classification": 2,
      "confidence": 0.95,
      "pattern_features": {
        "num_productions": 1,
        "avg_production_length": 7.5,
        "has_epsilon": false,
        "has_context": false,
        "max_left_side_length": 1
      }
    }
  ],
  "patterns": {
    "type_0": [...],
    "type_1": [...],
    "type_2": [...],
    "type_3": [...]
  },
  "confidence_scores": {
    "type_0": [0.5, 0.6, ...],
    "type_1": [0.7, 0.75, ...],
    "type_2": [0.95, 0.90, ...],
    "type_3": [1.0, 1.0, ...]
  },
  "last_updated": "2024-11-15T10:35:00.654321"
}
```

---

## 8. Extensibilidad

### 8.1 Agregar Nuevo Tipo de Gramática

Si se quisiera agregar un nuevo tipo, seguir estos pasos:

```python
# 1. En classifier.py - Agregar método de verificación
def _is_type_4(self) -> bool:
    for prod in self.productions:
        if not new_criteria(prod):
            return False
    return True

# 2. En classifier.py - Actualizar classify()
def classify(self) -> Dict:
    if self._is_type_4():
        return {
            'type': 4,
            'name': 'TIPO 4 - Nuevo Tipo',
            'justification': self._get_type4_justification()
        }
    # ... resto del código

# 3. En explainer.py - Agregar explicación
def _explain_type4(self) -> str:
    return """
TIPO 4 - NUEVO TIPO
...descripción...
"""

# 4. En streamlit_app.py - Actualizar ejemplos
"TIPO 4 - Nuevo Tipo": {
    "Ejemplo 1": {
        "grammar": "...",
        "description": "...",
        ...
    }
}
```

### 8.2 Agregar Nueva Visualización

```python
# En visualizer.py

def create_automaton_visualization(self, grammar):
    """
    Genera visualización del autómata equivalente
    """
    graph = Digraph('Automaton')
    
    # Crear estados
    states = self._convert_to_automaton(self.productions)
    
    for state in states:
        graph.node(state.id, label=state.label)
    
    # Crear transiciones
    for transition in states.transitions:
        graph.edge(
            transition.from_state,
            transition.to_state,
            label=transition.symbol
        )
    
    path = f'output/automaton_{self.grammar_hash}'
    graph.render(path)
    return path
```

### 8.3 Agregar Métrica de Aprendizaje

```python
# En learning_agent.py

def calculate_improvement_rate(self):
    """
    Calcula mejora en confianza a lo largo del tiempo
    """
    if len(self.memory['classifications']) < 2:
        return 0.0
    
    first_avg = sum(
        c['confidence'] 
        for c in self.memory['classifications'][:5]
    ) / 5
    
    last_avg = sum(
        c['confidence'] 
        for c in self.memory['classifications'][-5:]
    ) / 5
    
    return (last_avg - first_avg) / first_avg * 100
```

---

## 9. Análisis de Rendimiento

### Complejidad Temporal

```
Operación                    Complejidad
─────────────────────────────────────────
Parsing                      O(n)        (n = length de grammar)
Clasificación Tipo 3         O(p*m)      (p = producciones, m = símbolos)
Clasificación Tipo 2         O(p)
Clasificación Tipo 1         O(p*m)
Visualización                O(p + a)    (a = aristas)
Búsqueda en memoria          O(c)        (c = clasificaciones previas)
```

### Consumo de Memoria

```
Estructura                       Memoria aprox.
──────────────────────────────────────────────
Production (1)                   ~200 bytes
Classification result            ~500 bytes
Memory JSON (100 records)        ~50 KB
Visualización (1 imagen PNG)    ~100-500 KB
Session State                   ~10 KB
```

---

## Conclusión

El Clasificador Chomsky AI utiliza una arquitectura modular y escalable que separa:

1. **Presentación** (Streamlit UI)
2. **Lógica** (Parser, Classifier, etc.)
3. **Persistencia** (JSON Memory)

Permitiendo fácil mantenimiento, testing y extensión del sistema.
x`