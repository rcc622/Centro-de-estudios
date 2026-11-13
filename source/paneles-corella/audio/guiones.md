# Guiones de los resúmenes en audio · Sistemas Fotovoltaicos (Corella)

Cada guion resume los conceptos que las tarjetas `recall` de ese módulo ya enseñan (sus respuestas modelo están verificadas contra el contenido del módulo), así que no introduce material nuevo. Duración objetivo: alrededor de 60 segundos.

- **Voz:** Randy De Rosas (ElevenLabs, acento mexicano) · `voice_id` EQdYdxpkGKpMCC5nZMgi
- **Modelo:** eleven_v4
- **Archivo final:** `content/paneles-corella/assets/audio-mN-v1.mp3` (mono, 48 kbps, menos de 1 MB). Si se regenera un audio, súbele la versión al nombre (`-v2`).
- **Ojo con la terminología:** el curso sigue la convención del libro (irradiación = potencia instantánea en W/m²; irradiancia = energía del día en kWh/m²/día). El guion respeta esa convención para no contradecir las lecciones.

---

## m1

Módulo uno: del Sol a la electricidad. Primero, dos palabras que se confunden. En este curso, la irradiación es la potencia de un instante, en watts por metro cuadrado, y la irradiancia es la energía acumulada en el día, en kilowatts hora por metro cuadrado. Para el recibo de luz importa la irradiancia. En México los módulos van hacia el sur, con una inclinación parecida a la latitud del sitio; si el techo no ayuda, calculas las pérdidas y agregas uno o dos módulos. Dentro de la celda, el silicio se dopa para formar la unión P N: la luz libera electrones y el campo eléctrico los empuja en un solo sentido. La curva de corriente y tensión tiene un punto de máxima potencia que se mueve con el sol y la temperatura. Con frío sube la tensión, así que revisa el amanecer helado para no rebasar lo que aguanta el inversor. Y para estimar generación: potencia nominal por horas solares pico. Ojo: las horas solares pico no son las horas de luz.
