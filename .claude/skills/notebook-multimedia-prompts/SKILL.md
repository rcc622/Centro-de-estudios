---
name: notebook-multimedia-prompts
description: Genera prompts customizados para NotebookLM enfocados en producir contenido multimedia de calidad — Audio Overviews (podcast), Video Overviews, Mind Maps e infografías — que después se embeben en las lecciones de la app como cards `audio-link`, `video-embed` o `image`. Úsalo cuando Randall mencione "armame el prompt para audio overview del curso X", "quiero un mind map de Notebook para el módulo Y", "necesito generar un video explicativo", o cuando ya tenga el contenido teórico listo y quiera enriquecer la lección con multimedia.
---

# NotebookLM — Prompts para multimedia de calidad

NotebookLM genera audio (podcast 2-voces), mind maps (visuales jerárquicos) y video overviews. Randall usa esto para **enriquecer lecciones que ya tienen el texto**, no para reemplazar el texto. Esta skill produce prompts customizados según el output multimedia deseado y el contexto de uso.

## Workflow al activarse

1. **Identificar qué multimedia querés generar**: audio, mind map, video, o varios.
2. **Identificar el alcance**: ¿qué tema/módulo cubre? ¿es para repaso, para introducción, para casos aplicados?
3. **Identificar el tono y duración**:
   - Audio: 5/10/15/20 min · tono conversacional/didáctico/intensivo
   - Mind map: nivel de detalle (overview / completo / específico)
   - Video: estructura (intro / explicativo / repaso)
4. **Generar el prompt** llenando la plantilla apropiada.
5. **Entregarlo en bloque copiable** sin texto explicativo dentro del bloque.
6. **Explicar dónde usar la salida**:
   - Audio → subir MP3 a Drive público o YouTube unlisted → card `audio-link`
   - Mind map → descargar PNG → `content/<curso>/assets/` → card `image`
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

## Combinaciones óptimas por módulo

Para un módulo nuevo de la app, lo ideal:

| Card # | Tipo | Multimedia | Cuándo se ve |
|---|---|---|---|
| 1 | `image` (mind map) | Mind Map del módulo | Inicio sección A (Teoría) |
| ... | concept / kvtable / etc | (texto del PDF/study guide) | Resto de la lección |
| Última | `audio-link` (12 min) | Audio Overview repaso | Final sección D (Validación) |

Opcional si el material lo amerita: `video-embed` en sección C (Aplicación) para procesos visuales.

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
