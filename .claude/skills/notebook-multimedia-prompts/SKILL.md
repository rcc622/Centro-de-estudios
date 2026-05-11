---
name: notebook-multimedia-prompts
description: Genera prompts customizados para NotebookLM enfocados en producir contenido multimedia de calidad — Audio Overviews (podcast), Video Overviews, Mind Maps e infografías — que después se embeben en las lecciones de la app como cards `audio-link`, `video-embed` o `image`. Úsalo cuando Randall mencione "armame el prompt para audio overview del curso X", "quiero un mind map de Notebook para el módulo Y", "necesito generar un video explicativo", o cuando ya tenga el contenido teórico listo y quiera enriquecer la lección con multimedia.
---

# NotebookLM — Prompts para multimedia de calidad

NotebookLM genera audio (podcast 2-voces), mind maps (visuales jerárquicos) y video overviews. Randall usa esto para **enriquecer lecciones que ya tienen el texto**, no para reemplazar el texto. Esta skill produce prompts customizados según el output multimedia deseado y el contexto de uso.

## Default para Coursera (decisión de Randall — confirmada)

**1 audio overview + 1 mind map por CURSO** (no por módulo). Cobertura óptima sin inflar el trabajo:

- Audio (~20 min): repaso del curso entero como podcast — bueno para escuchar mientras maneja
- Mind map: estructura visual del curso con todos los módulos como ramas
- Ambos se embeben en el **primer módulo** del curso:
  - Mind map al inicio (sección A) → card `image`
  - Audio al final (sección D) → card `audio-link`

Si Randall pide explícitamente "por módulo" (más granular), respetar pero advertir el trabajo extra (10-20 audios + 10-20 mindmaps por curso).

## Workflow al activarse

1. **Identificar nivel**: ¿el multimedia es para 1 curso entero (default) o 1 módulo específico (si lo pide)?
2. **Identificar qué multimedia generar**: audio, mind map, video, o varios.
3. **Identificar el alcance**: ¿qué cubre? ¿overview, repaso, casos, examen?
4. **Identificar tono y duración**:
   - Audio: 15-20 min (curso completo) · 10-15 min (módulo) · tono conversacional/didáctico
   - Mind map: nivel de detalle (overview / completo)
   - Video: estructura (intro / explicativo / repaso)
5. **Generar el prompt** llenando la plantilla apropiada.
6. **Entregarlo en bloque copiable** sin texto explicativo dentro del bloque.
7. **Explicar dónde usar la salida**:
   - Audio → subir MP3 a Drive público o YouTube unlisted → card `audio-link`
   - Mind map → descargar PNG → `content/<curso>/assets/curso-overview.png` → card `image`
   - Video → YouTube unlisted → card `video-embed`

## Plantillas por tipo de multimedia

### A) Audio Overview — Podcast didáctico

**Cuándo usar**: para que Randall repase mientras maneja/camina. Va al FINAL del módulo como card `audio-link`.

```
Crea un Audio Overview en español neutro de [DURACIÓN] minutos
sobre [TEMA ESPECÍFICO DEL MÓDULO].

CONTEXTO: estoy preparando el examen [NOMBRE]. Necesito repasar
los conceptos clave de este módulo de forma conversacional pero
densa, para escuchar mientras hago otras cosas.

ENFÓCATE EN:
- Conceptos centrales del tema (no introducción genérica)
- Distinciones críticas entre conceptos parecidos
- Trampas típicas que aparecen en examen
- Ejemplos concretos que ayudan a recordar
- Por qué importa cada concepto, no solo qué es

EVITA:
- Introducciones largas sobre el curso completo
- Repetir información obvia
- Tono motivacional vacío
- Ejemplos genéricos

ESTRUCTURA SUGERIDA:
- 30 seg: gancho rápido — qué van a aprender y por qué importa
- 80% del audio: explicación densa de los conceptos clave en
  formato conversación entre los 2 hosts. Que se hagan preguntas,
  se cuestionen, profundicen.
- Cierre: las 3-5 ideas más importantes para no olvidar

TONO: experto pero accesible, ritmo ágil (no muy lento), ejemplos
prácticos donde aplique.
```

### B) Mind Map — Visual jerárquico

**Cuándo usar**: como card `image` al INICIO del módulo (sección A) para que Randall tenga el "mapa del territorio" antes de zambullirse.

NotebookLM no acepta prompt directo para el mind map (es un botón), pero podés guiarlo poniendo este texto **como nota interna en el notebook** para que el mind map salga enfocado:

```
NOTA INTERNA PARA EL NOTEBOOK (ponela como una "Nota" del notebook,
no como prompt de chat):

Estoy estudiando el módulo "[NOMBRE DEL MÓDULO]" para el examen
[NOMBRE DE CERTIFICACIÓN/CURSO].

Quiero un mind map enfocado en:
- Concepto raíz: [CONCEPTO PRINCIPAL DEL MÓDULO]
- Sub-temas que deben aparecer como ramas:
  · [SUB-TEMA 1]
  · [SUB-TEMA 2]
  · [SUB-TEMA 3]
  · [SUB-TEMA 4]

Quiero que cada sub-tema tenga 3-5 nodos hijos con los detalles
más críticos (no todo el contenido, lo esencial para examen).

Las relaciones importantes entre sub-temas deben verse
visualmente, no solo la jerarquía.

NO incluyas:
- Temas de otros módulos del curso
- Información introductoria general

Después generá el Mind Map desde el panel lateral.
```

Una vez generado, el botón "Mind Map" del panel derecho debería respetar el foco. Descargarlo con click derecho → "Guardar imagen como" → PNG.

### C) Video Overview — Visual explicativo

**Cuándo usar**: cuando un concepto es difícil de explicar en texto y se beneficia del visual + narración. Por ejemplo, procesos de instalación, jerarquías visuales, flujos.

```
Crea un Video Overview de [DURACIÓN] minutos sobre [TEMA
ESPECÍFICO] del curso [NOMBRE].

OBJETIVO: que el espectador entienda visualmente [QUÉ
CONCEPTO/PROCESO]. El texto del módulo ya cubre la teoría —
este video aporta la dimensión visual.

ENFÓCATE EN:
- [CONCEPTO 1]: mostrá visualmente cómo funciona
- [CONCEPTO 2]: usá diagramas/ilustraciones para explicarlo
- [PROCESO X]: representación paso a paso visual
- Relaciones espaciales / jerárquicas que en texto cuesta entender

ESTRUCTURA:
- 20 seg: introducción del problema que el visual resuelve
- 80% del video: visualizaciones acompañadas de narración
  conversacional
- Cierre 20 seg: recap visual de las 3 ideas centrales

EVITA:
- Información que ya está en texto (no repitas el contenido literal)
- Visualizaciones decorativas sin valor explicativo
- Texto en pantalla denso que distrae de la narración
```

### D) Audio Overview enfocado en casos / examen

**Cuándo usar**: la última lección del día como repaso intensivo previo al examen.

```
Crea un Audio Overview en español de [DURACIÓN] minutos
formato "preguntas tipo examen y discusión" sobre [MÓDULO
ESPECÍFICO] de la certificación [NOMBRE].

ESTRUCTURA: que los 2 hosts hagan dinámica de preguntas tipo
examen + discusión.

EJEMPLO DEL FLUJO:
- Host A: "OK, pregunta de examen — selecciona el objective
  correcto si el cliente quiere..."
- Host B responde, explica por qué, y descarta los distractores.
- Host A profundiza en una trampa típica de esa pregunta.
- Pasan a la siguiente pregunta.

GENERÁ [N] preguntas tipo examen sobre [TEMA] que cubran los
conceptos más importantes y las trampas más comunes. Las
preguntas deben tener 4 opciones plausibles.

TONO: como dos compañeros de estudio repasando antes del examen.
Que pongan énfasis en LAS TRAMPAS, no solo en la respuesta.

EVITA: preguntas obvias o de definición pura. Que sean preguntas
aplicadas o de diferenciación entre conceptos parecidos.
```

## Cómo entregar el prompt

Tras llenar la plantilla, entregalo así:

> Acá tenés el prompt para [TIPO DE MULTIMEDIA]. Pegalo en NotebookLM:
>
> ```
> [PROMPT COMPLETO LLENADO]
> ```
>
> **Después de generarlo**:
> - [Si audio] Descargá el MP3 → subilo a Google Drive → compartí público → pasame el link
> - [Si mind map] Descargá el PNG → subilo a `content/<curso>/assets/<modulo>-mindmap.png` o pasámelo
> - [Si video] Subilo a YouTube unlisted → pasame el link
>
> Yo lo embebo en la lección correcta como card `[audio-link / image / video-embed]`.

## Reglas para la salida

- **Un solo bloque copiable**: sin explicaciones dentro del backtick.
- **Variables siempre llenadas**: nunca dejes `[TEMA]` literal.
- **Pedir duración concreta**: 5/10/15/20 min en audio; 3/5/8 min en video.
- **Foco específico es crítico**: sin foco, Notebook hace un overview genérico de todo el material y no sirve para repaso de UN módulo.

## Combinaciones óptimas (default: por curso)

Para un curso Coursera nuevo en la app:

```
content/<id-curso>/m1.json (PRIMER módulo del curso)
├── lección 1.1 (sección A — teoría)
│   ├── [card image]   Mind Map del curso completo
│   ├── concepts, kvtable, etc.
├── lecciones 1.2 ... 1.6 (B, C, D)
└── lección 1.7 (sección D — validación, última del módulo 1)
    └── [card audio-link] Audio Overview del curso completo (~20 min)

content/<id-curso>/m2.json, m3.json, ... (resto de módulos)
└── solo texto/MCQs/etc — no necesitan multimedia adicional
```

**Por qué solo en m1**: el usuario ve el mindmap apenas empieza el curso (orientación) y escucha el audio de cierre cuando termina el primer módulo (repaso panorámico antes de pasar al siguiente). Los módulos siguientes ya tienen el contexto.

Opcional: si el material lo amerita, podés sugerir `video-embed` en módulos específicos para procesos visuales (ej. uso de software, instalaciones).

## Si Randall pide "por módulo" en vez de "por curso"

Confirmar primero el trabajo extra: "10-20 audios + 10-20 mindmaps en NotebookLM, sumando ~3-5 horas de generación. ¿Seguro?".

Si confirma, usar el flujo módulo-por-módulo:

| Card # | Tipo | Multimedia | Cuándo se ve |
|---|---|---|---|
| 1 | `image` | Mind Map del módulo | Inicio sección A |
| Última | `audio-link` (12 min) | Audio Overview del módulo | Final sección D |

## Estado de cursos para multimedia

Ver `CLAUDE.md` §9. Hoy:

- **meta-410** — Día 1 sin multimedia aún. Tiene PDF oficial → ideal para empezar a generar audio + mind map por día desde Notebook con el PDF como source.
- Resto de cursos: pendientes.

## Si Randall solo te pasa "armame un prompt para audio"

Preguntale **lo mínimo** antes de armar:
1. ¿Qué curso?
2. ¿Qué módulo/día específico?
3. ¿Duración? (default sugerí 12 min para repaso)
4. ¿Es de explicación, repaso, o casos de examen?

Con eso suficiente, llená la plantilla A o D según corresponda.
