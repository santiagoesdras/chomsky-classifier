# Chomsky Classifier AI - Agente Inteligente

Clasificador automático de gramáticas formales según la **Jerarquía de Chomsky** con capacidades de **Inteligencia Artificial y Aprendizaje Automático**.

## Características Principales

### Clasificación de Gramáticas
- **Tipo 3 (Regular)** - Autómata Finito
- **Tipo 2 (Libre de Contexto)** - Autómata con Pila
- **Tipo 1 (Sensible al Contexto)** - Máquina Turing Acotada
- **Tipo 0 (Recursivamente Enumerable)** - Máquina de Turing

### Agente de IA
- Aprendizaje automático de cada clasificación
- Memoria persistente en JSON
- Reconocimiento de patrones similares
- Confianza calculada en predicciones
- Estadísticas dinámicas del aprendizaje

### Interfaz Interactiva
- Clasificar Gramática - Ingresa tu propia gramática
- Ver Ejemplos - 4 ejemplos predefinidos
- Tutorial - Teoría completa de Chomsky
- Estadísticas - Métricas del agente
- Acerca de - Información del proyecto

### Análisis Detallado
- Visualización de producciones
- Jerarquía de Chomsky interactiva
- Explicaciones paso a paso
- Nivel de confianza de predicciones
- Histórico de clasificaciones

## Instalación

### Requisitos previos
- Python 3.8+
- pip

### Pasos de instalación

```bash
# 1. Clonar o descargar el proyecto
cd Chomsky-Classifier-AI

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
streamlit run ui/streamlit_app.py
```

## Cómo Usar

### 1. Clasificar una Gramática
```
Modo: "Clasificar Gramática"
Ingresa: S → aSb | ab
Resultado: TIPO 2 - Libre de Contexto
```

### 2. Ver Ejemplos
```
Modo: "Ver Ejemplos"
Selecciona un tipo
Haz clic en "Analizar este ejemplo"
```

### 3. Ver Estadísticas del Agente
```
Modo: "Estadísticas del Agente"
Observa patrones aprendidos
Revisa historial de clasificaciones
```

## Estructura del Proyecto

```
Chomsky-Classifier-AI/
├── src/
│   ├── grammar_parser.py          # Parser de BNF
│   ├── classifier.py               # Clasificador Chomsky
│   ├── explainer.py                # Generador de explicaciones
│   ├── visualizer.py               # Visualizaciones
│   ├── learning_agent.py           # Agente con aprendizaje
│   └── intelligent_predictor.py    # Predictor con confianza
├── ui/
│   └── streamlit_app.py            # Interfaz principal
├── tests/
│   └── test_classifier.py          # Tests unitarios
├── output/
│   ├── diagrams/                   # Visualizaciones generadas
│   └── reports/                    # Reportes generados
├── requirements.txt                # Dependencias
└── README.md                       # Este archivo
```

## Ejecutar Tests

```bash
source venv/bin/activate
pytest tests/test_classifier.py -v
```

## Tipos de Gramáticas Soportadas

### Tipo 3: Regular
```
S → aA
A → b | ε
```

### Tipo 2: Libre de Contexto
```
S → aSb | ab
A → aA | ε
```

### Tipo 1: Sensible al Contexto
```
S → aAbc | abc
Ab → bA
```

### Tipo 0: Recursivamente Enumerable
```
S → AB
AB → BA | a
```

## Cómo Funciona el Agente de IA

1. **Clasificación**: Analiza la gramática según reglas formales
2. **Aprendizaje**: Guarda clasificación + características
3. **Patrones**: Identifica similitudes con histórico
4. **Confianza**: Calcula certeza de la predicción
5. **Mejora**: Adapta su desempeño con cada uso

## Estadísticas del Agente

El agente mantiene:
- Total de clasificaciones realizadas
- Distribución por tipo de gramática
- Patrones reconocidos
- Confianza promedio
- Historial temporal

## Dependencias

- **streamlit** - Framework web interactivo
- **graphviz** - Visualización de grafos
- **fpdf2** - Generación de PDF (opcional)
- **pandas** - Análisis de datos
- **numpy** - Computación numérica

## Referencias Teóricas

1. Chomsky, N. (1956). "Three models for the description of language"
2. Russell, S. & Norvig, P. (2020). "Artificial Intelligence: A Modern Approach"
3. Hopcroft, J. E., et al. (2006). "Introduction to Automata Theory, Languages, and Computation"

## Casos de Uso

- Educación: Enseñanza de lenguajes formales
- Investigación: Análisis de gramáticas
- Desarrollo: Validación de lenguajes propios
- Análisis: Clasificación automatizada

## Configuración

Edita `streamlit_app.py` para:
- Cambiar tema (light/dark)
- Agregar más ejemplos
- Personalizar mensajes
- Ajustar estilos CSS

## Solución de Problemas

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: "Graphviz not installed"
```bash
# Linux
sudo apt-get install graphviz

# Mac
brew install graphviz

# Windows
choco install graphviz
```

### La app es lenta
- Limpia la carpeta `output/diagrams/`
- Reduce número de clasificaciones en historial

## Licencia

Este proyecto es de código abierto para fines educativos.

## Autor

Desarrollado como proyecto de **Remontada Académica** en Lenguajes Formales.

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

---

**Versión:** 2.0.0  
**Última actualización:** Noviembre 2024  
**Estado:** Completo y funcional