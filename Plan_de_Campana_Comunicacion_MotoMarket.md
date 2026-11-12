# Plan de Campaña de Comunicación

**Siete días para que la mayor cantidad de personas descubra qué revelan más de 6.100 anuncios sobre el mercado de motos en Cuba.**

**Autor:** Harold Ricardo Ponce  
**Asignatura:** Introducción a la Ciencia de Datos  
**Institución:** Universidad de La Habana  

---

## 1. EL PRODUCTO

**Descripción**  
MotoMarket Insights Cuba es una plataforma web interactiva de inteligencia de mercado para el sector de las motos en La Habana. Convierte más de 6.100 anuncios públicos y 30 entrevistas de campo en información accionable para compradores, vendedores, talleres, mecánicos, importadoras y emprendedores. Su promesa central es que ninguna persona compre, venda, repare o importe una moto a ciegas.

**URL**  
https://harolric78-lab.github.io/Proyecto-Campa-a-Publicitaria-/ (desplegada en GitHub Pages, rama `main`)

**Repositorios**  
- Campaña y plataforma web: https://github.com/harolric78-lab/Proyecto-Campa-a-Publicitaria-  
- Datos, ETL e informes: https://github.com/harolric78-lab/Mercado-de-Motos  

**Qué contiene**  
- Hero con resumen ejecutivo del mercado y contadores animados (6.101 anuncios, 30 entrevistas, 17 días de captura, 4 categorías).
- KPIs del mercado: volumen de anuncios, entrevistas, días de ventana, categorías, oferta eléctrica y precios medianos.
- Dashboard interactivo con Chart.js: composición por categoría, precio mediano, marcas con más presencia y demanda (vistas promedio).
- Comparador de precios: indica si una oferta es excelente, buena, normal o elevada frente a la mediana del mercado por categoría.
- Calculadora de precio justo por categoría, marca, estado y extras.
- Narrador inteligente con Web Speech API (resumen narrado de los hallazgos).
- Mapa interactivo con los 15 municipios reales de La Habana (polígonos coloreados por cantidad de anuncios, top 3 resaltado, vista de burbujas).
- Ranking animado de marcas y tarjetas de hallazgos compartibles.
- Testimonios de compradores, talleres e importadoras.
- Sección de necesidades detectadas y oportunidades de negocio.
- Timeline de metodología (scraping, limpieza, clasificación, análisis, entrevistas, visualización, informe).
- Quiz de 6 preguntas, reto de marca líder y test de tipo de comprador.
- Diseño oscuro premium, responsive, con microinteracciones y respeto por `prefers-reduced-motion`.

**Cómo se ve**  
Interfaz de tema oscuro con acentos en cian, tipografía Inter y Space Grotesk, grid responsivo, tarjetas de métricas con contadores animados, gráficos de lienzo (canvas) para composición, precios, marcas y demanda, y un mapa de calor de La Habana. Incluye enlace de accesibilidad "Saltar al dashboard", navegación por teclado y foco visible.

---

## 2. OBJETIVOS Y METAS

Metas para los primeros siete días de campaña:

| Métrica | Mínima | Objetivo | Ambiciosa |
|---------|--------|----------|-----------|
| Visitantes únicos a la plataforma | 500 | 1.000 | 2.000 |
| Compartidos orgánicos de tarjetas de dato | 10 | 30 | 60 |
| Tiempo medio de permanencia | 1:30 min | 2:00 min | 3:00 min |
| Sesiones con uso del comparador | 100 | 300 | 600 |
| Seguidores nuevos en Telegram/WhatsApp | 50 | 150 | 300 |
| Descargas del informe y reporte técnico | 5 | 20 | 50 |
| Menciones y respuestas en grupos de moteros | 20 | 60 | 120 |

**Nota de medición:** cada canal se etiqueta con parámetros UTM (`utm_source`, `utm_medium`, `utm_campaign=lanzamiento`) para atribuir visitas a Facebook, Instagram, Telegram, WhatsApp, LinkedIn y GitHub.

---

## 3. PÚBLICO OBJETIVO

**Compradores**  
Personas que buscan moto en La Habana y no saben si el precio que les piden es justo. Dolor principal: pagar de más por falta de referencia pública.

**Propietarios**   dueños de motos eléctricas y de combustión preocupados por batería, autonomía, apagones y repuestos.

**Talleres y mecánicos**  
Negocios que necesitan saber qué vehículos dominan el mercado para especializarse y qué servicios van a crecer (batería, carga, mecánica eléctrica).

**Importadoras**  
Empresas que deciden qué traer al país, a qué precio y para qué segmento de demanda.

**Emprendedores**  
Personas que buscan nichos de negocio claros: alquiler, mensajería, carga compartida, importación de bicicletas y patinetes eléctricos.

**Comunidad tecnológica**  
Desarrolladores, analistas y estudiantes interesados en datos abiertos, scraping, observatorios digitales y ciencia de datos aplicada.

**Estudiantes**  
Alumnos de la Universidad de La Habana y otros centros que necesitan un caso real y reproducible de análisis de mercado con datos públicos.

---

## 4. EL MENSAJE

**Mensaje principal**  
El mercado de motos en Cuba se mueve a ciegas: no existe un observatorio público de precios, oferta y demanda. MotoMarket Insights Cuba convierte más de 6.100 anuncios y 30 entrevistas en datos claros para decidir mejor al comprar, vender, reparar o importar.

**Eslogan principal**  
"Decisiones sobre ruedas, con datos."

**Eslóganes alternativos**  
1. "El mercado de motos, por fin en datos."  
2. "Antes de comprar, míralo en datos."  
3. "Datos que valen una moto."  
4. "Conduce con información, no con rumores."  
5. "El observatorio de las motos en Cuba."  
6. "6.101 anuncios. Una sola verdad: el mercado habla."

**Tono de comunicación**  
Directo, útil, con autoridad técnica y cercano al habla cubana. Nunca académico, nunca frío. Cada pieza comunica un descubrimiento concreto respaldado por datos, no una promoción vacía de la plataforma.

---

## 5. LOS GANCHOS PRINCIPALES

Estos seis ganchos son el corazón de la campaña. Se construyen exclusivamente a partir de hallazgos respaldados por datos del proyecto (dataset de Revolico, entrevistas de campo, dashboard y reporte técnico). Ningún resultado está inventado.

### Gancho 1. "El promedio mentía"

**Hallazgo**  
La mediana de una moto de combustión es 2.250 USD, mientras que una moto eléctrica cuesta 2.050 USD. La combustión es más cara que la eléctrica, rompiendo el mito de que lo eléctrico es inaccesible.

**Evidencia**  
Dashboard: precio mediano por categoría (combustión 2250 USD, moto eléctrica 2050 USD). Rango típico combustión 1.900–2.600 USD; eléctrica 1.300–2.630 USD.

**Por qué funciona**  
Desafía una creencia extendida sin atacar directamente a nadie. Invita a comprobarlo con el comparador.

**Potencial de viralización**  
Alto. Es un dato contraintuitivo ideal para titular de publicación y carrusel de Instagram.

**Público objetivo**  
Compradores, propietarios, emprendedores.

---

### Gancho 2. "Menos oferta, más interés"

**Hallazgo**  
La combustión tiene menos oferta que la eléctrica, pero genera más del cuádruple de interés por anuncio: 60.8 vistas promedio por anuncio de combustión frente a 14.9 en eléctricas.

**Evidencia**  
Dashboard: demnda (vistas promedio) — combustión 60.8, bicicletas eléctricas 27.4, motos eléctricas 14.9, patinetes 9.2. Composición: combustión 1.099 anuncios vs bicicletas eléctricas 2.576.

**Por qué funciona**  
Plantea una pregunta incómoda: si hay menos combustión, ¿por qué se mira más? Genera debate sobre qué busca realmente el comprador cubano.

**Potencial de viralización**  
Muy alto. Identificado en el kit de campaña como el gancho más fuerte para usar como titular.

**Público objetivo**  
Compradores, vendedores, importadoras, emprendedores.

---

### Gancho 3. "Casi la mitad no dice su marca"

**Hallazgo**  
El 47,7% de los anuncios no declara marca. Solo cinco marcas concentran la presencia publicada: Topmaq (506 anuncios), JMD (227), Mountain (187), Vedca (173) y Challenger (170).

**Evidencia**  
Dashboard: marcas con más presencia. Pie de página del ranking: "El 47,7% de los anuncios no declara marca".

**Por qué funciona**  
Desnuda una opacidad del mercado: casi la mitad de la oferta es anónima en cuanto a marca. Posiciona a la plataforma como quien ordena lo confuso.

**Potencial de viralización**  
Medio-alto. Funciona bien como tarjeta de dato con número grande (47,7%).

**Público objetivo**  
Importadoras, talleres, compradores, emprendedores.

---

### Gancho 4. "Lo que importa no aparece en el anuncio"

**Hallazgo**  
Los verdaderos dolores del comprador y el propietario no están en el título del anuncio: batería, autonomía, apagones, repuestos y papeles. La autonomía real varía según peso, velocidad y terreno; los apagones afectan la decisión de carga y compra.

**Evidencia**  
Sección de necesidades detectadas y testimonios del sitio web ("En ocasiones no puedo usar la moto por el apagón", "La autonomía anunciada era real, pero ha perdido con el tiempo"). Metodología: 25 compradores, 4 talleres y 1 importadora entrevistados.

**Por qué funciona**  
Conecta con la experiencia vivida del usuario cubano, no con cifras frías. Genera reconocimiento inmediato.

**Potencial de viralización**  
Alto. Ideal para historias de Instagram/Telegram con frases reales de compradores y talleres.

**Público objetivo**  
Propietarios, compradores, talleres, mecánicos.

---

### Gancho 5. "Eléctrico domina la oferta, no la atención"

**Hallazgo**  
El 78,3% de la oferta observada en La Habana es eléctrica (motos + bicicletas), pero las eléctricas generan menos interés por anuncio que la combustión.

**Evidencia**  
Hero y dashboard: oferta eléctrica 78,3%. Composición: bicicletas eléctricas 2.576, motos eléctricas 2.201, combustión 1.099, patinetes 225. Demanda: combustión 60.8 vistas vs motos eléctricas 14.9.

**Por qué funciona**  
Muestra una contradicción del mercado: hay mucha oferta eléctrica, pero el comprador sigue mirando más la combustión. Útil para talleres e importadoras que decidan apostar por uno u otro segmento.

**Potencial de viralización**  
Medio. Dato de autoridad para importadoras y emprendedores.

**Público objetivo**  
Importadoras, talleres, emprendedores, vendedores.

---

### Gancho 6. "Antes de pagar, compáralo"

**Hallazgo**  
El comparador de la plataforma permite introducir categoría y precio y saber al instante si la oferta es excelente, buena, normal o elevada, usando los percentiles 25, 50 y 75 de cada categoría.

**Evidencia**  
Herramienta "Comparador de precios" del sitio web. Referencia: medianas publicadas en Revolico (octubre 2026).

**Por qué funciona**  
No vende la plataforma; vende la utilidad inmediata. Resuelve un problema real en cinco segundos. Es la pieza que más se reenvía en grupos de WhatsApp.

**Potencial de viralización**  
Muy alto. Utilidad directa y comprobable por el usuario en el momento.

**Público objetivo**  
Compradores, vendedores, propietarios.

---

## 6. CANALES

**WhatsApp**  
Rol: difusión de utilidad inmediata en grupos de moteros, talleres y círculos familiares. Es el canal con mayor tasa de reenvío en Cuba para el comparador de precios. Pieza clave: mensaje corto con enlace directo al comparador.

**Facebook**  
Rol: alcance masivo y lanzamiento. Publicaciones para el público general (dato del 78,3% eléctrico), para talleres e importadoras (necesidades y servicios con demanda), y para compradores (comparador). Público amplio y heterogéneo.

**Telegram**  
Rol: comunidad técnica y observatorio. Mensajes directos con el comparador, la calculadora y el mapa de actividad. Canal idóneo para compartir el informe técnico y el reporte con audiencia interesada en datos.

**Instagram**  
Rol: narrativa visual y hallazgos compartibles. Carrusel de 5 tarjetas (6.101 anuncios, 78,3% eléctrico, Topmaq 506, mediana 2.250, precio justo), reels del comparador en 5 segundos y dato del día. Público joven y compradores activos.

**LinkedIn**  
Rol: credibilidad profesional y B2B. Importadoras, emprendedores y comunidad tecnológica. Publicar el enfoque de ciencia de datos, metodología reproducible y oportunidades de negocio detectadas.

**GitHub**  
Rol: transparencia y credibilidad académica. Repositorio público del código y de los datos (Mercado-de-Motos). Permite auditar el scraping, la limpieza y el ETL. Enlace en el pie de página de la plataforma y en piezas de comunidad tecnológica.

---

## 7. PREPARACIÓN

**Piezas visuales necesarias (antes del día 1)**  
- Tarjetas de dato 1080×1080 con número grande y una línea de contexto (78,3% eléctrico, Topmaq 506, mediana 2.250, 47,7% sin marca).  
- Captura del dashboard con la categoría eléctrica resaltada.  
- Captura del comparador mostrando "Precio elevado" y "Oferta excelente".  
- Mapa de calor de La Habana con leyenda y aviso de simulación (el dataset no contiene municipios para todos los anuncios).  
- Carrusel de 5 tarjetas con un hallazgo por tarjeta.

**Copies aprobados**  
Todos los textos por canal (Facebook, Instagram, Telegram, WhatsApp, X) están definidos en `campana.md` y deben revisarse antes del lanzamiento, reemplazando `TU-DOMINIO` por la URL final: `https://harolric78-lab.github.io/Proyecto-Campa-a-Publicitaria-/`.

**Hashtags**  
Núcleo: #MotoMarketCuba #MercadoDeMotos #MotosCuba #LaHabana #MovilidadCuba  
Compra y venta: #ComprarMoto #VenderMoto #PreciosDeMotos #OfertasDeMotos  
Sector: #Talleres #Mecanica #MotosElectricas #BicicletasElectricas #Importacion #EmprendimientoCuba  
Datos: #DatosAbiertos #InteligenciaDeMercado #DataAnalytics #ObservatorioDigital  
Regla de uso: entre 5 y 10 por publicación, mezclando 2 de núcleo, 2 de sector y 1 de datos.

**Enlaces y UTMs**  
Un solo enlace por publicación (no dividir la atención):  
- Facebook: `.../?utm_source=facebook&utm_medium=social&utm_campaign=lanzamiento`  
- Instagram: `.../?utm_source=instagram&utm_medium=social&utm_campaign=lanzamiento`  
- Telegram: `.../?utm_source=telegram&utm_medium=social&utm_campaign=lanzamiento`  
- WhatsApp: `.../?utm_source=whatsapp&utm_medium=social&utm_campaign=lanzamiento`

**Transparencia y limitaciones (mencionar siempre)**  
- Los datos representan oferta publicada en Revolico, no ventas efectivas.  
- Ventana de captura: 17 días (10 al 26 de octubre de 2026).  
- El mapa de calor es una simulación visual; el dataset no contiene municipios para la mayoría de anuncios.  
- Solo el 1,70% de los anuncios (105/6.159) tiene municipio identificable.  
- Las estimaciones de precio son orientativas y no sustituyen una inspección técnica.  
- La muestra cualitativa es pequeña y no probabilística.

**Pruebas previas al lanzamiento**  
- Abrir `index.html` en móvil y escritorio; verificar enlaces, portapapeles y narración Web Speech API.  
- Confirmar que los parámetros UTM llegan a la plataforma.  
- Verificar despliegue en GitHub Pages (Settings → Pages, rama `main`, carpeta `/`).  
- Preparar calendario de publicación con responsables por canal.

---

## 8. CRONOGRAMA DE 7 DÍAS

### Día 1 — Lanzamiento: "El mercado habla en datos"
- **Objetivo:** dar a conocer la plataforma y lograr las primeras 500 visitas.
- **Mensaje:** "¿Cuánto cuesta realmente una moto en La Habana? Lanzamos MotoMarket Insights Cuba, el primer observatorio digital del mercado de motos. Analizamos 6.101 anuncios y 30 entrevistas para que compres, vendas o repares con datos, no con rumores."
- **Hallazgo protagonista:** 78,3% de la oferta observada en La Habana es eléctrica.
- **Canales:** Facebook + Instagram.
- **Formato:** Reel de lanzamiento + carrusel de 5 tarjetas.
- **CTA:** Visitar la plataforma.

### Día 2 — Comparador: "¿Estás pagando de más?"
- **Objetivo:** que al menos 100 usuarios usen el comparador de precios.
- **Mensaje:** "Te piden 2.600 USD por una eléctrica. ¿Es caro? En segundos puedes saber si estás pagando de más, comparar con la mediana del mercado y negociar con argumentos."
- **Hallazgo protagonista:** la mediana de combustión es 2.250 USD y la de eléctrica, 2.050 USD.
- **Canales:** Telegram + WhatsApp.
- **Formato:** Mensaje directo + enlace al comparador.
- **CTA:** "Prueba el comparador gratuito".

### Día 3 — Marcas: "Casi la mitad no dice su marca"
- **Objetivo:** generar 20 compartidos del hallazgo de marcas.
- **Mensaje:** "El 47,7% de los anuncios no declara marca. Topmaq lidera con 506 anuncios, seguido de JMD, Mountain, Vedca y Challenger. Conoce quiénes dominan realmente el mercado."
- **Hallazgo protagonista:** concentración de marcas y opacidad en casi la mitad de la oferta.
- **Canales:** Instagram.
- **Formato:** Carrusel Top 5 marcas (Topmaq, JMD, Mountain, Vedca, Challenger).
- **CTA:** Compartir el hallazgo.

### Día 4 — Talleres e importadoras: "Qué vehículos dominan y qué servicios crecerán"
- **Objetivo:** atraer a 30 talleres e importadoras a probar el dashboard.
- **Mensaje:** "Si tienes un taller o importas vehículos, esto te interesa: el 78,3% de la oferta es eléctrica y la demanda de servicios de batería no deja de crecer. Descubre qué vehículos dominan y dónde están los nichos."
- **Hallazgo protagonista:** oferta eléctrica dominante (78,3%) y oportunidades de servicio de batería y carga.
- **Canales:** Facebook.
- **Formato:** Publicación orientada a talleres e importadoras.
- **CTA:** Probar el dashboard.

### Día 5 — Quiz: "¿Cuánto sabes del mercado de motos?"
- **Objetivo:** 100 participaciones en el quiz y 20 retos entre amigos.
- **Mensaje:** "Seis preguntas, retroalimentación inmediata y puntuación final. Demuestra cuánto sabes del mercado de motos en La Habana. ¿Eres experto o compras a ciegas?"
- **Hallazgo protagonista:** la combustión genera 60,8 vistas promedio por anuncio frente a 14,9 en eléctricas (menos oferta, más interés).
- **Canales:** Instagram + X (Twitter).
- **Formato:** Quiz interactivo de 6 preguntas con reto de etiquetar a un amigo.
- **CTA:** Retar a un amigo y comparar resultados.

### Día 6 — Voces reales: "Lo que los números no alcanzan a contar"
- **Objetivo:** 50 respuestas o menciones en grupos de compradores y talleres.
- **Mensaje:** "30 entrevistas de campo entre octubre y noviembre de 2026. 'En ocasiones no puedo usar la moto por el apagón'. 'El avance se inclina hacia los equipos eléctricos'. Escucha las voces del mercado."
- **Hallazgo protagonista:** dolores reales — batería, autonomía, apagones, repuestos y papeles — que no aparecen en los anuncios.
- **Canales:** Telegram + Facebook.
- **Formato:** Testimonio de compradores, talleres e importadoras + dato del apagón.
- **CTA:** Escuchar la narración de la plataforma.

### Día 7 — Resumen y comunidad: "Guarda y comparte lo que descubrimos esta semana"
- **Objetivo:** cerrar la semana con 1.000 visitas acumuladas y crear hábito de retorno.
- **Mensaje:** "Siete días, seis hallazgos, una sola verdad: el mercado de motos en Cuba habla en datos. Guarda las mejores tarjetas y compártelas con quien va a comprar o vender una moto."
- **Hallazgo protagonista:** recopilación de los mejores hallazgos de la semana (el promedio mentía, menos oferta más interés, casi la mitad sin marca, eléctrico domina oferta no atención).
- **Canales:** Todos (Facebook, Instagram, Telegram, WhatsApp, LinkedIn, GitHub).
- **Formato:** Resumen semanal + llamado a guardar y compartir.
- **CTA:** Guardar y compartir los hallazgos de la semana.

---

**Fin del documento.**  
Todos los hallazgos, cifras y copias se extraen exclusivamente de los archivos del repositorio `Proyecto-Campa-a-Publicitaria-` (`index.html`, `README.md`, `campana.md`) y del repositorio de datos `Mercado-de-Motos`. No se inventa ningún resultado.
