#!/usr/bin/env python3
"""Protocolo multimedia del Centro de Estudios.

Uso (desde la raíz del repo):
  python3 .claude/skills/multimedia/multimedia.py status
      Inventario: qué unidades con lección recall tienen audio y cuáles no,
      y si cada curso tiene base de conocimiento para el tutor.
  python3 .claude/skills/multimedia/multimedia.py compress <entrada.mp3> <curso> <unidad>
      Comprime a mono 48 kbps en content/<curso>/assets/audio-<unidad>-vN.mp3
      (siguiente versión libre) e imprime ruta, duración y peso.
  python3 .claude/skills/multimedia/multimedia.py insert <curso> <unidad> <ruta-mp3>
      Inserta la tarjeta audio-embed como primera tarjeta de la lección
      <N>.recall, sin reformatear el JSON. Si ya hay una, actualiza su src.
  python3 .claude/skills/multimedia/multimedia.py kb <curso>
      Regenera source/<curso>/tutor/kb-tutor.txt (guiones + respuestas modelo).
"""
import html, json, os, re, subprocess, sys

ROOT = os.getcwd()
MAX_BYTES = 1_000_000

def jload(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)

def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

def units(cid):
    meta = jload(f'content/{cid}/meta.json')
    for u in meta['units']:
        f = f'content/{cid}/{u["id"]}.json'
        if u.get('locked') or not os.path.exists(f):
            continue
        yield meta, u, f, jload(f)

def recall_lesson(d):
    return next((l for l in d.get('lessons', []) if str(l['id']).endswith('.recall')), None)

def guiones(cid):
    p = f'source/{cid}/audio/guiones.md'
    if not os.path.exists(p):
        return {}
    g = open(p, encoding='utf-8').read()
    parts = re.split(r'^## (\S+)\s*$', g, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}

def dur(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                          '-of', 'csv=p=0', path], capture_output=True, text=True).stdout
    return float(out.strip())

def mmss(sec):
    sec = round(sec)
    return f'{sec // 60}:{sec % 60:02d}'

def cmd_status():
    cs = jload('content/courses.json')
    faltan = 0
    for c in cs['courses']:
        cid = c['id']
        if not c.get('active') or not os.path.exists(f'content/{cid}/meta.json'):
            continue
        g = guiones(cid)
        kb = os.path.exists(f'source/{cid}/tutor/kb-tutor.txt')
        print(f'## {cid}  · base del tutor: {"sí" if kb else "NO"}')
        for meta, u, f, d in units(cid):
            rec = recall_lesson(d)
            if not rec:
                continue
            aud = next((k for k in rec['cards'] if k.get('type') == 'audio-embed'), None)
            ok = aud and os.path.exists(aud['src'])
            if not ok:
                faltan += 1
            print(f'   {u["id"]:8} guion={"sí" if u["id"] in g else "NO":2}  audio={"sí" if ok else "NO"}')
    print(f'\nUnidades con recall sin audio: {faltan}')

def cmd_compress(src, cid, uid):
    os.makedirs(f'content/{cid}/assets', exist_ok=True)
    v = 1
    while os.path.exists(f'content/{cid}/assets/audio-{uid}-v{v}.mp3'):
        v += 1
    out = f'content/{cid}/assets/audio-{uid}-v{v}.mp3'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-ac', '1', '-b:a', '48k', out], check=True)
    size = os.path.getsize(out)
    print(f'{out}  {mmss(dur(out))}  {size} B')
    if size > MAX_BYTES:
        sys.exit(f'ERROR: pesa más de 1 MB ({size} B). Acorta el guion.')

def cmd_insert(cid, uid, mp3):
    f = f'content/{cid}/{uid}.json'
    meta = jload(f'content/{cid}/meta.json')
    d = jload(f)
    rec = recall_lesson(d)
    if not rec:
        sys.exit(f'ERROR: {f} no tiene lección .recall')
    if not os.path.exists(mp3):
        sys.exit(f'ERROR: no existe {mp3}')
    s = open(f, encoding='utf-8').read()
    ya = next((k for k in rec['cards'] if k.get('type') == 'audio-embed'), None)
    if ya:
        s2 = s.replace(f'"src": "{ya["src"]}"', f'"src": "{mp3}"', 1)
        s2 = s2.replace(f'"duration": "{ya.get("duration", "")}"', f'"duration": "{mmss(dur(mp3))}"', 1)
    else:
        n = re.sub(r'\D', '', uid) or uid
        etiqueta = 'Día' if meta.get('structure') == 'days' else 'Módulo'
        anchor = f'"id": "{rec["id"]}",'
        i = s.index(anchor)
        m = re.compile(r'\n(\s*)"cards": \[\n').search(s, i)
        ind = m.group(1) + '  '
        card = (f'{ind}{{\n'
                f'{ind}  "type": "audio-embed",\n'
                f'{ind}  "title": "Resumen en audio · {etiqueta} {n}",\n'
                f'{ind}  "src": "{mp3}",\n'
                f'{ind}  "duration": "{mmss(dur(mp3))}",\n'
                f'{ind}  "source": "Escúchalo primero y luego explícalo con tus palabras"\n'
                f'{ind}}},\n')
        s2 = s[:m.end()] + card + s[m.end():]
    json.loads(s2)  # nunca guardar JSON inválido
    open(f, 'w', encoding='utf-8').write(s2)
    print(f'{f}: tarjeta de audio {"actualizada" if ya else "insertada"} → {mp3}')

def cmd_kb(cid):
    cs = {c['id']: c for c in jload('content/courses.json')['courses']}
    meta = jload(f'content/{cid}/meta.json')
    g = guiones(cid)
    out = [f'MATERIAL DE ESTUDIO · {meta.get("title", cid)}', '']
    for _, u, f, d in units(cid):
        rec = recall_lesson(d)
        if not rec:
            continue
        out += [f'=== {d.get("title", u["id"])} ===', '']
        if u['id'] in g:
            out += ['Resumen: ' + g[u['id']], '']
        for k in rec['cards']:
            if k.get('type') != 'recall':
                continue
            out += ['Pregunta: ' + clean(k['q']),
                    'Respuesta modelo: ' + clean(k['model']),
                    'Conceptos clave: ' + ', '.join(k.get('keywords', [])), '']
    os.makedirs(f'source/{cid}/tutor', exist_ok=True)
    p = f'source/{cid}/tutor/kb-tutor.txt'
    open(p, 'w', encoding='utf-8').write('\n'.join(out))
    print(f'{p}  {os.path.getsize(p)} B')

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    {'status': lambda: cmd_status(),
     'compress': lambda: cmd_compress(*a[1:4]),
     'insert': lambda: cmd_insert(*a[1:4]),
     'kb': lambda: cmd_kb(a[1])}[a[0]]()
