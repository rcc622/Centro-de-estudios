# Guiones de los resúmenes en audio · Meta 400-101

Cada guion resume los conceptos que las tarjetas `recall` de ese módulo ya enseñan (sus respuestas modelo están verificadas contra el contenido del módulo), así que no introduce material nuevo. Duración objetivo: alrededor de 60 segundos.

- **Voz:** Randy De Rosas (ElevenLabs, acento mexicano) · `voice_id` EQdYdxpkGKpMCC5nZMgi
- **Modelo:** eleven_v4
- **Archivo final:** `content/meta-400/assets/audio-mN-v1.mp3` (mono, 48 kbps, menos de 1 MB). Si se regenera un audio, súbele la versión al nombre (`-v2`): el service worker sirve `assets/` desde caché sin revalidar.

---

## m1

Módulo uno: del negocio al objetivo de campaña. La regla de oro es que el punto de partida nunca es la plataforma, es el negocio. Primero defines la meta comercial real, luego la ubicas en una etapa del embudo, y hasta el final eliges el objetivo de campaña. Después configuras tres perillas que suenan parecido. La ubicación de la conversión dice dónde ocurre la acción: sitio web, app, mensajes o formulario. El evento de conversión dice qué cuenta como resultado, como una compra o un contacto. Y la meta de rendimiento dice cómo optimiza Meta: más conversiones, más valor o más clics. El objetivo va a nivel campaña; las tres perillas, a nivel conjunto de anuncios. Ojo con la señal: sin Píxel o API de conversiones bien instalada, Meta optimiza a ciegas. Y un plan serio no es una sola campaña: captas arriba del embudo con Reconocimiento o Clientes potenciales, sostienes el interés con Interacción o Tráfico, y cierras con Ventas.

## m2

Módulo dos: tipos de compra y estrategias de puja. Solo hay dos tipos de compra. Subasta es la flexible: compites en tiempo real y tienes todos los objetivos. Reserva es un seguro: pactas alcance, frecuencia y un CPM fijo por adelantado, pero solo para Reconocimiento e Interacción, y puede salir igual o más cara. En la subasta no gana quien pone más dinero, sino el mayor valor total, que combina tres cosas: tu puja, la probabilidad estimada de que la persona haga la acción, y la calidad del anuncio. Por eso mejorar el creativo abarata más que subir la puja. Las estrategias de puja son cinco, en tres familias. Las basadas en gasto: Volumen más alto y Valor más alto. Las basadas en meta: Objetivo de costo por resultado y Objetivo de ROAS. Y la manual: Límite de puja, que si la pones muy baja deja tu campaña sin gastar.

## m3

Módulo tres: presupuesto. El presupuesto diario es un promedio para campañas siempre encendidas, y Meta puede gastar hasta alrededor de veinticinco por ciento más en un buen día. El presupuesto total cubre todo el periodo, y es obligatorio si programas horarios o si compras por Reserva. Luego decides dónde vive el dinero. Con presupuesto de campaña Advantage plus, el famoso CBO, Meta reparte solo entre los conjuntos de anuncios. Con presupuesto por conjunto, el ABO, tú controlas cada monto. Para estimar en Subasta, multiplicas los resultados que quieres por el costo por resultado esperado, y revisas que cada conjunto junte unos cincuenta eventos en siete días para salir del aprendizaje. En Reserva no estimas, calculas: alcance por frecuencia te da las impresiones, y las impresiones por el CPM, entre mil, te dan el presupuesto exacto.

## m4

Módulo cuatro: planeación de audiencia. Hoy el punto de partida es el público Advantage plus: tú das señales y el sistema las usa como sugerencia, con permiso de ir más allá. La audiencia original encierra al pie de la letra, y sigue siendo la correcta cuando hay restricciones legales o de marca. Cuidado con la segmentación detallada: estrechar suma condiciones que se tienen que cumplir a la vez, y cada capa encoge el público hasta que casi no entra a subastas. Mejor pocos intereses y buena señal de conversión. Los públicos personalizados salen de gente que ya te conoce: visitantes del sitio, usuarios de la app, tu lista de clientes hasheada, e interacciones. Tienen tres usos: remarketing, semilla y exclusión. Y el público similar parte de una semilla: el uno por ciento es más preciso y más chico; el diez por ciento llega a más gente, pero se parece menos. Nunca es mejor que su semilla.

## m5

Módulo cinco: ubicaciones y creativo. Las ubicaciones son los espacios donde sale tu anuncio: Feeds, Stories, Reels, videos, Marketplace y Audience Network. El default es Ubicaciones Advantage plus: más superficies significan más subastas y casi siempre un costo menor. Solo restringes con una razón de negocio real. El creativo no es decoración: aunque no cambia tu puja, sube la probabilidad de acción y la calidad del anuncio, y por eso gana subastas sin gastar más. No confundas las dos automatizaciones: creativo Advantage plus cambia cómo se ve el anuncio para cada persona; ubicaciones Advantage plus decide dónde se muestra. La receta es doble: abrir todas las ubicaciones y cargar variedad creativa pensada para celular, vertical, que funcione sin sonido y con la marca al inicio. Un solo creativo en muchas ubicaciones se desgasta rápido, y a eso se le llama fatiga creativa.

## m6

Módulo seis: reportes y medición. No existe una métrica universal: depende de qué querías lograr. Para reconocimiento cuentan el alcance y la recordación; para ventas, el costo por resultado; para ingreso, el ROAS. Los likes y los clics sueltos son métricas de vanidad. La incrementalidad responde lo más honesto: cuántas ventas no habrían pasado sin el anuncio. Para medirla necesitas un grupo de control que no ve tus anuncios. Si el grupo expuesto vendió mil y el de control equivale a seiscientas, el efecto real fueron cuatrocientas. Meta recomienda triangular tres lentes: los experimentos prueban causalidad, la atribución te guía en el día a día, y el modelado de mezcla de marketing compara todos tus canales, incluso los que no son digitales. Y la ventana de atribución solo cambia cómo se reparte el crédito, no cambia una sola venta: dile siempre al cliente cuál estás usando.

## m7

Módulo siete: privacidad y seguridad de marca. La privacidad se diseña desde el plan, con cuatro reglas: consentimiento para usar los datos, listas de clientes hasheadas, nada de segmentar por datos sensibles como salud o religión, y respetar las políticas de Meta y la ley del país. La seguridad de marca evita que tu anuncio salga junto a contenido dañino. El riesgo vive donde convives con contenido de terceros: videos, Audience Network y Reels. Tienes cuatro controles: el filtro de inventario, con tres niveles; las listas de bloqueo; las listas de permitidos; y las exclusiones por tipo de contenido. Entre más estricto, más seguro, pero con menos alcance. Todo anuncio pasa por revisión, que suele tardar unas veinticuatro horas e incluye la página de destino. Y cuidado con la redacción: un anuncio no puede dar a entender que conoce un atributo personal de quien lo ve. Habla del producto, no de la persona.
