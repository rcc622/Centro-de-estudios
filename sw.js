// Service Worker — Centro de Estudios Randall
// Estrategia:
//   - Assets multimedia (content/*/assets/, imágenes, audio, video, íconos):
//     CACHE-FIRST puro. Una vez bajados, nunca se re-descargan en background
//     (ahorra datos móviles). Si cambia un asset, cambia su nombre de archivo.
//   - Todo lo demás (index.html, JSONs de contenido): stale-while-revalidate.
//     La 2da carga abre instantáneo desde cache; en background refresca por
//     si hay versión nueva. Si offline, sirve lo cacheado.
//
// Cómo invalidar el cache: bumpear CACHE_VERSION (forces purge en activate).
const CACHE_VERSION = 'cer-v2026-06-24a';

// Lista de assets críticos que se precargan al instalar el SW. La app
// arranca con esto disponible sin red. El resto se cachea on-demand.
// Lazy load: contenido de cursos no-primarios se cachea cuando el usuario
// los abre (no aquí). Solo precacheamos lo del curso primario.
const PRECACHE = [
  './',
  'index.html',
  'manifest.json',
  'icon-192.png',
  'icon-512.png',
  'apple-touch-icon.png',
  'content/courses.json',
  'content/meta-410/meta.json',
  // Starter sprites (uno será visible en cada battle)
  'content/battles/pokemon/25-back.png',
  'content/battles/pokemon/4-back.png',
  'content/battles/pokemon/7-back.png',
  'content/battles/pokemon/1-back.png'
];

// ¿Es un asset inmutable? (multimedia + íconos). Estos se sirven cache-first
// sin revalidación en background.
function isImmutableAsset(pathname){
  if(/\/assets\//.test(pathname)) return true;
  if(/\/content\/battles\//.test(pathname)) return true;
  return /\.(png|jpe?g|webp|gif|svg|ico|m4a|mp3|ogg|wav|mp4|webm|mov)$/i.test(pathname);
}

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_VERSION).then(cache =>
      // allSettled: no fallar el install si algún asset falla
      Promise.allSettled(PRECACHE.map(url => cache.add(url)))
    )
  );
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(names => Promise.all(
        names.filter(n => n !== CACHE_VERSION).map(n => caches.delete(n))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if(e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if(url.origin !== self.location.origin) return;

  e.respondWith(
    caches.open(CACHE_VERSION).then(cache =>
      cache.match(e.request).then(cached => {
        // Assets inmutables: cache-first puro, sin re-descarga en background
        if(isImmutableAsset(url.pathname)){
          if(cached) return cached;
          return fetch(e.request).then(resp => {
            if(resp && resp.ok) cache.put(e.request, resp.clone());
            return resp;
          });
        }
        // Resto: stale-while-revalidate
        const networkFetch = fetch(e.request).then(resp => {
          if(resp && resp.ok) cache.put(e.request, resp.clone());
          return resp;
        }).catch(() => cached);

        // Sirve cache primero (instantáneo). Si no hay, espera red.
        return cached || networkFetch;
      })
    )
  );
});
