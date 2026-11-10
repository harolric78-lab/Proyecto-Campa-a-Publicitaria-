# MotoMarket Insights Cuba

Plataforma web de inteligencia de mercado para el sector de las motos en Cuba. Convierte 6.159 anuncios públicos y 30 entrevistas de campo en datos accionables para compradores, talleres, mecánicos, importadoras y emprendedores.

**Sitio:** pendiente de despliegue · **Datos:** [Mercado-de-Motos](https://github.com/harolric78-lab/Mercado-de-Motos)

## Qué incluye

- Hero con resumen ejecutivo del mercado y contadores animados.
- KPIs del mercado: anuncios, entrevistas, días, categorías, oferta eléctrica y precios medianos.
- Dashboard interactivo con Chart.js: composición, precios, marcas y demanda.
- Comparador de precios: indica si una oferta es excelente, buena, normal o elevada.
- Calculadora de precio justo por categoría, marca, estado y extras.
- Narrador inteligente con Web Speech API.
- Mapa interactivo con los 15 municipios reales de La Habana: polígonos coloreados por cantidad de anuncios, top 3 resaltado y vista alternativa de burbujas.
- Ranking animado de marcas y tarjetas de hallazgos compartibles.
- Testimonios de compradores, talleres e importadoras.
- Necesidades, oportunidades, timeline de metodología y sección de transparencia.
- Quiz de 6 preguntas, reto de marca líder y test de tipo de comprador.
- Diseño oscuro premium, responsive, con microinteracciones y respeto por `prefers-reduced-motion`.

## Stack

- HTML5 semántico.
- CSS3 con variables, grid, animaciones y media queries.
- JavaScript puro, sin frameworks.
- Chart.js 4 para visualizaciones.
- Leaflet 1.9 para geointeligencia y tiles de OpenStreetMap sin API key.
- Web Speech API para narración.
- Google Fonts: Space Grotesk e Inter.

## Estructura

```text
Proyecto de campana publicitaria/
├── index.html           # Estructura y contenido de la plataforma
├── style.css            # Tema visual, layout y responsive
├── script.js            # Datos, gráficos e interactividad
├── mapa_datos.js        # Métricas reales por municipio
├── mapa_municipios.js   # Polígonos GeoJSON de los 15 municipios
├── datos_mapa/
│   ├── anuncios_georreferenciados.csv
│   ├── municipios_georreferenciacion.csv
│   ├── municipios_geometrias.geojson
│   ├── resumen_municipios.csv
│   └── resumen_municipios.json
├── campana.md           # Kit de campaña y calendario de publicación
└── README.md            # Este documento
```

## Ejecutar en local

No requiere build ni instalación de dependencias. Abre `index.html` en el navegador o levanta un servidor estático:

### Python

```bash
python -m http.server 8000
```

Luego visita `http://localhost:8000`.

### Node

```bash
npx serve .
```

Usar un servidor local es recomendable para que el portapapeles y algunas APIs funcionen con un origen seguro.

Comandos de ejemplo:

```bash
git add index.html style.css script.js mapa_datos.js mapa_municipios.js datos_mapa campana.md README.md
git commit -m "Lanza plataforma MotoMarket Insights Cuba"
git push origin main
```

## Publicar en Netlify

**Opción arrastrar y soltar:** entra en [netlify.com](https://www.netlify.com), crea un sitio y arrastra la carpeta completa. Netlify detecta `index.html` automáticamente.

**Opción CLI:**

```bash
npm install -g netlify-cli
netlify deploy --prod --dir .
```

**Opción Git:** conecta el repositorio, deja el comando de build vacío y el directorio de publicación en `/`.

## Publicar en Vercel

**Opción CLI:**

```bash
npm install -g vercel
vercel --prod
```

Cuando pregunte por el framework, elige **Other**. Directorio de salida: `.` y sin build.

**Opción Git:** importa el repositorio en [vercel.com/new](https://vercel.com/new), framework **Other**, build vacío y output `.`.

## Configuración

- **Datos del mercado:** edita `MEDIANS` y `MARKET` al inicio de `script.js`.
- **Preguntas del quiz:** edita el arreglo `QUIZ` en `script.js`.
- **Mapa:** edita `mapa_datos.js` para las cifras por municipio y `mapa_municipios.js` para los polígonos GeoJSON. Los CSV y GeoJSON auditables están en `datos_mapa/`.
- **Narración:** edita el arreglo `NARRATION` en `script.js`.
- **Colores y tipografía:** edita las variables de `:root` en `style.css`.
- **Enlaces de informes y repositorio:** edítalos en el `footer` de `index.html`.

## Datos y metodología

- Fuente cuantitativa: anuncios públicos de Revolico en La Habana, capturados entre el 10 y el 26 de octubre de 2026.
- Fuente cualitativa: 25 compradores, 4 talleres y 1 importadora (30 entrevistas).
- Precios en USD. Los anuncios en CUP se conservan para conteo.
- Categorías: motos de combustión, motos eléctricas, bicicletas eléctricas y patinetes.
- Georreferenciación: 105 de 6.159 anuncios (1,70%) tienen municipio identificable; 90 provienen de la referencia Apollo y 15 de mención explícita en el texto. Los 6.054 restantes se excluyen.
- Cobertura municipal: 12 de 15 municipios con datos. Top 3: Plaza de la Revolución (35), Centro Habana (19) y Playa (16).
- Límites y centroides: OpenStreetMap / Overpass API (`admin_level=6`, consulta del 09/11/2026), sin coordenadas simuladas.
- El proyecto completo, el ETL y los informes están en el repositorio de datos.

## Limitaciones y transparencia

- Los anuncios representan oferta publicada, no ventas efectivas.
- La ventana de 17 días no permite medir crecimiento.
- El dataset no incluye condición (nueva/usada).
- Solo el 1,70% de los anuncios (105/6.159) tiene municipio identificable. El mapa usa esa cobertura parcial y no representa el total del mercado.
- El mapa asigna cada anuncio al municipio declarado, no a una dirección exacta. Guanabacoa, Habana Vieja y Regla no tienen anuncios identificables.
- Los precios por municipio se basan en muestras pequeñas y no deben interpretarse como precios de venta.
- Las estimaciones de precio son orientativas y no sustituyen una inspección técnica.
- La muestra cualitativa es pequeña y no probabilística.

## Accesibilidad y rendimiento

- HTML semántico, etiquetas ARIA y enlace para saltar al dashboard.
- Navegación por teclado y foco visible.
- Respeto por `prefers-reduced-motion`.
- Sin frameworks ni build: carga rápida y despliegue simple.
- Los scripts de terceros se cargan por CDN; se recomienda conexión a internet.

## Créditos

Proyecto de análisis de datos e inteligencia de mercado desarrollado por Harold Ricardo Ponce. Datos y metodología: repositorio [Mercado-de-Motos](https://github.com/harolric78-lab/Mercado-de-Motos).

## Licencia

MIT.
