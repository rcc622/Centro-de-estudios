# source/ — material crudo del que se construye el contenido

Esta carpeta **NO se sirve por GitHub Pages**. Es solo el material fuente
del que Claude extrae el contenido para los JSONs de `content/`.

## Cómo cargar material

Organizá los archivos en subcarpetas según el curso. Para Meta 410-101:

- PDFs oficiales (Blueprint, guías oficiales) → `source/meta-410/oficial/`
- Apuntes / blog posts / notas personales → `source/meta-410/extra/`
- Capturas / imágenes de referencia → `source/meta-410/img/`

### Cómo subir desde GitHub web

1. Andá a https://github.com/rcc622/Centro-de-estudios/tree/main/source/meta-410
2. Botón **Add file → Upload files** (en celular: `+`).
3. Seleccioná los archivos y commiteá con mensaje tipo *"add: material oficial meta 410"*.

### Cómo subir desde Claude Code

1. En el chat, adjuntá los archivos (ícono 📎 / clip).
2. Pedile: *"Guardá estos archivos en `source/meta-410/oficial/` y procesá."*
3. Claude se ocupa de mover, commitear y pushear.

## Convención de nombres

Para que Claude pueda ordenar correctamente, usá prefijo numérico:

```
01-blueprint-overview.pdf
02-campaign-objectives.pdf
03-audience-targeting.pdf
04-creative-best-practices.pdf
...
```

Si los archivos llegan sin ese formato, Claude los renombra al moverlos.

## Cómo pedir que Claude procese el material

Después de subir todo, abrí una sesión y decí algo así:

> "Procesá `source/meta-410/` y armá el plan de estudio con módulos.
> Quiero que propongas la estructura de módulos primero (M1, M2, ...),
> estimes cuántos días por módulo, y después generes los JSONs en
> `content/meta-410/`."

Claude va a:
1. Leer todo lo que haya en `source/meta-410/`.
2. Proponer estructura de módulos (ej: M1 Fundamentos, M2 Campañas, M3 Audiencias, M4 Creativos, M5 Medición, M6 Optimización, M7 Examen).
3. Estimar días por módulo (esperable 20-25 días totales).
4. Generar `meta.json` actualizado y `dayN.json` por cada día.

## Importante

- Esta carpeta puede crecer mucho (PDFs pesados, imágenes). Está bien.
- El motor (`index.html`) **nunca** lee de `source/` — solo lee de `content/`.
- No borres archivos de `source/` aunque ya estén procesados — sirven como referencia para regenerar contenido o agregar lecciones después.
