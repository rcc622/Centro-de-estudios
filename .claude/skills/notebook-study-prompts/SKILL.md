---
name: notebook-study-prompts
description: Genera prompts customizados para NotebookLM que producen Study Guides densos a partir de transcripciones de video, PDFs no estructurados, apuntes propios o cualquier .txt que Randall suba. Diseñado para el flujo Coursera (especialización → curso → módulo). Úsalo cuando Randall mencione "tengo transcripciones / .txt / apuntes para el curso X", "armame el prompt para generar el Study Guide del módulo Y", "necesito que NotebookLM me dé contenido denso", o cuando arranque una especialización Coursera nueva.
---

# NotebookLM — Prompts para Study Guides densos

Randall sube material crudo (transcripciones de Coursera, apuntes, .txt) a NotebookLM y necesita prompts específicos según el tipo de curso para que la salida sea contenido pedagógico de calidad. Esta skill produce esos prompts.

## Jerarquía Coursera → app (importante)

Randall estudia en Coursera y la jerarquía real es:

```
Especialización (5 cursos)
└── Curso (10-20 módulos)
    └── Módulo (varios videos .txt)
        └── Video (transcripción .txt)
```

Mapeo a la app:

| Coursera | App |
|---|---|
| Especialización | Etiqueta visual agrupadora en home (`specialization` en courses.json) |
| 1 Curso | 1 carpeta en `content/<id-curso>/` con su meta.json |
| 1 Módulo | 1 unit/día dentro de meta.json (5-7 lecciones A→B→C→D) |
| 1 Video | Material fuente, NO se mapea 1:1 |

## Estructura de notebook óptima (regla de oro)

**1 notebook = 1 curso Coursera entero**. NO uno por módulo, NO uno por especialización.

- Subir TODOS los .txt de TODOS los módulos del curso al mismo notebook
- Notebook ve el curso completo → entiende conexiones entre módulos y evita repetir
- Hacés N consultas en ese notebook (1 prompt por módulo, todas con foco específico + exclusiones)

Por qué no "1 notebook por módulo":
- Notebook no ve el contexto del curso entero → puede repetir o pisar otros módulos
- Más notebooks que mantener

Por qué no "1 notebook por especialización":
- Satura el límite de fuentes (~50 docs gratis, ~300 Pro)
- Calidad baja al diluir el contexto

## Estructura de archivos en el repo

```
source/
└── <id-especializacion>/               # ej. google-data-analytics
    ├── README.md                       # qué es la especialización, cursos contenidos
    ├── <id-curso-1>/                   # ej. 1-foundations-data
    │   ├── transcripciones/            # los .txt originales de Coursera
    │   │   ├── m1-v1-intro.txt
    │   │   ├── m1-v2-...txt
    │   │   ├── m2-v1-...txt
    │   │   └── ...
    │   ├── m1/                         # outputs Notebook para módulo 1
    │   │   ├── study-guide.md
    │   │   ├── mindmap.png             # opcional (ver multimedia skill)
    │   │   └── audio-link.txt          # opcional
    │   ├── m2/
    │   └── ...
    └── <id-curso-2>/
        └── ...
```

## Workflow al activarse

1. **Identificar nivel**: ¿estamos armando prompt para 1 curso entero (poco común) o 1 módulo específico (lo normal)?
   - Default: 1 módulo. Es la unidad pedagógica óptima.

2. **Identificar el tipo de curso**:
   - **Certificación con examen** (ej. Meta 410, ITIL) → preguntas tipo examen, distractores plausibles
   - **Técnico aplicado** (ej. Interconexión Solar, Coursera Google Data) → cálculos, casos reales, normativas
   - **Habilidades / soft skills** (ej. Liderazgo) → frameworks, autodiagnóstico, ejercicios
   - **Teórico-conceptual** (ej. CVS) → definiciones, contraste, ejemplos

3. **Identificar el alcance específico del módulo**:
   - Qué temas SÍ cubre (lista)
   - Qué temas NO cubre (lista de exclusiones — crítico para evitar overlap con otros módulos del MISMO curso)

4. **Generar el prompt** llenando la plantilla apropiada.

5. **Entregar el prompt en bloque copiable** — sin texto explicativo dentro del backtick.

6. Decirle qué hacer con la salida:
   - Pegarla acá, o
   - Subirla a `source/<especializacion>/<curso>/<modulo>/study-guide.md`

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
- **meta-410** — Día 1 listo. **PDF oficial → esta skill NO aplica**, leer el PDF directo.
- **Coursera especializaciones futuras** — SÍ aplica esta skill (transcripciones .txt)
- **cfe-interconexion**, **paneles-corella**, **liderazgo**, **itil**, **cvs** — depende del input que tenga Randall (PDF vs transcripciones)

## Cómo decidir si esta skill aplica

| Material de Randall | ¿Esta skill? |
|---|---|
| PDF oficial estructurado de la certificación | NO — leer el PDF directo |
| Transcripciones de Coursera (.txt por video) | SÍ — esta skill |
| Apuntes propios (.md, .txt) sueltos | SÍ — esta skill |
| Mix de PDF + transcripciones | Depende — si el PDF es completo, usarlo; si es parcial, mezclar |
