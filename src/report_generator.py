import os
from datetime import datetime
from fpdf import FPDF

def generate_report(grammar: str, classification: str, explanation: str, 
                   visualizations=None, output_dir: str = None) -> str:
    """Generar reporte PDF - Versión simplificada sin dependencias de fuentes externas"""
    
    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), 'output', 'reports')
    
    # Crear directorio si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Crear PDF con fuentes estándar
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Usar solo fuentes estándar (sin necesidad de archivos externos)
        pdf.set_font("Helvetica", "B", 16)
        
        # Título
        pdf.cell(0, 15, "Reporte de Clasificacion", ln=True, align="C")
        pdf.cell(0, 10, "Jerarquia de Chomsky", ln=True, align="C")
        
        # Fecha
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 10, f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
        
        pdf.ln(5)
        
        # Separador
        pdf.set_draw_color(100, 100, 100)
        pdf.line(15, pdf.get_y(), 195, pdf.get_y())
        pdf.ln(5)
        
        # Clasificación
        pdf.set_font("Helvetica", "B", 14)
        pdf.multi_cell(0, 10, f"CLASIFICACION: {classification}")
        
        pdf.ln(3)
        
        # Gramática
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 10, "GRAMATICA:", ln=True)
        pdf.set_font("Courier", "", 10)
        for line in grammar.split('\n'):
            if line.strip():
                clean_line = _clean_text_for_pdf(line)
                for part in _split_long_line(clean_line):
                    pdf.multi_cell(0, 6, f"  {part}")

        pdf.ln(3)
        
        # Explicación
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 10, "ANALISIS:", ln=True)
        
        pdf.set_font("Helvetica", "", 9)
        
        for line in explanation.split('\n'):
            clean_line = _clean_text_for_pdf(line.strip())
            if clean_line and len(clean_line) > 0:
                for part in _split_long_line(clean_line):
                    pdf.multi_cell(0, 5, f"  {part}", align="L")
        
        # Separador final
        pdf.ln(3)
        pdf.set_draw_color(100, 100, 100)
        pdf.line(15, pdf.get_y(), 195, pdf.get_y())
        
        # Footer
        pdf.ln(2)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 5, "Chomsky Classifier AI v2.0 - Clasificador de Lenguajes Formales", ln=True, align="C")
        
        # Guardar
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reporte_{timestamp}.pdf"
        filepath = os.path.join(output_dir, filename)
        
        pdf.output(filepath)
        print(f"✓ PDF generado correctamente: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"✗ Error al generar PDF: {e}")
        import traceback
        traceback.print_exc()
        return None


def _clean_text_for_pdf(text: str) -> str:
    """
    Limpiar texto para que sea compatible con FPDF (solo caracteres ASCII)
    """
    # Reemplazar caracteres especiales Unicode con equivalentes ASCII
    replacements = {
        '→': '->',           # Flecha derecha
        '⇒': '=>',           # Flecha doble derecha
        '←': '<-',           # Flecha izquierda
        '⇐': '<=',           # Flecha doble izquierda
        'ε': 'eps',          # Epsilon
        '∅': '{}',           # Conjunto vacío
        'Ø': '{}',           # Conjunto vacío (alt)
        '≤': '<=',           # Menor o igual
        '≥': '>=',           # Mayor o igual
        '≠': '!=',           # No igual
        '∈': 'in',           # Pertenece
        '∉': 'not in',       # No pertenece
        '∩': 'AND',          # Intersección
        '∪': 'OR',           # Unión
        '⊆': '<=',           # Subconjunto
        '⊇': '>=',           # Superconjunto
        '∞': 'inf',          # Infinito
        '•': '*',            # Punto
        '◦': 'o',            # Círculo
        '×': 'x',            # Multiplicación
        '÷': '/',            # División
        '±': '+/-',          # Plus-minus
        '√': 'sqrt',         # Raíz cuadrada
        'ⁿ': '^n',           # Superíndice n
        'π': 'pi',           # Pi
        '∀': 'for all',      # Para todo
        '∃': 'exists',       # Existe
        '∧': 'AND',          # AND lógico
        '∨': 'OR',           # OR lógico
        '¬': 'NOT',          # NOT lógico
        '⊢': '|-',           # Símbolo de derivación
        '⊨': '|=',           # Símbolo de satisfacción
        '■': '[END]',        # Símbolo de fin
    }
    
    result = text
    
    # Reemplazar cada carácter Unicode
    for unicode_char, ascii_equivalent in replacements.items():
        result = result.replace(unicode_char, ascii_equivalent)
    
    # Eliminar caracteres problemáticos que no están en ASCII estándar
    # Mantener solo ASCII imprimible (32-126)
    cleaned = []
    for char in result:
        # Mantener caracteres ASCII estándar
        if 32 <= ord(char) <= 126:
            cleaned.append(char)
        # Omitir otros caracteres
    
    return ''.join(cleaned)

def _split_long_line(line, maxlen=80):
    """Divide líneas largas sin espacios para evitar errores de FPDF."""
    result = []
    while len(line) > maxlen:
        result.append(line[:maxlen])
        line = line[maxlen:]
    if line:
        result.append(line)
    return result