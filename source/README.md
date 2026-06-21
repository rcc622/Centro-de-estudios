# source/ — Bases de conocimiento (material crudo)

Aquí Randall sube el material original de cada curso: guías oficiales,
transcripciones, temarios, PDFs, etc. Es el **input**. El **output** jugable
vive en `content/<curso>/`.

## Cómo subir material

1. Entra a la carpeta del curso correspondiente (`source/<id-curso>/`).
2. Sube el archivo dentro de `oficial/` (guías oficiales) o crea la subcarpeta
   que tenga sentido (`transcripciones/`, `temario/`, etc.).
3. Nombra los archivos de forma clara (ver convención abajo).
4. Avísale a Claude qué subiste y a qué curso pertenece.

## Convención de nombres para guías oficiales

Para que el bilingüe quede con los términos correctos, sube **una guía por
idioma**:

- `<curso>-guia-oficial-es.<ext>` — guía oficial en **español**
- `<curso>-guia-oficial-en.<ext>` — guía oficial en **inglés**

Ejemplo para Meta Media Buying 410:
- `source/meta-410/oficial/410-guia-oficial-es.pdf`
- `source/meta-410/oficial/410-guia-oficial-en.pdf`

## Política de peso (ver CLAUDE.md §9)

- PDFs **> 5 MB**: NO se commitean al repo. Claude los convierte a Markdown con
  MarkItDown y commitea solo el `.md` (mucho más liviano). El PDF original se
  queda en tu dispositivo / Drive.
- PDFs **< 5 MB**: se pueden quedar en el repo sin problema.
- Claude siempre genera el `.md` en la misma carpeta `oficial/` para que las
  sesiones futuras no tengan que reconvertir.

## Cursos

| id-curso     | Curso                                | Carpeta                    |
|--------------|--------------------------------------|----------------------------|
| `meta-410`   | Meta Media Buying Professional 410   | `source/meta-410/`         |
| `meta-400`   | Meta Media Planning Professional 400 | `source/meta-400/`         |

> ¿Curso nuevo? Crea `source/<id-curso>/oficial/` y sube ahí su material.
