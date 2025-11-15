# Enlace al proyecto de github

https://github.com/santiagoesdras/chomsky-classifier

# Manual de Usuario - Chomsky Classifier AI

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación y Configuración](#instalación-y-configuración)
4. [Guía de Inicio Rápido](#guía-de-inicio-rápido)
5. [Funcionalidades Principales](#funcionalidades-principales)
6. [Ejemplos Prácticos](#ejemplos-prácticos)
7. [Solución de Problemas](#solución-de-problemas)
8. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## Introducción

**Chomsky Classifier AI** es una herramienta educativa interactiva que clasifica automáticamente gramáticas formales según la **Jerarquía de Chomsky**, con capacidades de inteligencia artificial y aprendizaje automático.

### Para quién es este manual
- Estudiantes de Teoría de Lenguajes Formales
- Docentes de Compiladores e Informática Teórica
- Investigadores en Lenguajes Formales
- Desarrolladores interesados en autómatas

### Qué aprenderás
- Cómo instalar y ejecutar la aplicación
- Usar todas las funcionalidades disponibles
- Clasificar tus propias gramáticas
- Entender la Jerarquía de Chomsky
- Interpretar resultados y análisis

---

## Requisitos del Sistema

### Hardware Mínimo
- **Procesador:** Intel/AMD 1.8 GHz o superior
- **RAM:** 2 GB mínimo (4 GB recomendado)
- **Espacio:** 500 MB disponibles
- **Pantalla:** Resolución 1024x768 mínimo

### Software Requerido
- **Python:** versión 3.8 o superior
- **Sistema Operativo:** Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Navegador Web:** Chrome, Firefox, Safari o Edge (versión reciente)

### Verificar versión de Python
```bash
python3 --version
```

---

## Instalación y Configuración

### Paso 1: Preparar el Entorno

#### En Linux/Mac:
```bash
# Abrir terminal
cd ~/Tareas/LenguajesFormales/Remontada-Academica/chomsky_classifier

# Crear entorno virtual
python3 -m venv venv

# Activar entorno
source venv/bin/activate
```

#### En Windows:
```bash
cd Tareas\LenguajesFormales\Remontada-Academica\chomsky_classifier

python -m venv venv

venv\Scripts\activate
```

Verifica que el entorno esté activado: el prompt debe mostrar `(venv)` al inicio.

---

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Espera a que se completen todas las instalaciones. Verás mensajes confirmando cada paquete instalado correctamente.

---

### Paso 3: Instalar Graphviz (Herramienta de Visualización)

#### Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install graphviz
```

#### Mac:
```bash
brew install graphviz
```

#### Windows:
1. Descargar desde: https://graphviz.org/download/
2. Ejecutar el instalador .msi
3. Marcar la opción "Add Graphviz to system PATH" durante la instalación

---

### Paso 4: Ejecutar la Aplicación

```bash
streamlit run ui/streamlit_app.py
```

Resultado esperado:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://XXX.XXX.X.XXX:8501
```

La aplicación se abrirá automáticamente en tu navegador. Si no ocurre, abre manualmente:
```
http://localhost:8501
```

---

## Guía de Inicio Rápido

### Pantalla Principal

La interfaz principal contiene los siguientes elementos:

```
ENCABEZADO
|--Titulo de la aplicacion
|--Subtitle

MENU LATERAL (izquierda)          CONTENIDO PRINCIPAL (derecha)
|--Clasificar Gramática           |-- Area de contenido principal
|--Ver Ejemplos                   |-- Cambia según opcion del menu
|--Tutorial
|--Estadísticas
|--Acerca de
```

El menú lateral permite navegar entre todas las funcionalidades de la aplicación.

---

## Funcionalidades Principales

### 1. Clasificar Gramática

**Ubicación:** Menú lateral -> "Clasificar Gramática"

#### Cómo usar:

1. Selecciona el formato de entrada (BNF o Notación Estándar)
2. Ingresa tu gramática en el área de texto
3. Haz clic en el botón "Clasificar Gramática"
4. La aplicación mostrará el resultado con explicación detallada

#### Ejemplo 1: Gramática Regular

Gramática a clasificar:
```
S -> aA
A -> b
```

Pasos:
1. Selecciona "Notación Estándar"
2. Copia y pega el texto anterior en el área de entrada
3. Haz clic en "Clasificar Gramática"

Resultado esperado:
```
TIPO 3 - Gramática Regular
Reconocida por: Autómata Finito Determinista (AFD)
Confianza: 95%

Análisis:
- Todas las producciones tienen solo un no-terminal a la derecha
- Forma normal: A -> aB (Lineal Derecha)
```

Razón de clasificación:
- La estructura sigue el patrón de gramáticas regulares
- Cada producción contiene máximo un no-terminal
- Es reconocible por un autómata finito

---

#### Ejemplo 2: Gramática Libre de Contexto

Gramática a clasificar:
```
S -> aSb | ab
```

Pasos:
1. Selecciona "Notación Estándar"
2. Ingresa la gramática
3. Haz clic en "Clasificar Gramática"

Resultado esperado:
```
TIPO 2 - Gramática Libre de Contexto
Reconocida por: Autómata con Pila (PDA)
Confianza: 98%

Análisis:
- El lado izquierdo contiene solo un no-terminal
- No hay restricciones de contexto
- Reconoce lenguajes como {a^n b^n | n >= 1}
```

---

### 2. Ver Ejemplos

**Ubicación:** Menú lateral -> "Ver Ejemplos"

Esta sección proporciona 4 ejemplos predefinidos, uno para cada tipo de gramática de la jerarquía de Chomsky.

#### Cómo usar:

1. Selecciona un tipo de gramática (Tipo 0, 1, 2 o 3) del desplegable
2. Lee la descripción y la gramática mostrada
3. Haz clic en "Analizar este ejemplo"
4. Observa el análisis detallado generado por la aplicación

#### Ejemplo Tipo 3 - Gramática Regular

Descripción: Reconoce identificadores simples (variables)

Gramática:
```
S -> aA | bA | a | b
A -> aA | bA | 0A | 1A | epsilon
```

Palabras aceptadas: a, b, a1, bx0, variable123
Palabras rechazadas: 1a (comienza con número), _var (comienza con guion)

---

### 3. Tutorial

**Ubicación:** Menú lateral -> "Tutorial"

El tutorial incluye las siguientes secciones:

#### Introducción a Lenguajes Formales
- Definiciones básicas
- Alfabetos y palabras
- Lenguajes y su clasificación

#### Jerarquía de Chomsky
- Tipo 0: Recursivamente Enumerable
- Tipo 1: Sensible al Contexto
- Tipo 2: Libre de Contexto
- Tipo 3: Regular

#### Autómatas Asociados
- Autómata Finito (AFD/AFND)
- Autómata con Pila
- Máquina Turing Acotada
- Máquina de Turing

#### Aplicaciones Prácticas
- Compiladores
- Procesamiento de Lenguaje Natural
- Validación de Datos

El tutorial proporciona una referencia visual de la jerarquía de Chomsky y conceptos relacionados.

---

### 4. Estadísticas del Agente

**Ubicación:** Menú lateral -> "Estadísticas"

#### Información Mostrada

La sección de estadísticas presenta:

General:
- Total de clasificaciones realizadas
- Fecha del primer uso
- Fecha del último uso
- Número de sesiones

Distribución por Tipo:
- Tipo 0: cantidad y porcentaje
- Tipo 1: cantidad y porcentaje
- Tipo 2: cantidad y porcentaje
- Tipo 3: cantidad y porcentaje

Confianza Promedio:
- Confianza media para cada tipo de gramática
- Confianza general del sistema

Información del Agente:
- Patrones aprendidos
- Precisión general

#### Cómo se usan estas estadísticas

- Monitorear desempeño: Ver qué tipos se clasifican con mayor frecuencia
- Evaluar aprendizaje: Observar cómo cambia la confianza en el tiempo
- Identificar debilidades: Detectar dónde el sistema tiene menor precisión
- Análisis temporal: Ver tendencias de uso a lo largo del tiempo

---

### 5. Acerca de

**Ubicación:** Menú lateral -> "Acerca de"

Información del proyecto:
- Versión actual de la aplicación
- Descripción de funcionalidades
- Autores y desarrolladores
- Referencias teóricas utilizadas
- Licencia del proyecto

---

## Ejemplos Prácticos

### Caso 1: Validar una Gramática de Expresiones Aritméticas

Objetivo: Clasificar una gramática que reconoce expresiones aritméticas simples

Gramática a analizar:
```
E -> E + T | T
T -> T * F | F
F -> (E) | n
```

Pasos:
1. Abre "Clasificar Gramática"
2. Selecciona "Notación Estándar"
3. Copia la gramática en el área de texto
4. Haz clic en "Clasificar"

Resultado esperado:
```
TIPO 2 - Libre de Contexto
Razón: Estructura recursiva típica de análisis sintáctico
Confianza: 99%
```

Explicación:
- No hay restricciones de contexto
- Es la gramática estándar para lenguajes de programación
- Requiere autómata con pila para su reconocimiento
- Las producciones siguen el patrón de derivación gramatical

---

### Caso 2: Analizar una Gramática Sensible al Contexto

Objetivo: Entender las diferencias entre Tipo 1 y Tipo 2

Gramática a analizar:
```
S -> aAbc | abc
Ab -> bA
Ac -> bc
```

Pasos:
1. Abre "Clasificar Gramática"
2. Ingresa la gramática en el área de texto
3. Observa la clasificación generada

Resultado esperado:
```
TIPO 1 - Sensible al Contexto
Razón: Presencia de producciones con contexto
Confianza: 94%

Detalles:
- Producción "Ab -> bA" depende del contexto
- Requiere máquina Turing acotada para su reconocimiento
- Más expresiva que Tipo 2
```

Por qué NO es Tipo 2:
- Tiene producciones con contexto (Ab, Ac) en el lado izquierdo
- El lado izquierdo contiene múltiples símbolos
- Exceede la capacidad de un autómata con pila

---

## Solución de Problemas

### Problema 1: "ModuleNotFoundError: No module named 'streamlit'"

Causa: Las dependencias no se instalaron correctamente

Solución:
```bash
# Asegurate que el entorno este activado
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Reinstala las dependencias
pip install --upgrade -r requirements.txt
```

---

### Problema 2: "Graphviz not found"

Causa: Graphviz no está instalado o no está en el PATH del sistema

Solución:

Linux:
```bash
sudo apt-get install graphviz
```

Mac:
```bash
brew install graphviz
```

Windows:
1. Descarga desde: https://graphviz.org/download/
2. Ejecuta el instalador .msi
3. Marca "Add Graphviz to the system PATH"
4. Reinicia la terminal

Verificar instalación:
```bash
dot -V
```

---

### Problema 3: "localhost:8501 no responde"

Causa: El puerto está en uso o Streamlit no inició correctamente

Solución:

Opción 1: Usar puerto diferente
```bash
streamlit run ui/streamlit_app.py --server.port 8502
```

Opción 2: Terminar proceso anterior
```bash
# Linux/Mac
lsof -ti:8501 | xargs kill -9

# Windows (PowerShell)
Get-Process -Id (Get-NetTCPConnection -LocalPort 8501).OwningProcess | Stop-Process
```

---

### Problema 4: "La aplicación es muy lenta"

Causa: Caché lleno o muchas visualizaciones almacenadas

Solución:
```bash
# Limpiar caché de Streamlit
rm -rf ~/.streamlit/cache_dir/*

# Limpiar diagramas generados
rm -rf output/diagrams/*
```

---

### Problema 5: "Error al ingresar gramática"

Posibles causas y soluciones:

| Error | Causa | Solución |
|-------|-------|----------|
| Caracteres inválidos | Símbolos no permitidos | Usa solo a-z, A-Z, 0-9, epsilon, ->, &#124; |
| Producción vacía | Falta especificar derecha | Asegúrate S -> (algo) |
| Sin no-terminales | Escritura incorrecta | Usa mayúsculas: A, B, S |
| Formato incorrecto | Sintaxis de BNF incorrecta | Revisa que las reglas sean válidas |

---

## Preguntas Frecuentes

### P: ¿Puedo usar la aplicación sin internet?

R: Sí, la aplicación funciona completamente offline una vez que está instalada. El único requisito es tener Python y las dependencias del proyecto instaladas en tu computadora.

---

### P: ¿Dónde se guardan mis clasificaciones?

R: Se guardan en el archivo `learning_agent_memory.json` en la carpeta del proyecto. Puedes revisar el historial completo en la sección "Estadísticas" de la aplicación.

---

### P: ¿Qué significa el porcentaje de confianza?

R: Es el nivel de certeza que tiene el sistema sobre la clasificación realizada. Se basa en:
- Coincidencia con patrones aprendidos en sesiones anteriores
- Consistencia de la gramática ingresada
- Claridad de las reglas de producción

Un porcentaje alto (mayor a 90%) significa que la clasificación es muy confiable.

---

### P: ¿Puedo exportar los resultados?

R: Actualmente la aplicación muestra resultados directamente en pantalla. Puedes:
- Capturar pantallas de los resultados
- Copiar el texto de los resultados
- Revisar el archivo JSON del historial de clasificaciones

Versiones futuras incluirán exportación directa a formatos PDF y otros.

---

### P: ¿Qué pasa si ingreso una gramática incorrecta?

R: El clasificador intentará analizarla. Posibles resultados:
- Clasificación correcta: Si la gramática sigue patrones reconocibles
- Mensaje de error informativo: Si está mal formada
- Confianza baja: Si no coincide con patrones conocidos

El sistema siempre explica su análisis para ayudarte a entender el resultado.

---

### P: ¿Cómo reinicio el aprendizaje del agente?

R: Elimina el archivo `learning_agent_memory.json`:

```bash
rm learning_agent_memory.json  # Linux/Mac
# o
del learning_agent_memory.json  # Windows
```

La próxima vez que ejecutes, el agente comenzará desde cero sin historial previo.

---

### P: ¿Puedo modificar los ejemplos predefinidos?

R: Sí, editando el archivo `ui/streamlit_app.py`. Busca la sección de ejemplos y modifica las gramáticas según tus necesidades educativas.

---

## Tips y Trucos

### Tip 1: Notación Rápida

Usa el portapapeles de tu sistema para pegar gramáticas complejas directamente en el área de entrada.

---

### Tip 2: Revisar Patrones Aprendidos

En la sección Estadísticas, puedes ver qué patrones ha aprendido el sistema. Esto te ayuda a entender qué características son importantes para cada clasificación.

---

### Tip 3: Comparar Gramáticas

Clasifica varias gramáticas seguidas para ver las diferencias en:
- Estructuras de producciones
- Niveles de confianza
- Explicaciones generadas

---

### Tip 4: Usar el Tutorial Regularmente

Si no recuerdas algún concepto, revisa el Tutorial. Proporciona una referencia rápida sin necesidad de libros externos.

---

## Accesos Directos (Teclado)

| Acción | Atajo |
|--------|-------|
| Recargar página | F5 |
| Mostrar consola del navegador | F12 |
| Ir al inicio | Ctrl + Home |

---

## Contacto y Soporte

### Reportar Problemas

Si encuentras un error o comportamiento inesperado:
1. Abre la sección de Issues en el repositorio de GitHub
2. Crea un nuevo Issue
3. Describe el problema con detalles específicos
4. Incluye información sobre: sistema operativo, versión de Python, pasos para reproducir

### Sugerencias de Mejora

Si tienes ideas para mejorar la aplicación:
- Crea un Feature Request en GitHub
- Envía un email al desarrollador
- Participa en las discusiones del proyecto

---

## Recursos Adicionales

### Libros Recomendados
- "Introduction to Automata Theory" - Hopcroft, Motwani, Ullman
- "Compiler Design" - Aho, Lam, Sethi, Ullman
- "Introduction to the Theory of Computation" - Michael Sipser

### Videos Educativos
- YouTube: Chomsky Hierarchy explained
- YouTube: Formal Languages and Automata Theory
- YouTube: Compiler Design Fundamentals

### Recursos Online
- automata.csc.ksu.edu - Interactive Automata Simulator
- jflap.org - Java Formal Languages and Automata Package

---

## Resumen Rápido

```
INICIO RAPIDO EN 5 PASOS:

1. Instala Python 3.8 o superior
2. Clona o descarga el proyecto
3. Crea entorno: python3 -m venv venv
4. Instala dependencias: pip install -r requirements.txt
5. Ejecuta: streamlit run ui/streamlit_app.py

Abre http://localhost:8501 en tu navegador
```

---

Manual actualizado: Noviembre 2024