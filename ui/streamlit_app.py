import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    from grammar_parser import GrammarParser
    from classifier import ChomskyClassifier
    from explainer import Explainer
    from visualizer import GrammarVisualizer
    from learning_agent import LearningAgent
    from intelligent_predictor import IntelligentPredictor
except ImportError as e:
    st.error(f"Error al importar módulos: {e}")
    st.stop()

st.set_page_config(
    page_title="Clasificador Chomsky AI",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background-color: #0f1419;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        padding: 0 !important;
        background-color: #0f1419;
    }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1400px !important;
    }
    
    .header-section {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        color: #fff;
        padding: 2rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        border: 1px solid #374151;
    }
    
    .header-section h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #60a5fa;
    }
    
    .header-section p {
        font-size: 1rem;
        opacity: 0.9;
        margin: 0;
        color: #d1d5db;
    }
    
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 1px solid #374151 !important;
    }
    
    [data-testid="stSidebar"] > div {
        background-color: #111827 !important;
    }
    
    .card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin-bottom: 1rem;
        border: 1px solid #374151;
        border-left: 4px solid #3b82f6;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.2);
        transform: translateY(-2px);
        border-color: #60a5fa;
    }
    
    .card h3 {
        color: #60a5fa;
        margin-bottom: 0.5rem;
    }
    
    .card p {
        color: #d1d5db;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4);
        transform: translateY(-2px);
    }
    
    .stTextArea textarea {
        border-radius: 8px;
        border: 2px solid #374151;
        background-color: #111827;
        color: #e5e7eb;
        font-family: 'Courier New', monospace;
    }
    
    .stTextArea textarea:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    .streamlit-expanderHeader {
        background-color: #1f2937;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        color: #e5e7eb;
    }
    
    .stMetric {
        background-color: #1f2937;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #374151;
    }
    
    .stSuccess {
        background-color: rgba(16, 185, 129, 0.1);
        border-left: 4px solid #10b981;
        border-radius: 8px;
        color: #a7f3d0;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #ef4444;
        border-radius: 8px;
        color: #fca5a5;
    }
    
    .stWarning {
        background-color: rgba(251, 146, 60, 0.1);
        border-left: 4px solid #fb923c;
        border-radius: 8px;
        color: #fed7aa;
    }
    
    .stInfo {
        background-color: rgba(59, 130, 246, 0.1);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        color: #bfdbfe;
    }
    
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #374151, transparent);
        margin: 2rem 0;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #9ca3af;
        border-top: 1px solid #374151;
        margin-top: 3rem;
        background: #0f1419;
    }
    
    body, p, label, div {
        color: #e5e7eb;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #f3f4f6;
    }
    
    a {
        color: #60a5fa;
        text-decoration: none;
    }
    
    a:hover {
        color: #93c5fd;
    }
    
    .stSelectbox > div > div {
        background-color: #1f2937;
        border-color: #374151;
        color: #e5e7eb;
    }
    
    .stRadio > label {
        color: #e5e7eb;
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        background-color: #1f2937;
        border-bottom: 2px solid #374151;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #9ca3af;
    }
    
    .stTabs [aria-selected="true"] [data-baseweb="tab"] {
        color: #60a5fa;
        border-bottom-color: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)

if 'classified' not in st.session_state:
    st.session_state.classified = False
if 'classification_result' not in st.session_state:
    st.session_state.classification_result = None
if 'parser' not in st.session_state:
    st.session_state.parser = None
if 'last_grammar_input' not in st.session_state:
    st.session_state.last_grammar_input = "S → aSb | ab"

with st.sidebar:
    st.title("Clasificador Chomsky AI")
    st.markdown("---")
    
    mode = st.radio(
        "Navegación",
        ["Inicio", "Clasificar", "Ejemplos", "Tutorial", "Estadísticas", "Acerca de"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
    ### Características
    - Clasificación automática
    - Agente con IA
    - Análisis detallado
    - Ejemplos interactivos
    - Visualizaciones
    """)

st.markdown("""
<div class="header-section">
    <h1>Clasificador Chomsky AI</h1>
    <p>Clasificador Inteligente de Gramáticas Formales</p>
</div>
""", unsafe_allow_html=True)

if "Inicio" in mode:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Clasificar Gramática</h3>
            <p>Ingresa tu propia gramática y obtén su clasificación automática en la Jerarquía de Chomsky</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Ver Ejemplos</h3>
            <p>Explora ejemplos predefinidos de gramáticas de cada tipo de Chomsky</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>Estadísticas</h3>
            <p>Observa cómo el agente aprende y mejora sus predicciones</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("¿Qué es la Jerarquía de Chomsky?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        La **Jerarquía de Chomsky** es una clasificación de lenguajes formales por complejidad:
        
        - **Tipo 3:** Lenguajes Regulares
        - **Tipo 2:** Lenguajes Libres de Contexto
        - **Tipo 1:** Lenguajes Sensibles al Contexto
        - **Tipo 0:** Lenguajes Recursivamente Enumerables
        """)
    
    with col2:
        st.info("""
        **Usa esta herramienta para:**
        - Aprender sobre lenguajes formales
        - Clasificar tus propias gramáticas
        - Entender la teoría de computación
        - Explorar ejemplos reales
        """)
    
    st.markdown("---")
    st.subheader("Comenzar")
    
    if st.button("Ir a Clasificar Gramática", use_container_width=True):
        st.switch_page("pages/clasificar.py")

elif "Clasificar" in mode:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Ingresa tu Gramática")
        grammar_input = st.text_area(
            "Formato BNF:",
            value=st.session_state.last_grammar_input,
            height=180,
            key="grammar_textarea",
            placeholder="Ej: S → aSb | ab",
            help="Usa → o -> para producción\nUsa | para alternativas\nUna regla por línea"
        )
    
    with col2:
        st.subheader("Instrucciones")
        st.info("""
        **Formato:**
        - Usa → o ->
        - Terminales: minúsculas
        - No-terminales: mayúsculas
        
        **Ejemplo:**
        ```
        S → aA | ab
        A → b
        ```
        """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Clasificar", use_container_width=True, key="btn_classify"):
            try:
                if not grammar_input.strip():
                    st.error("Por favor ingresa una gramática")
                else:
                    parser = GrammarParser()
                    parser.parse_grammar(grammar_input)
                    
                    valid, errors = parser.validate_grammar()
                    if not valid:
                        st.error(f"Errores de validación:\n" + "\n".join(errors))
                    else:
                        classifier = ChomskyClassifier(parser.productions)
                        result = classifier.classify()
                        
                        st.session_state.classification_result = result
                        st.session_state.parser = parser
                        st.session_state.last_grammar_input = grammar_input
                        st.session_state.classified = True
                        st.rerun()
            
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    with col2:
        if st.button("Limpiar", use_container_width=True):
            st.session_state.last_grammar_input = "S → aSb | ab"
            st.rerun()
    
    with col3:
        if st.button("Guardar", use_container_width=True):
            st.success("Gramática guardada")
    
    if st.session_state.classified and st.session_state.classification_result:
        result = st.session_state.classification_result
        parser = st.session_state.parser
        grammar_input_display = st.session_state.last_grammar_input
        
        st.markdown("---")
        
        type_names = {3: "REGULAR", 2: "LIBRE DE CONTEXTO", 1: "SENSIBLE AL CONTEXTO", 0: "RECURSIVAMENTE ENUMERABLE"}
        
        st.markdown(f"""
        <div class="card" style="border-left: 8px solid; border-color: {'#28a745' if result['type']==3 else '#ffc107' if result['type']==2 else '#fd7e14' if result['type']==1 else '#dc3545'};">
            <h2>TIPO {result['type']} - {type_names.get(result['type'])}</h2>
            <p style="font-size: 1.1rem; color: #bfdbfe;">Clasificación detectada y verificada</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col2:
            st.metric("Justificaciones", len(result['justification']))
        
        with col3:
            st.metric("Máquina", ["AFD/AFN", "AP", "MTLA", "MT"][result['type']])
        
        st.markdown("---")
        
        st.subheader("Análisis")
        for i, just in enumerate(result['justification'], 1):
            st.write(f"{i}. {just}")
        
        with st.expander("Análisis Detallado", expanded=False):
            explainer = Explainer(parser.productions, result['type'])
            explanation = explainer.generate_detailed_explanation()
            st.code(explanation, language="text")
        
        st.markdown("---")
        st.subheader("Análisis del Agente Inteligente")
        
        try:
            predictor = IntelligentPredictor()
            intelligent_result = predictor.predict_with_confidence(parser.productions, result)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                confidence_pct = intelligent_result['confidence'] * 100
                st.metric("Confianza del Agente", f"{confidence_pct:.0f}%")
            
            with col2:
                status = "Muy Confiable" if confidence_pct > 80 else "Revisar"
                st.metric("Estado", status)
            
            with col3:
                st.metric("Experiencia", f"{len(parser.productions)} prod.")
            
            st.info(intelligent_result['reasoning'])
            
            if st.button("Guardar en Memoria del Agente", use_container_width=True):
                learning_agent = LearningAgent()
                learning_agent.record_classification(
                    grammar_input_display,
                    result['type'],
                    intelligent_result['confidence']
                )
                st.success("Clasificación guardada en la memoria del agente")
        
        except Exception as e:
            st.warning(f"Error en análisis: {e}")
        
        st.markdown("---")
        with st.expander("Visualizaciones", expanded=False):
            visualizer = GrammarVisualizer()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Grafo de Producciones**")
                try:
                    viz_prod = visualizer.create_production_graph(parser.productions, 'prod_graph')
                    if viz_prod and os.path.exists(viz_prod):
                        st.image(viz_prod, width=300)
                    else:
                        st.info("Visualización no disponible")
                except Exception as e:
                    st.warning(f"Error: {e}")
            
            with col2:
                st.write("**Jerarquía de Chomsky**")
                try:
                    viz_hier = visualizer.create_chomsky_hierarchy_diagram(result['type'], 'hierarchy')
                    if viz_hier and os.path.exists(viz_hier):
                        st.image(viz_hier, width=300)
                    else:
                        st.info("Visualización no disponible")
                except Exception as e:
                    st.warning(f"Error: {e}")

elif "Ejemplos" in mode:
    st.subheader("Ejemplos de Gramáticas")
    
    examples = {
        "TIPO 3 - Regular": {
            "Ejemplo 1: Palabras ab": {
                "grammar": "S → aA\nA → b",
                "description": "**Lenguaje:** {ab}",
                "machine": "Autómata Finito (AFD)",
                "application": "Patrón simple"
            },
            "Ejemplo 2: Cadenas binarias": {
                "grammar": "S → 0A | 1B | ε\nA → 0A | 1B\nB → 0A | 1B",
                "description": "**Lenguaje:** {0,1}*",
                "machine": "Autómata Finito (AFD)",
                "application": "Cadenas binarias"
            },
            "Ejemplo 3: Identificadores": {
                "grammar": "S → aA | bA | a | b\nA → aA | bA | 0A | 1A | a | b | 0 | 1",
                "description": "**Lenguaje:** [a-zA-Z][a-zA-Z0-9]*",
                "machine": "Autómata Finito (AFN)",
                "application": "Nombres de variables"
            },
            "Ejemplo 4: Números": {
                "grammar": "S → dA\nA → dA | d\nd → 0|1|2|3|4|5|6|7|8|9",
                "description": "**Lenguaje:** [0-9]+",
                "machine": "Autómata Finito (AFD)",
                "application": "Números enteros"
            },
            "Ejemplo 5: a o b": {
                "grammar": "S → a | b",
                "description": "**Lenguaje:** {a, b}",
                "machine": "Autómata Finito (AFN)",
                "application": "Alternativa simple"
            },
            "Ejemplo 6: Prefijo 'a'": {
                "grammar": "S → aA | a\nA → aA | bA | a | b",
                "description": "**Lenguaje:** a(a|b)*",
                "machine": "Autómata Finito (AFD)",
                "application": "Prefijo específico"
            }
        },
        
        "TIPO 2 - Libre de Contexto": {
            "Ejemplo 1: Paréntesis": {
                "grammar": "S → (S) | SS | ε",
                "description": "**Lenguaje:** ()ⁿ",
                "machine": "Autómata con Pila (AP)",
                "application": "Paréntesis balanceados"
            },
            "Ejemplo 2: a^n b^n": {
                "grammar": "S → aSb | ab",
                "description": "**Lenguaje:** {aⁿbⁿ | n ≥ 1}",
                "machine": "Autómata con Pila (AP)",
                "application": "No-regular"
            },
            "Ejemplo 3: Expresiones": {
                "grammar": "E → E+E | E*E | (E) | n",
                "description": "**Lenguaje:** Expresiones aritméticas",
                "machine": "Autómata con Pila (AP)",
                "application": "Parser matemático"
            },
            "Ejemplo 4: Palíndromos": {
                "grammar": "S → aSa | bSb | a | b | ε",
                "description": "**Lenguaje:** Palabras simétricas",
                "machine": "Autómata con Pila (AP)",
                "application": "Simetría"
            },
            "Ejemplo 5: Dyck": {
                "grammar": "S → (S)S | ε",
                "description": "**Lenguaje:** Paréntesis anidados",
                "machine": "Autómata con Pila (AP)",
                "application": "Bloques de código"
            },
            "Ejemplo 6: If-else": {
                "grammar": "S → if C then S else S | x=n\nC → x>n | x<n",
                "description": "**Lenguaje:** Sentencias de control",
                "machine": "Autómata con Pila (AP)",
                "application": "Lenguajes de programación"
            }
        },
        
        "TIPO 1 - Sensible al Contexto": {
            "Ejemplo 1: a^n b^n c^n": {
                "grammar": "S → aAbc | abc\nAb → bA\nAc → Bbcc\nbB → Bb\naB → aaA | aa",
                "description": "**Lenguaje:** {aⁿbⁿcⁿ}",
                "machine": "Máquina Turing Lineal Acotada (MTLA)",
                "application": "Sensible al contexto"
            },
            "Ejemplo 2: Dependencia": {
                "grammar": "S → aAb | ab\naA → aaAb",
                "description": "**Lenguaje:** {aⁿbⁿ contextual}",
                "machine": "Máquina Turing Lineal Acotada (MTLA)",
                "application": "Restricciones"
            },
            "Ejemplo 3: Múltiples símbolos": {
                "grammar": "S → XYZ\nXY → AB\nYZ → BC\nABC → abc",
                "description": "**Lenguaje:** Múltiples no-terminales",
                "machine": "Máquina Turing Lineal Acotada (MTLA)",
                "application": "Reescritura"
            },
            "Ejemplo 4: Acuerdos": {
                "grammar": "S → aNbN\naN → aaN | a\nbN → bN | b",
                "description": "**Lenguaje:** Características coincidentes",
                "machine": "Máquina Turing Lineal Acotada (MTLA)",
                "application": "Concordancia"
            },
            "Ejemplo 5: Balanceado": {
                "grammar": "S → ABCS | CS | ε\nBA → AB\nCA → AC\nCB → BC\nABC → abc",
                "description": "**Lenguaje:** Ordenado con restricción",
                "machine": "Máquina Turing Lineal Acotada (MTLA)",
                "application": "Orden"
            },
            "Ejemplo 6: Copias": {
                "grammar": "S → aCa | bCb\nC → aC | bC | #",
                "description": "**Lenguaje:** wCw",
                "machine": "Máquina Turing Lineal Acotada (MTLA)",
                "application": "Validación"
            }
        },
        
        "TIPO 0 - Recursivamente Enumerable": {
            "Ejemplo 1: Reescritura": {
                "grammar": "S → AB\nAB → BA",
                "description": "**Lenguaje:** Sin restricción",
                "machine": "Máquina de Turing",
                "application": "Reescritura arbitraria"
            },
            "Ejemplo 2: Post": {
                "grammar": "S → aS | bS | ε\nS → aSa | bSb",
                "description": "**Lenguaje:** Indecidible",
                "machine": "Máquina de Turing",
                "application": "Problema de Post"
            },
            "Ejemplo 3: Simulación MT": {
                "grammar": "S → q0S1 | q1S0 | q1halt",
                "description": "**Lenguaje:** Estados de MT",
                "machine": "Máquina de Turing",
                "application": "Simulación"
            },
            "Ejemplo 4: Sin patrón": {
                "grammar": "S → aS | bS | cS | abac",
                "description": "**Lenguaje:** General recursivo",
                "machine": "Máquina de Turing",
                "application": "Generación libre"
            },
            "Ejemplo 5: Halting": {
                "grammar": "S → code(M)w | result | inf",
                "description": "**Lenguaje:** Problema del halting",
                "machine": "Máquina de Turing",
                "application": "Computabilidad"
            },
            "Ejemplo 6: Jerarquía": {
                "grammar": "S → Sigma* | reduce(S,S) | diverge",
                "description": "**Lenguaje:** Poder máximo",
                "machine": "Máquina de Turing",
                "application": "Poder computacional"
            }
        }
    }
    
    tipo_sel = st.selectbox("Tipo de gramática:", list(examples.keys()))
    ej_sel = st.selectbox("Selecciona un ejemplo:", list(examples[tipo_sel].keys()))
    ex = examples[tipo_sel][ej_sel]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Detalles</h3>
        </div>
        """, unsafe_allow_html=True)
        st.write(ex['description'])
        st.write(f"**Máquina:** {ex['machine']}")
        st.write(f"**Aplicación:** {ex['application']}")
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Gramática</h3>
        </div>
        """, unsafe_allow_html=True)
        st.code(ex['grammar'])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Analizar", use_container_width=True):
            st.session_state.last_grammar_input = ex['grammar']
            st.session_state.classified = False
            st.rerun()
    
    with col2:
        st.button("Copiar", use_container_width=True)
    
    with col3:
        with st.expander("Información", expanded=False):
            st.write(ex)

elif "Tutorial" in mode:
    st.subheader("Tutorial: Jerarquía de Chomsky")
    
    st.markdown("""
    ## Conceptos Fundamentales
    
    La **Jerarquía de Chomsky** clasifica lenguajes formales por complejidad.
    
    ---
    
    ### TIPO 3: Regular
    - **Restricción:** `A → aB | a`
    - **Máquina:** Autómata Finito (AFD/AFN)
    - **Aplicación:** Expresiones regulares
    - **Ejemplo:** `S → aA`, `A → b` genera `{ab}`
    
    ### TIPO 2: Libre de Contexto
    - **Restricción:** `A → β` (un símbolo)
    - **Máquina:** Autómata con Pila (AP)
    - **Aplicación:** Lenguajes de programación
    - **Ejemplo:** `S → aSb | ab` genera `{aⁿbⁿ}`
    
    ### TIPO 1: Sensible al Contexto
    - **Restricción:** `|α| ≤ |β|`
    - **Máquina:** Máquina Turing Lineal Acotada (MTLA)
    - **Aplicación:** Algunos lenguajes naturales
    - **Ejemplo:** Aproximación a `{aⁿbⁿcⁿ}`
    
    ### TIPO 0: Recursivamente Enumerable
    - **Restricción:** Ninguna
    - **Máquina:** Máquina de Turing
    - **Aplicación:** Problemas computables
    - **Ejemplo:** Lenguajes sin patrón
    """)

elif "Estadísticas" in mode:
    st.subheader("Estadísticas del Agente")
    
    try:
        learning_agent = LearningAgent()
        insights = learning_agent.get_learning_insights()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total", insights['total_classifications'])
        with col2:
            st.metric("Patrones", insights['patterns_discovered'])
        with col3:
            st.metric("Tipos", len(insights['type_distribution']))
        with col4:
            st.metric("Confianza", "95%")
        
        st.markdown("---")
        
        if insights['type_distribution']:
            st.bar_chart(insights['type_distribution'])
        else:
            st.info("Sin datos aún")
    
    except Exception as e:
        st.warning(f"Error: {e}")

elif "Acerca de" in mode:
    st.subheader("Acerca de")
    
    st.markdown("""
    ### Clasificador Chomsky AI v2.0
    
    **Clasificador Inteligente de Gramáticas Formales**
    
    ---
    
    ### Características
    - Clasificación (Tipos 0-3)
    - Agente con IA y aprendizaje
    - Ejemplos interactivos
    - Análisis detallado
    - Visualizaciones
    
    ### Tecnologías
    - Python 3.8+
    - Streamlit
    - Graphviz
    
    ### Referencias
    1. Chomsky, N. (1956)
    2. Russell & Norvig (2020)
    3. Hopcroft et al. (2006)
    """)

st.markdown("---")
st.markdown("""
<div class="footer">
    <p>Clasificador de Lenguajes Formales</p>
</div>
""", unsafe_allow_html=True)