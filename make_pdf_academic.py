# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
    Table, TableStyle, HRFlowable, Image, PageBreak, KeepTogether
)
import os

DST = r"C:\Users\LA RUEDA\Desktop\Poyectos Matcom\Proyecto de campana publicitaria\Plan_de_Campana_Comunicacion_MotoMarket.pdf"
ASSETS = r"C:\Users\LA RUEDA\Desktop\Poyectos Matcom\Proyecto de campana publicitaria\\assets"

PAGE_W, PAGE_H = A4
M = 18 * mm

DARK = colors.HexColor("#081120")
INK = colors.HexColor("#1a202c")
GRAY = colors.HexColor("#64748b")
LIGHT = colors.HexColor("#f8fafc")
RULE = colors.HexColor("#e2e8f0")
ACCENT = colors.HexColor("#00a3d6")

styles = {}
styles["cover_kicker"] = ParagraphStyle("cover_kicker", fontName="Helvetica", fontSize=10, leading=14, textColor=GRAY, alignment=TA_LEFT)
styles["cover_title"] = ParagraphStyle("cover_title", fontName="Helvetica-Bold", fontSize=24, leading=30, textColor=DARK, alignment=TA_LEFT, spaceAfter=6)
styles["cover_sub"] = ParagraphStyle("cover_sub", fontName="Helvetica", fontSize=13, leading=18, textColor=INK, alignment=TA_LEFT, spaceAfter=14)
styles["cover_meta"] = ParagraphStyle("cover_meta", fontName="Helvetica", fontSize=10.5, leading=16, textColor=INK, alignment=TA_LEFT, spaceAfter=2)
styles["cover_meta_lbl"] = ParagraphStyle("cover_meta_lbl", fontName="Helvetica-Bold", fontSize=8.5, leading=12, textColor=GRAY, alignment=TA_LEFT, spaceBefore=6, spaceAfter=1)
styles["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=DARK, spaceBefore=4, spaceAfter=7, alignment=TA_LEFT)
styles["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11.5, leading=15, textColor=ACCENT, spaceBefore=10, spaceAfter=4, alignment=TA_LEFT)
styles["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.8, leading=14.6, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5)
styles["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.8, leading=14, textColor=INK, alignment=TA_LEFT, leftIndent=14, bulletIndent=3, spaceAfter=2.5)
styles["small"] = ParagraphStyle("small", fontName="Helvetica-Oblique", fontSize=8.3, leading=11.5, textColor=GRAY, alignment=TA_LEFT, spaceAfter=4)
styles["tbl_head"] = ParagraphStyle("tbl_head", fontName="Helvetica-Bold", fontSize=8.6, leading=11, textColor=colors.white, alignment=TA_LEFT)
styles["tbl_cell"] = ParagraphStyle("tbl_cell", fontName="Helvetica", fontSize=8.6, leading=11.5, textColor=INK, alignment=TA_LEFT)
styles["caption"] = ParagraphStyle("caption", fontName="Helvetica-Oblique", fontSize=8, leading=11, textColor=GRAY, alignment=TA_LEFT, spaceBefore=2, spaceAfter=8)
styles["toc_l1"] = ParagraphStyle("toc_l1", fontName="Helvetica-Bold", fontSize=10.5, leading=18, textColor=DARK, alignment=TA_LEFT)
styles["eslo"] = ParagraphStyle("eslo", fontName="Helvetica-Oblique", fontSize=11, leading=16, textColor=ACCENT, alignment=TA_LEFT, spaceAfter=4)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(M, PAGE_H - 14 * mm, PAGE_W - M, PAGE_H - 14 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GRAY)
    canvas.drawString(M, PAGE_H - 12 * mm, "Plan de Campaña de Comunicación · MotoMarket Insights Cuba")
    canvas.drawRightString(PAGE_W - M, PAGE_H - 12 * mm, "Universidad de La Habana")
    canvas.line(M, 14 * mm, PAGE_W - M, 14 * mm)
    canvas.drawString(M, 10 * mm, "Harold Ricardo Ponce · Introducción a la Ciencia de Datos")
    canvas.drawRightString(PAGE_W - M, 10 * mm, "Página %d" % doc.page)
    canvas.restoreState()


def cover(story):
    story.append(Spacer(1, 22 * mm))
    story.append(Paragraph("UNIVERSIDAD DE LA HABANA", styles["cover_kicker"]))
    story.append(Paragraph("Facultad de Matemática y Computación", styles["cover_kicker"]))
    story.append(Spacer(1, 10 * mm))
    story.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceBefore=2, spaceAfter=10))
    story.append(Paragraph("Plan de Campaña de Comunicación", styles["cover_title"]))
    story.append(Paragraph("MotoMarket Insights Cuba", styles["cover_sub"]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceBefore=2, spaceAfter=14))
    story.append(Paragraph("Autor: Harold Ricardo Ponce", styles["cover_meta"]))
    story.append(Paragraph("Asignatura: Introducción a la Ciencia de Datos", styles["cover_meta"]))
    story.append(Paragraph("Tipo de documento: Informe ejecutivo de campaña de comunicación", styles["cover_meta"]))
    story.append(Paragraph("Fecha: 10 de noviembre de 2026", styles["cover_meta"]))
    story.append(Spacer(1, 14 * mm))
    from reportlab.graphics.shapes import Drawing, Circle, Line
    d = Drawing(120, 60)
    d.add(Circle(30, 22, 9, fillColor=None, strokeColor=ACCENT, strokeWidth=1.2))
    d.add(Circle(90, 22, 9, fillColor=None, strokeColor=ACCENT, strokeWidth=1.2))
    d.add(Line(42, 26, 78, 26, strokeColor=ACCENT, strokeWidth=1.2))
    d.add(Circle(55, 33, 2, fillColor=ACCENT, strokeColor=None))
    story.append(d)
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Repositorio de campaña: github.com/harolric78-lab/Proyecto-Campa-a-Publicitaria-", styles["cover_meta_lbl"]))
    story.append(Paragraph("Repositorio de datos: github.com/harolric78-lab/Mercado-de-Motos", styles["cover_meta_lbl"]))
    story.append(PageBreak())


def toc(story):
    story.append(Paragraph("Contenido", styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceBefore=1, spaceAfter=8))
    toc_items = [
        ("1.", "Introducción"),
        ("2.", "El producto"),
        ("3.", "Objetivos y metas"),
        ("4.", "Público objetivo"),
        ("5.", "El mensaje"),
        ("6.", "Los hallazgos principales"),
        ("7.", "Canales de comunicación"),
        ("8.", "Cronograma de 7 días"),
        ("9.", "Métricas y evaluación"),
        ("10.", "Conclusiones"),
    ]
    for num, t in toc_items:
        story.append(Paragraph("<b>%s</b>&nbsp;&nbsp;%s" % (num, t), styles["toc_l1"]))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Nota metodológica", styles["h2"]))
    story.append(Paragraph(
        "Todos los hallazgos, cifras y copias de este documento se extraen exclusivamente de los archivos del repositorio "
        "<i>Proyecto-Campa-a-Publicitaria-</i> (<i>index.html</i>, <i>README.md</i> y <i>campana.md</i>) y del repositorio de datos "
        "<i>Mercado-de-Motos</i>. No se inventa ningún resultado.", styles["body"]))
    story.append(PageBreak())


def section_header(story, num, title):
    story.append(Paragraph("%s&nbsp;&nbsp;%s" % (num, title), styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceBefore=1, spaceAfter=6))


def bullets(story, items):
    for it in items:
        story.append(Paragraph("&bull;&nbsp;&nbsp;" + it, styles["bullet"]))


def hallazgo_block(story, num, titulo, descripcion, importa, evidencia, viral, publico, img_path=None, img_caption=None):
    flowables = []
    flowables.append(Paragraph("Hallazgo %d" % num, styles["h2"]))
    flowables.append(Paragraph(titulo, ParagraphStyle("ht", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=DARK, spaceAfter=3)))
    flowables.append(Paragraph("<b>Descripción.</b> " + descripcion, styles["body"]))
    flowables.append(Paragraph("<b>Por qué importa.</b> " + importa, styles["body"]))
    if evidencia:
        flowables.append(Paragraph("<b>Evidencia.</b> " + evidencia, styles["body"]))
    flowables.append(Paragraph("<b>Potencial de viralización:</b> " + viral, styles["body"]))
    flowables.append(Paragraph("<b>Público objetivo:</b> " + publico, styles["body"]))
    if img_path and os.path.exists(img_path):
        img = Image(img_path, width=120 * mm, height=120 * mm * 0.47)
        flowables.append(Spacer(1, 3 * mm))
        flowables.append(img)
        if img_caption:
            flowables.append(Paragraph(img_caption, styles["caption"]))
    story.append(KeepTogether(flowables))
    story.append(Spacer(1, 4 * mm))


def simple_table(story, headers, rows, col_widths, align_center_cols=None):
    align_center_cols = align_center_cols or []
    data = [[Paragraph(h, styles["tbl_head"]) for h in headers]]
    for r in rows:
        data.append([Paragraph(c, styles["tbl_cell"]) for c in r])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), DARK),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for ci in align_center_cols:
        style.append(("ALIGN", (ci, 0), (ci, -1), "CENTER"))
    t.setStyle(TableStyle(style))
    story.append(t)


doc = BaseDocTemplate(DST, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=16 * mm, bottomMargin=16 * mm,
                      title="Plan de Campaña de Comunicación - MotoMarket Insights Cuba", author="Harold Ricardo Ponce")
frame = Frame(M, 16 * mm, PAGE_W - 2 * M, PAGE_H - 16 * mm - 16 * mm, id="main")
doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=header_footer)])

story = []
cover(story)
toc(story)

# 1. Introducción
section_header(story, "1.", "Introducción")
story.append(Paragraph(
    "MotoMarket Insights Cuba es una plataforma web interactiva de inteligencia de mercado para el sector de las motos en La Habana. "
    "Convierte más de 6.100 anuncios públicos y 30 entrevistas de campo en información accionable para compradores, vendedores, talleres, "
    "mecánicos, importadoras y emprendedores. Su promesa central es que ninguna persona compre, venda, repare o importe una moto a ciegas.", styles["body"]))
story.append(Paragraph(
    "El presente documento es el plan de campaña de comunicación asociado al lanzamiento de la plataforma. Está elaborado como parte de la "
    "asignatura Introducción a la Ciencia de Datos de la Universidad de La Habana y se fundamenta exclusivamente en datos reales obtenidos "
    "mediante scraping de anuncios públicos en Revolico (La Habana), entrevistas de campo y el informe técnico del proyecto.", styles["body"]))
story.append(Spacer(1, 3 * mm))

# 2. El producto
section_header(story, "2.", "El producto")
story.append(Paragraph(
    "La plataforma contiene un dashboard interactivo con Chart.js, un comparador de precios, una calculadora de precio justo, un narrador "
    "inteligente con Web Speech API, un mapa interactivo de los 15 municipios de La Habana, un ranking de marcas, tarjetas de hallazgos "
    "compartibles, testimonios, un quiz de seis preguntas y una sección de metodología y transparencia. Está construida con HTML5, CSS3 y "
    "JavaScript puro, sin frameworks de frontend.", styles["body"]))
story.append(Paragraph("<b>URL de la plataforma:</b> https://harolric78-lab.github.io/Proyecto-Campa-a-Publicitaria-/", styles["body"]))
story.append(Paragraph("<b>Repositorio de campaña:</b> https://github.com/harolric78-lab/Proyecto-Campa-a-Publicitaria-", styles["body"]))
story.append(Paragraph("<b>Repositorio de datos:</b> https://github.com/harolric78-lab/Mercado-de-Motos", styles["body"]))
story.append(Spacer(1, 3 * mm))
img = Image(ASSETS + "/categoria.png", width=120 * mm, height=120 * mm * 0.47)
story.append(KeepTogether([img, Paragraph("Figura 1. Composición del mercado por categoría (anuncios publicados).", styles["caption"])]))

# 3. Objetivos y metas
section_header(story, "3.", "Objetivos y metas")
story.append(Paragraph(
    "Se definen metas para los primeros siete días de campaña, diferenciando entre meta mínima, objetivo y meta ambiciosa.", styles["body"]))
simple_table(story,
    ["Métrica", "Mínima", "Objetivo", "Ambiciosa"],
    [
        ["Visitantes únicos", "500", "1.000", "2.000"],
        ["Compartidos orgánicos", "10", "30", "60"],
        ["Tiempo de permanencia", "1:30 min", "2:00 min", "3:00 min"],
        ["Uso del comparador", "100", "300", "600"],
        ["Seguidores TG/WA", "50", "150", "300"],
        ["Descargas del informe", "5", "20", "50"],
        ["Menciones en grupos", "20", "60", "120"],
    ],
    [70 * mm, 30 * mm, 30 * mm, 38 * mm],
    align_center_cols=[1, 2, 3])
story.append(Spacer(1, 3 * mm))
story.append(Paragraph(
    "Cada canal se etiqueta con parámetros UTM (utm_source, utm_medium, utm_campaign=lanzamiento) para atribuir visitas a Facebook, "
    "Instagram, Telegram, WhatsApp, LinkedIn y GitHub.", styles["small"]))

# 4. Público objetivo
section_header(story, "4.", "Público objetivo")
simple_table(story,
    ["Audiencia", "Dolor principal", "Mensaje clave"],
    [
        ["Compradores", "No saben si pagan de más", "Antes de pagar, compáralo con 6.101 anuncios reales."],
        ["Propietarios", "Dolores: batería, autonomía, apagones", "Lo que importa no aparece en el anuncio."],
        ["Talleres", "Qué vehículos dominan el mercado", "Descubre qué servicios van a crecer."],
        ["Importadoras", "Qué importar, a qué precio, para quién", "Eléctrico domina la oferta, no la atención."],
        ["Emprendedores", "No encuentran nichos claros", "Las oportunidades del mercado, sobre la mesa."],
        ["Comunidad tecnológica", "Datos abiertos y ciencia de datos", "Observatorio digital reproducible."],
        ["Estudiantes", "Caso real de análisis de mercado", "Metodología y datos auditables en GitHub."],
    ],
    [34 * mm, 56 * mm, 68 * mm])
story.append(Spacer(1, 3 * mm))

# 5. El mensaje
section_header(story, "5.", "El mensaje")
story.append(Paragraph("<b>Mensaje principal.</b>", styles["h2"]))
story.append(Paragraph(
    "El mercado de motos en Cuba se mueve a ciegas: no existe un observatorio público de precios, oferta y demanda. MotoMarket Insights Cuba "
    "convierte más de 6.100 anuncios y 30 entrevistas en datos claros para decidir mejor al comprar, vender, reparar o importar.", styles["body"]))
story.append(Paragraph("<b>Eslogan principal.</b>", styles["h2"]))
story.append(Paragraph(
    "\"Decisiones sobre ruedas, con datos.\"", styles["eslo"]))
story.append(Paragraph("<b>Eslóganes alternativos.</b>", styles["h2"]))
bullets(story, [
    "El mercado de motos, por fin en datos.",
    "Antes de comprar, míralo en datos.",
    "Datos que valen una moto.",
    "Conduce con información, no con rumores.",
    "El observatorio de las motos en Cuba.",
    "6.101 anuncios. Una sola verdad: el mercado habla.",
])
story.append(Paragraph("<b>Tono de comunicación.</b>", styles["h2"]))
story.append(Paragraph(
    "Directo, útil, con autoridad técnica y cercano al habla cubana. Nunca académico, nunca frío.", styles["body"]))

# 6. Los hallazgos principales
section_header(story, "6.", "Los hallazgos principales")
story.append(Paragraph(
    "Los seis hallazgos seleccionados son el corazón de la campaña. Cada uno está respaldado por datos reales del proyecto: el dashboard, "
    "el informe final, el reporte técnico y los gráficos generados a partir del dataset de Revolico.", styles["body"]))
story.append(Spacer(1, 2 * mm))

hallazgo_block(story, 1, "El promedio mentía",
    "La mediana de una moto de combustión es 2.250 USD, mientras que una moto eléctrica cuesta 2.050 USD. La combustión es más cara que la eléctrica, rompiendo el mito de que lo eléctrico es inaccesible.",
    "Desafía una creencia extendida sin atacar directamente a nadie. Invita a comprobarlo con el comparador de la plataforma.",
    "Mediana combustión: 2.250 USD · mediana eléctrica: 2.050 USD.",
    "Alto", "Compradores, propietarios, emprendedores",
    img_path=ASSETS + "/precios.png",
    img_caption="Figura 2. Precio mediano por categoría (USD).")

hallazgo_block(story, 2, "Menos oferta, más interés",
    "La combustión tiene menos oferta que la eléctrica, pero genera más del cuádruple de interés por anuncio: 60.8 vistas promedio por anuncio de combustión frente a 14.9 en eléctricas.",
    "Plantea una pregunta incómoda: si hay menos combustión, ¿por qué se mira más? Genera debate sobre qué busca realmente el comprador cubano.",
    "60.8 vistas (combustión) vs 14.9 (eléctricas) por anuncio. Composición: combustión 1.099 anuncios vs bicicletas eléctricas 2.576.",
    "Muy alto", "Compradores, vendedores, importadoras, emprendedores",
    img_path=ASSETS + "/demanda.png",
    img_caption="Figura 3. Demanda: vistas promedio por anuncio.")

hallazgo_block(story, 3, "Casi la mitad no dice su marca",
    "El 47,7 % de los anuncios no declara marca. Solo cinco marcas concentran la presencia publicada: Topmaq (506 anuncios), JMD (227), Mountain (187), Vedca (173) y Challenger (170).",
    "Desnuda una opacidad del mercado: casi la mitad de la oferta es anónima en cuanto a marca. Posiciona a la plataforma como quien ordena lo confuso.",
    "47,7 % de anuncios sin marca. Top 5: Topmaq 506, JMD 227, Mountain 187, Vedca 173, Challenger 170.",
    "Medio-alto", "Importadoras, talleres, compradores, emprendedores",
    img_path=ASSETS + "/marcas.png",
    img_caption="Figura 4. Marcas con más presencia (anuncios publicados).")

hallazgo_block(story, 4, "Lo que importa no aparece en el anuncio",
    "Los verdaderos dolores del comprador y el propietario no están en el título del anuncio: batería, autonomía, apagones, repuestos y papeles. La autonomía real varía según peso, velocidad y terreno; los apagones afectan la decisión de carga y compra.",
    "Conecta con la experiencia vivida del usuario cubano, no con cifras frías. Genera reconocimiento inmediato y confianza.",
    "25 compradores, 4 talleres y 1 importadora entrevistados. Sección de necesidades detectadas del sitio web.",
    "Alto", "Propietarios, compradores, talleres, mecánicos",
    img_path=None)

hallazgo_block(story, 5, "Eléctrico domina la oferta, no la atención",
    "El 78,3 % de la oferta observada en La Habana es eléctrica (motos + bicicletas), pero las eléctricas generan menos interés por anuncio que la combustión.",
    "Muestra una contradicción del mercado: hay mucha oferta eléctrica, pero el comprador sigue mirando más la combustión. Útil para talleres e importadoras que decidan apostar por uno u otro segmento.",
    "Oferta eléctrica 78,3 %. Combustión 60,8 vistas vs 14,9 eléctricas.",
    "Medio", "Importadoras, talleres, emprendedores, vendedores",
    img_path=ASSETS + "/electrica.png",
    img_caption="Figura 5. Participación de la oferta eléctrica.")

hallazgo_block(story, 6, "Antes de pagar, compáralo",
    "El comparador de la plataforma permite introducir categoría y precio y saber al instante si la oferta es excelente, buena, normal o elevada, usando los percentiles 25, 50 y 75 de cada categoría.",
    "No vende la plataforma; vende la utilidad inmediata. Resuelve un problema real en cinco segundos. Es la pieza que más se reenvía en grupos de WhatsApp.",
    "Usa percentiles 25, 50 y 75 de cada categoría (octubre 2026). Referencia: medianas publicadas en Revolico.",
    "Muy alto", "Compradores, vendedores, propietarios",
    img_path=None)

# 7. Canales de comunicación
section_header(story, "7.", "Canales de comunicación")
simple_table(story,
    ["Canal", "Rol en la campaña"],
    [
        ["WhatsApp", "Difusión de utilidad inmediata en grupos de moteros, talleres y círculos familiares. Canal con mayor tasa de reenvío para el comparador de precios."],
        ["Facebook", "Alcance masivo y lanzamiento. Publicaciones para el público general, talleres e importadoras, y compradores."],
        ["Telegram", "Comunidad técnica y observatorio. Mensajes directos con el comparador, la calculadora y el mapa de actividad."],
        ["Instagram", "Narrativa visual y hallazgos compartibles. Carrusel de 5 tarjetas, reels del comparador y dato del día."],
        ["LinkedIn", "Credibilidad profesional y B2B. Importadoras, emprendedores y comunidad tecnológica."],
        ["GitHub", "Transparencia y credibilidad académica. Repositorio público del código y de los datos (Mercado-de-Motos)."],
    ],
    [34 * mm, 124 * mm])
story.append(Spacer(1, 3 * mm))
story.append(Paragraph("<b>Hashtags.</b> Núcleo: #MotoMarketCuba #MercadoDeMotos #MotosCuba #LaHabana #MovilidadCuba. Compra y venta: #ComprarMoto #VenderMoto #PreciosDeMotos #OfertasDeMotos. Sector: #Talleres #Mecanica #MotosElectricas #BicicletasElectricas #Importacion #EmprendimientoCuba. Datos: #DatosAbiertos #InteligenciaDeMercado #DataAnalytics #ObservatorioDigital. Usar entre 5 y 10 por publicación, mezclando 2 de núcleo, 2 de sector y 1 de datos.", styles["body"]))

# 8. Cronograma de 7 días
section_header(story, "8.", "Cronograma de 7 días")
simple_table(story,
    ["Día", "Objetivo", "Hallazgo protagonista", "Canales", "Formato", "CTA"],
    [
        ["1 · Lanzamiento", "Dar a conocer la plataforma y lograr las primeras 500 visitas", "78,3 % de la oferta es eléctrica", "Facebook + Instagram", "Reel + carrusel", "Visitar la plataforma"],
        ["2 · Comparador", "Que al menos 100 usuarios usen el comparador", "Mediana combustión 2.250 USD · eléctrica 2.050 USD", "Telegram + WhatsApp", "Mensaje + enlace", "Prueba el comparador gratuito"],
        ["3 · Marcas", "Generar 20 compartidos del hallazgo de marcas", "47,7 % sin marca · Topmaq lidera con 506", "Instagram", "Carrusel Top 5", "Compartir hallazgo"],
        ["4 · Talleres", "Atraer a 30 talleres e importadoras al dashboard", "78,3 % oferta eléctrica · servicios de batería", "Facebook", "Publicación para talleres", "Probar el dashboard"],
        ["5 · Quiz", "100 participaciones y 20 retos entre amigos", "Combustión 60,8 vistas vs 14,9 eléctricas", "Instagram + X", "Quiz interactivo 6 preguntas", "Retar a un amigo"],
        ["6 · Voces", "50 respuestas o menciones en grupos", "Batería, autonomía, apagones, repuestos, papeles", "Telegram + Facebook", "Testimonios + dato", "Escuchar narración"],
        ["7 · Resumen", "Cerrar con 1.000 visitas acumuladas y hábito de retorno", "Recopilación de los mejores hallazgos", "Todos los canales", "Resumen semanal", "Guardar y compartir"],
    ],
    [26 * mm, 44 * mm, 42 * mm, 30 * mm, 28 * mm, 28 * mm])
story.append(Spacer(1, 3 * mm))

# 9. Métricas y evaluación
section_header(story, "9.", "Métricas y evaluación")
story.append(Paragraph(
    "Se miden awareness, interacción, conversión y comunidad durante la primera semana.", styles["body"]))
simple_table(story,
    ["Dimensión", "Indicador", "Meta inicial"],
    [
        ["Awareness", "Alcance, impresiones, reproducciones de video, visitas nuevas", "1.000 visitas en 7 días"],
        ["Interacción", "Clics en el enlace, uso del comparador, uso de la calculadora, compartidos", "30 % de interacción con el comparador"],
        ["Conversión", "Sesiones con más de 2 minutos, regresos en 7 días, descargas del informe", "10 compartidos orgánicos"],
        ["Comunidad", "Respuestas en Telegram, mensajes directos, menciones, talleres interesados", "Seguimiento diario"],
    ],
    [32 * mm, 86 * mm, 40 * mm])
story.append(Spacer(1, 3 * mm))
story.append(Paragraph("<b>Transparencia y limitaciones.</b>", styles["h2"]))
bullets(story, [
    "Los datos representan oferta publicada en Revolico, no ventas efectivas.",
    "La ventana de captura es de 17 días (10 al 26 de octubre de 2026).",
    "Solo el 1,70 % de los anuncios (105/6.159) tiene municipio identificable; el mapa usa esa cobertura parcial.",
    "Las estimaciones de precio son orientativas y no sustituyen una inspección técnica.",
    "La muestra cualitativa es pequeña y no probabilística.",
])

# 10. Conclusiones
section_header(story, "10.", "Conclusiones")
story.append(Paragraph(
    "La campaña aprovecha seis hallazgos reales respaldados por datos para posicionar a MotoMarket Insights Cuba como el primer observatorio "
    "público del mercado de motos en La Habana. La combinación de ganchos contraintuitivos (\"el promedio mentía\", \"menos oferta, más interés\"), "
    "utilidad inmediata (comparador de precios) y voces reales del mercado ofrece una base sólida para alcanzar las metas de alcance, interacción "
    "y comunidad en los primeros siete días. Toda la información, los datos y el código están disponibles de forma abierta en los repositorios "
    "asociados, garantizando transparencia y reproducibilidad.", styles["body"]))
story.append(Spacer(1, 6 * mm))
story.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceBefore=2, spaceAfter=8))
story.append(Paragraph("<b>Referencias.</b>", styles["h2"]))
story.append(Paragraph("1. Repositorio de campaña y plataforma: https://github.com/harolric78-lab/Proyecto-Campa-a-Publicitaria-", styles["body"]))
story.append(Paragraph("2. Repositorio de datos, ETL e informes: https://github.com/harolric78-lab/Mercado-de-Motos", styles["body"]))
story.append(Paragraph("3. Sitio desplegado (GitHub Pages): https://harolric78-lab.github.io/Proyecto-Campa-a-Publicitaria-/", styles["body"]))

doc.build(story)
print("PDF académico generado:", DST)
