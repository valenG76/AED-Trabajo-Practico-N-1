# Sistema de Gestión de Tratamientos Médicos (ICD10) - AED 2026

## DESCRIPCIÓN GENERAL DEL PROBLEMA
El proyecto consiste en desarrollar un sistema en Python para procesar datos de tratamientos médicos. El centro de salud utiliza el modelo **ICD10** (International Classification of Diseases, versión 10) para estandarizar los diagnósticos.

### Contexto y Reglas
* **Formato del Código**: Los códigos son alfanuméricos de hasta 6 caracteres (ej. "X##.##").
* **Entradas Obligatorias**: Se debe cargar el nombre del paciente, el código ICD10 y el monto base del tratamiento.
* **Restricciones Técnicas**: No se deben imprimir títulos ni mensajes de bienvenida. La calificación es semiautomática mediante un software de control (*runner*).
* **Salida Estándar**: Los resultados deben seguir una secuencia de instrucciones `print` específica: Beneficiario, Código, Capítulo y Monto a pagar.

---

## OBJETIVO DEL PROYECTO
Implementar una aplicación funcional que capture datos, identifique el capítulo médico correspondiente a través del código y calcule el monto final aplicando reglas financieras específicas.

---

## ENFOQUE DE SOLUCIÓN (ALTO NIVEL)
1. **Captura de Datos**: Recepción de entradas en el orden estrictamente solicitado.
2. **Parsing**: Descomposición del código ICD10 para separar la letra inicial, el bloque y la enfermedad específica (dígitos a la derecha del punto).
3. **Mapeo de Capítulos**: Clasificación del diagnóstico dentro de los 22 capítulos del catálogo ICD10.
4. **Cálculo de Monto**:
    * **Recargo fijo universal**: $25.000.
    * **Adicional por letra**: A-L ($25.000), M-Z ($40.000, sin "U"), o U ($100.000).
    * **Porcentaje variable**: Se suma un porcentaje igual al número ubicado a la derecha del punto.

---

## DIVISIÓN DEL TRABAJO
Para una colaboración equitativa, el equipo se divide en 4 roles:

### Programador 1: Gestión de I/O y Salida Estándar
* **Responsabilidad**: Asegurar que el programa sea compatible con el *runner*.
* **Tareas**: Implementar la carga de datos sin mensajes de bienvenida y la salida final con el formato exacto solicitado.

### Programador 2: Lógica de Identificación de Capítulos
* **Responsabilidad**: Mapear el código con el nombre del capítulo médico.
* **Tareas**: Definir los rangos de letras y números para cada uno de los 22 capítulos (ej. distinguir Capítulos II y III para la letra "D").

### Programador 3: Motor de Cálculos (Fase A)
* **Responsabilidad**: Procesar el monto base y los recargos fijos iniciales.
* **Tareas**: Implementar la lógica condicional para los adicionales según la letra del código.

### Programador 4: Integración y Cálculo Porcentual (Fase B)
* **Responsabilidad**: Finalizar el cálculo del importe e integrar los módulos del equipo.
* **Tareas**: Extraer el valor decimal del código y aplicarlo como porcentaje sobre el monto acumulado.

---

## FLUJO DE TRABAJO DEL EQUIPO
* **Integración**: Uso de nombres de variables consistentes para facilitar la unión del código.
* **Hito Presencial**: El ajuste final se realizará en laboratorio durante la semana del 20 al 24 de abril, donde se recibirá un ítem extra obligatorio.

---

## CONSIDERACIONES DE TRABAJO EN GRUPO
* **Precisión**: No agregar saltos de línea ni adornos a las salidas, ya que esto invalidará la corrección automática.
* **Asistencia**: La entrega solo es válida para los alumnos presentes en la clase de laboratorio.
