# Guiones de los resúmenes en audio · Meta 410-101

Cada guion resume los conceptos que las tarjetas `recall` de ese día ya enseñan (sus respuestas modelo están verificadas contra el contenido del día), así que no introduce material nuevo. Duración objetivo: 60 a 90 segundos.

- **Voz:** Randy De Rosas (ElevenLabs, acento mexicano) · `voice_id` EQdYdxpkGKpMCC5nZMgi
- **Modelo:** eleven_v4
- **Archivo final:** `content/meta-410/assets/audio-dayN-v1.mp3` (mono, 48 kbps, menos de 1 MB). Si se regenera un audio, súbele la versión al nombre (`-v2`): el service worker sirve `assets/` desde caché sin revalidar.

---

## day1

Día uno: cómo está armada una campaña en Meta. Primero, la estructura tiene tres niveles. En la campaña decides qué quieres lograr: el objetivo y el tipo de compra. En el conjunto de anuncios decides a quién, dónde y cuándo: audiencia, ubicaciones y calendario. Y en el anuncio decides cómo se ve: creativo, texto y destino. El presupuesto es la trampa: va en campaña o en conjunto de anuncios, nunca en los dos. Segundo, Advantage plus. Tiene dos familias: las soluciones de campaña completa, que son exactamente tres, Sales, App y Leads; y las de un solo paso, que automatizan una sola pieza, como la audiencia o las ubicaciones. Tercero, el Opportunity Score, de cero a cien. Ojo: no predice tu rendimiento, solo cuenta cuántas recomendaciones de Meta ya aplicaste. Y cuarto, el business portfolio: el contenedor donde repartes accesos sin prestar contraseñas. Si un despacho solo descarga facturas, dale acceso financiero, no control total.

## day2

Día dos: los objetivos de campaña. Meta los organiza con ODAX, experiencias guiadas por resultados, y son seis. Arriba del embudo está Reconocimiento, para que te recuerden. En medio: Tráfico, Interacción, Clientes potenciales y Promoción de la app. Y hasta abajo, Ventas. La pregunta que más cae es Clientes potenciales contra Ventas. La regla es simple: si necesitas datos de contacto para darle seguimiento a alguien, es Clientes potenciales; si necesitas una transacción con cobro, es Ventas. Una clínica que agenda valoraciones gratis está en Clientes potenciales, aunque después venda paquetes caros. Luego, no confundas el evento de conversión con la meta de rendimiento. El evento es qué cuenta como resultado, por ejemplo una compra. La meta es cómo puja Meta: maximizar el número de conversiones, o maximizar su valor. Y un dato que el examen usa mucho: Reconocimiento e Interacción son los únicos dos objetivos que existen en Reservation.

## day3

Día tres: cómo compras y cómo pujas. Hay dos tipos de compra. Auction, la subasta, es la de siempre: el costo fluctúa y tienes todos los objetivos. Reservation compra por adelantado con un CPM fijo, pero solo para Reconocimiento e Interacción. Ahora, ¿quién gana la subasta? No el que pone más dinero, sino el de mayor valor total: tu puja, por la probabilidad de que la persona haga lo que pides, más la calidad del anuncio. Por eso un anuncio relevante con puja modesta le gana a uno genérico. Las estrategias de puja vienen en tres familias: las que gastan todo el presupuesto, como Volumen más alto; las que respetan una meta, como Objetivo de ROAS; y la manual, con el Bid Cap. Si el cliente exige un retorno mínimo de cuatro a uno, es Objetivo de ROAS. Y la fase de aprendizaje: sales de ella con cincuenta eventos de optimización en siete días. Cualquier cambio importante la reinicia desde cero.

## day4

Día cuatro: señales y datos. Una señal es la intención de la persona, como agregar al carrito; el evento es el reporte técnico que le dice a Meta que eso pasó. Hay cuatro fuentes de datos: el Píxel en tu sitio web, la API de conversiones desde tu servidor, el SDK para apps, y las conversiones fuera de línea para lo que pasa en tienda o por teléfono. La pregunta clásica: ¿si ya tengo Píxel, para qué quiero la API de conversiones? Porque el Píxel vive en el navegador y pierde entre diez y treinta por ciento de los eventos por bloqueadores e iOS. La API va de servidor a servidor. Lo recomendado es usar los dos, conectados a un mismo dataset para que no se cuente doble la venta. Distingue también tres cosas: el evento estándar, que ya existe; el personalizado, que inventas tú; y la conversión personalizada, que es solo una regla sobre un evento que ya mandas. Y desde iOS catorce, la medición agregada te limita a ocho eventos por dominio.

## day5

Día cinco: audiencias y catálogos. Un público personalizado es gente que ya te conoce, para retargeting. Un público similar sale a buscar gente nueva parecida a una audiencia fuente; mientras mejor sea esa fuente, mejor resultado. Uno por ciento es más parecido y más chico; diez por ciento llega a más gente pero con menos precisión. Ahora, la diferencia clave de Advantage plus público: los controles son límites duros que nunca se cruzan, como ubicación, idioma y edad mínima; las sugerencias son pistas que la inteligencia artificial puede ampliar, como intereses. Y cuidado al apilar intereses: dentro de la misma categoría se suman, pero entre categorías distintas se cruzan, así que cada categoría nueva achica tu audiencia y te encarece el resultado. Por último, el catálogo vive en Commerce Manager. Lo ideal es uno solo por negocio, dividido con conjuntos de productos. Si la tasa de coincidencia sale baja, casi siempre los identificadores del Píxel no empatan con los del catálogo.

## day6

Día seis: creativo y medición. Hay cuatro formatos de anuncio: Flexible, imagen o video sencillo, carrusel y colección. La Experiencia instantánea es otra cosa: una mini página a pantalla completa dentro de Meta, útil cuando tu sitio carga lento. En ubicaciones, deja Advantage plus: compite por más inventario y suele bajar el costo. Cuida la proporción: nueve por dieciséis para Stories y Reels, cuatro por cinco para el Feed, y respeta la zona segura del centro. Ahora la medición. La atribución decide a qué anuncio le toca el crédito, y la ventana por defecto es un día por visualización y siete días por clic. Y los tres experimentos, que el examen mezcla a propósito: la Prueba A/B compara dos versiones cambiando una sola variable; la Mejora de la marca mide percepción con encuestas; y el Aumento de conversiones mide cuántas ventas extra causó realmente la campaña. Los tres viven en la sección Experiments.
