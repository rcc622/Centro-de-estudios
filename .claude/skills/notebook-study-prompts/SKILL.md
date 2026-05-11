---
name: notebook-study-prompts
description: Genera prompts customizados para NotebookLM que producen Study Guides densos y de calidad a partir de transcripciones de video, PDFs no estructurados, apuntes propios o cualquier .txt que Randall suba. Úsalo cuando Randall mencione "tengo transcripciones / .txt / apuntes para el curso X y quiero pasarlos a Notebook", "armame el prompt para generar el Study Guide", "necesito que NotebookLM me dé contenido denso de este material", o cuando vaya a arrancar un curso nuevo sin PDF oficial.
---

# NotebookLM — Prompts para Study Guides densos

Randall sube material crudo (transcripciones, apuntes, .txt) a NotebookLM y necesita prompts específicos según el tipo de curso para que la salida sea contenido pedagógico de calidad, no un resumen genérico. Esta skill produce esos prompts.

## Workflow al activarse

1. **Identificar el tipo de curso** según contexto o preguntando a Randall:
   - **Certificación con examen** (ej. Meta 410, ITIL, AWS) → prompts apuntan a "preguntas tipo examen, distractores plausibles, trampas"
   - **Curso técnico aplicado** (ej. Interconexión Solar, paneles Corella) → prompts apuntan a "cálculos, normativas, casos reales de instalación"
   - **Curso de habilidades / soft skills** (ej. Liderazgo) → prompts apuntan a "frameworks, autodiagnóstico, ejercicios de aplicación"
   - **Curso teórico-conceptual** (ej. CVS) → prompts apuntan a "definiciones, contraste de conceptos, ejemplos"

2. **Identificar el alcance específico** del módulo/día/sección que se va a generar. **No pedir un Study Guide del curso entero** — saturación de tokens y baja calidad. Mejor pedir por módulo/día.

3. **Generar el prompt** llenando la plantilla apropiada con:
   - Nombre del curso
   - Alcance específico (lista de temas que SÍ se cubren)
   - Lista de exclusiones (temas que NO van acá, evitar overlap con otros días)
   - Profundidad y formato deseado

4. **Entregar el prompt** a Randall **en un bloque copiable**, sin ningún texto explicativo extra dentro del bloque (para que pueda copy-paste directo a Notebook).

5. Decirle qué hacer con la salida: pegarla acá o subirla a `source/<curso>/<modulo>/study-guide.md`.

## Plantillas por tipo de curso

### A) Certificación con examen oficial

```
Voy a crear el contenido del [MÓDULO/DÍA N] de mi guía de estudio
para el examen [NOMBRE DE LA CERTIFICACIÓN].

ALCANCE — enfocate SOLO en:
- [TEMA 1]
- [TEMA 2]
- [TEMA 3]
- ...

NO incluyas estos temas (van en otros módulos):
- [TEMA EXCLUIDO 1]
- [TEMA EXCLUIDO 2]
- ...

Para cada tema del alcance generá:

1. **Definición precisa** del concepto, en 1-2 oraciones.

2. **Cuándo se usa / contexto de aplicación** — situaciones típicas
   donde aparece este concepto.

3. **Ejemplos concretos** del material fuente.

4. **Distinciones críticas** con conceptos parecidos que se
   suelen confundir en el examen.

5. **Trampas típicas de examen** — qué errores comete la gente,
   qué distractores parecen correctos pero no lo son.

6. **5 preguntas tipo examen** con:
   - 4 opciones (A, B, C, D)
   - Respuesta correcta marcada
   - Explicación de POR QUÉ la correcta es correcta
   - Explicación de POR QUÉ cada distractor es trampa

Al final del documento:

7. **30 flashcards Q/A**: preguntas específicas (no "qué es X" sino
   "diferencia entre X y Y", "qué pasa cuando Z"). Respuestas
   concisas (máx 2 oraciones).

8. **8 casos aplicados B2B**: situación realista + cuál es la
   decisión correcta + por qué.

9. **6 pares para emparejar**: concepto ↔ aplicación correcta.

10. **3 secuencias ordenables**: procesos del material que tengan
    orden específico, con los pasos en orden correcto y por qué
    ese orden importa.

Formato: Markdown bien estructurado, secciones numeradas.
```

### B) Curso técnico aplicado

```
Voy a crear el contenido del [MÓDULO/DÍA N] de mi guía de estudio
para [NOMBRE DEL CURSO] enfocado en aplicación profesional.

CONTEXTO: lo voy a usar en mi trabajo como [ROL] en [INDUSTRIA].

ALCANCE — enfocate SOLO en:
- [TEMA 1]
- [TEMA 2]
- ...

NO incluyas estos temas (van en otros módulos):
- [...]

Para cada tema del alcance generá:

1. **Concepto técnico** — definición y fundamento.

2. **Fórmulas / cálculos relevantes** si aplican, con
   variables explicadas.

3. **Normativas mexicanas vigentes** que apliquen (NOM, CFE,
   reglamentos), si el material las menciona.

4. **Proceso paso a paso** de cómo se aplica en campo / oficina.

5. **Errores comunes en la práctica** y cómo evitarlos.

6. **Caso real de aplicación**: empresa mexicana ficticia
   industrial, problema específico, solución correcta.

Al final:

7. **25 flashcards Q/A** técnicas y aplicadas.

8. **6 casos prácticos**: cliente real ficticio + reto + decisión
   técnica correcta + justificación.

9. **5 cálculos resueltos** paso a paso (si el material es
   numérico).

10. **5 errores típicos de instalación / aplicación** con
    explicación de por qué pasa y cómo se previene.

Formato: Markdown. Usá tablas para fórmulas y normativas.
```

### C) Curso de habilidades / soft skills

```
Voy a crear el contenido del [MÓDULO N] de mi guía de estudio
sobre [NOMBRE DEL CURSO] enfocado en aplicación personal.

CONTEXTO: soy [ROL] en [EMPRESA / ÁREA] y quiero aplicar esto
en [SITUACIÓN CONCRETA].

ALCANCE — enfocate SOLO en:
- [FRAMEWORK 1]
- [FRAMEWORK 2]
- ...

Para cada framework / habilidad del alcance generá:

1. **Definición del framework** y por qué importa.

2. **Componentes del modelo** con explicación de cada uno.

3. **Autodiagnóstico**: 4-5 preguntas que el lector se hace
   para evaluar dónde está parado hoy.

4. **Ejercicio práctico** que el lector puede hacer esta
   semana en su contexto laboral.

5. **Antipatrones**: qué hace la gente que NO funciona y
   por qué.

6. **Ejemplo real** de aplicación correcta con narrativa.

Al final:

7. **20 flashcards Q/A** conceptuales y de aplicación.

8. **5 escenarios de decisión**: situación + 4 cursos de acción +
   cuál es el correcto según el framework + por qué.

9. **3 mini-casos**: persona ficticia + reto interpersonal +
   cómo aplicar el framework.

Formato: Markdown. Tono cercano pero profesional.
```

### D) Curso teórico-conceptual

```
Voy a crear el contenido del [MÓDULO N] de mi guía de estudio
sobre [NOMBRE DEL CURSO].

ALCANCE — enfocate SOLO en:
- [TEMA 1]
- [TEMA 2]
- ...

Para cada tema del alcance generá:

1. **Definición rigurosa** con terminología precisa.

2. **Origen / contexto histórico** breve si aplica.

3. **Conceptos relacionados** y cómo se diferencian del
   concepto principal.

4. **Ejemplos canónicos** del material.

5. **Aplicaciones prácticas** del concepto.

6. **Preguntas conceptuales** de comprensión profunda (5).

Al final:

7. **30 flashcards Q/A** conceptuales específicas.

8. **6 pares de conceptos parecidos** que requieren distinguir,
   con la clave de diferenciación.

9. **5 mapas conceptuales en formato lista**: concepto raíz →
   sub-conceptos → conexiones.

Formato: Markdown con jerarquía clara.
```

## Cómo identificar qué tipo de curso es

| Señal | Tipo |
|---|---|
| Hay un examen oficial con código (410-101, etc.) | Certificación |
| Hay normativas, cálculos, instalación física | Técnico aplicado |
| Habla de personas, equipos, comunicación | Habilidades |
| Es teórico puro sin examen | Conceptual |

Si no es claro, **preguntale a Randall directamente** antes de armar el prompt: "¿esto va para certificación con examen, aplicación técnica, soft skills, o teórico?"

## Cómo entregar el prompt

Tras llenar la plantilla, entregalo así:

> Acá tenés el prompt para NotebookLM. Pegalo tal cual:
>
> ```
> [PROMPT COMPLETO LLENADO]
> ```
>
> Una vez que NotebookLM te dé la salida, pegamela acá o subila a
> `source/<curso>/<módulo>/study-guide.md` y yo armo los JSONs de
> las lecciones siguiendo A→B→C→D.

## Reglas para la salida

- **Un solo bloque copiable**: nada de explicaciones dentro del bloque triple-backtick.
- **Variables llenadas**: nunca dejes `[TEMA 1]` literal en lo que le pasás a Randall.
- **Lista de exclusiones es crítica**: sin esto, Notebook genera contenido que pisa otros módulos.
- **Si el material lo amerita**, ajustá las cantidades (20-30 flashcards, 5-10 casos).
- **Si Randall ya te dio el alcance**, no le preguntes de nuevo — usá lo que dijo.

## Estado de cursos (al iniciar la skill, consultá)

Ver `CLAUDE.md` §9 para la lista de cursos y prioridad. Hoy:
- meta-410 — Día 1 listo, Día 2-7 pendiente (tiene PDF oficial — usar approach diferente, esta skill no aplica)
- cfe-interconexion — pendiente (probablemente input transcripciones → SÍ aplica)
- paneles-corella — pendiente (puede tener PDF + transcripciones)
- liderazgo — pendiente (input transcripciones de Guillermo → SÍ aplica)
- itil — pendiente (mix de PDFs y videos)
- cvs — pendiente

**Importante**: para Meta 410, NO usar esta skill — ya está el PDF oficial. Para los demás cursos sí, asumiendo que Randall sube transcripciones a Notebook.
