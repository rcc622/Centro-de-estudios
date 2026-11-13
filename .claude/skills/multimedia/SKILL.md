---
name: multimedia
description: >
  Protocolo multimedia del Centro de Estudios: resumen en audio (~1 min, ElevenLabs, voz Randy)
  por unidad, tarjeta audio-embed en la lección recall y base de conocimiento del tutor por
  llamada. USAR SIEMPRE que se agregue o reescriba una unidad (día/módulo) con lección
  `<N>.recall`, se cree un curso nuevo, o Randall pida "audios", "multimedia", "tutor",
  "pobla las lecciones", "protocolo multimedia". También al cerrar Tarea A o Tarea B de CLAUDE.md.
---

# Protocolo multimedia (ENCENDIDO por default)

Toda unidad nueva con lección `<N>.recall` sale con su audio y entra a la base del tutor.
No hay que esperar a que Randall lo pida: es el último paso de la Tarea A / Tarea B.

Herramienta: `python3 .claude/skills/multimedia/multimedia.py` (correr desde la raíz del repo).

## Pasos

1. **Inventario:** `multimedia.py status` → lista las unidades con recall sin guion o sin audio.
2. **Guion** en `source/<curso>/audio/guiones.md`, sección `## <unitId>`:
   - Sale SOLO de las respuestas `model` de los `recall` de esa unidad (no meter material nuevo).
   - ~140-170 palabras (≈1 min). Arranca con "Día N:" o "Módulo N:" y el tema.
   - Para voz: números en palabras ("cincuenta eventos"), sin símbolos ni unidades abreviadas
     ("watts por metro cuadrado", no "W/m²"), "Advantage plus" en vez de "Advantage+".
   - Respeta la terminología del curso aunque difiera de la convención común (ej. Corella).
   - Tuteo mexicano, nunca voseo.
3. **Generar** con ElevenLabs MCP: `creative_generate_speech`, `model_id` eleven_v4,
   `voice_id` EQdYdxpkGKpMCC5nZMgi (Randy De Rosas), `generations_count` 1.
   Costo ≈ 850-950 créditos (~$0.16 USD) por audio. Nunca re-llamar para "reintentar":
   cobra otra vez; si sale "concurrency limit", ElevenLabs reintenta solo, sigue haciendo poll.
4. **Descargar** el `content_url` (expira en horas) al scratchpad y comprimir:
   `multimedia.py compress <archivo.mp3> <curso> <unitId>` → `content/<curso>/assets/audio-<unitId>-vN.mp3`.
   Falla si pesa >1 MB.
5. **Insertar:** `multimedia.py insert <curso> <unitId> <ruta-mp3>` → tarjeta `audio-embed`
   como primera tarjeta de `<N>.recall` (o actualiza el src si ya existía). Valida el JSON.
6. **Tutor:** `multimedia.py kb <curso>` regenera `source/<curso>/tutor/kb-tutor.txt`.
   Después de hacer push, en ElevenLabs: crear el documento con `agents_create_kb_url`
   (URL raw de GitHub del archivo, rama `main`), adjuntarlo al agente
   `agent_0701m79qrsa0e1gvcga8sqhj1vdm` con `agents_attach_kb_document`, desadjuntar
   la versión vieja de ese curso si la había, y `agents_publish_draft`.
7. **Verificar:** que el audio cargue en el navegador (duración real, sin error), regresión
   recall, `multimedia.py status` en 0 pendientes.
8. **CLAUDE.md** (sección Multimedia): anotar los IDs de documentos nuevos del tutor.

## Reglas

- Audio: mono 48 kbps, <1 MB, nombre versionado (`-v2` si se regenera, por el caché del service worker).
- Video NUNCA al repo: es caro (~$2.55 por 5 s) y pesado; solo bajo pedido, vía YouTube unlisted + `video-embed`.
- Unidades sin `recall` (glosario, simulacro) no llevan audio.
- El tutor usa SOLO el número de prueba +1 586 328 0753. **Nunca tocar las 4 líneas de Kenet (MVA, MTY, TRC, SLT).**
