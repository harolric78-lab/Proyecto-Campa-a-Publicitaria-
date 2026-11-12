# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
import math, datetime

W, H = A4
DARK   = HexColor("#081120")
DARK2  = HexColor("#0c1728")
PANEL  = HexColor("#111e30")
CYAN   = HexColor("#00e5ff")
BLUE   = HexColor("#00a3d6")
PURPLE = HexColor("#7c3aed")
PINK   = HexColor("#ec4899")
AMBER  = HexColor("#f59e0b")
GREEN  = HexColor("#10b981")
RED    = HexColor("#ef4444")
LIGHT  = HexColor("#f4f6f8")
GRAY   = HexColor("#6b7280")
INK    = HexColor("#0f172a")
MUTED  = HexColor("#94a3b8")

c = canvas.Canvas("C:\\Users\\LA RUEDA\\Desktop\\Poyectos Matcom\\Proyecto de campana publicitaria\\Plan_de_Campana_Comunicacion_MotoMarket.pdf",
                  pagesize=A4)
c.setTitle("Plan de Campaña de Comunicación - MotoMarket Insights Cuba")
c.setAuthor("Harold Ricardo Ponce")
c.setSubject("Propuesta de comunicacion y marketing - MotoMarket Insights Cuba")

M = 20 * mm  # margin
def set_fill(col): c.setFillColor(col)
def set_stroke(col, w=1): c.setStrokeColor(col); c.setLineWidth(w)

def rect(x, y, w, h, fill=None, stroke=None, r=0):
    if fill is not None:
        c.setFillColor(fill)
    else:
        c.setFillColor(white)
    c.roundRect(x, y, w, h, r, stroke=1 if stroke else 0, fill=1)

RULE = MUTED
def line(x1, y1, x2, y2, col=RULE, w=0.8):
    c.setStrokeColor(col); c.setLineWidth(w)
    c.line(x1, y1, x2, y2)

def text(x, y, s, font="Helvetica", size=10, color=INK, align="left"):
    c.setFont(font, size); c.setFillColor(color)
    if align == "center":
        c.drawCentredString(x, y, s)
    elif align == "right":
        c.drawRightString(x, y, s)
    else:
        c.drawString(x, y, s)

def wrap(s, font, size, max_w):
    words = s.split(); lines = []; cur = ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if stringWidth(t, font, size) <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = wd
    if cur: lines.append(cur)
    return lines

def para(x, y, s, font="Helvetica", size=10, color=INK, max_w=None, leading=None, align="left", first_leading_offset=0):
    if leading is None: leading = size * 1.45
    max_w = max_w or (W - 2 * M)
    lines = wrap(s, font, size, max_w)
    yy = y
    for i, ln in enumerate(lines):
        text(x, yy - i * leading, ln, font, size, color, align)
    return yy - len(lines) * leading

def chip(x, y, w, h, label, bg, fg=white, size=8.5, bold=True):
    rect(x, y, w, h, fill=bg, r=h/2)
    c.setFillColor(fg); c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    c.drawCentredString(x + w/2, y + h/2 - size/2.6, label)

def badge(x, y, w, h, label, bg=DARK, fg=CYAN, size=8, stroke=CYAN):
    rect(x, y, w, h, fill=bg, stroke=stroke, r=3)
    c.setFillColor(fg); c.setFont("Helvetica-Bold", size)
    c.drawCentredString(x + w/2, y + h/2 - size/2.6, label)

def header_band(y, num, title, subtitle=None):
    rect(0, y, W, 26*mm, fill=DARK)
    rect(0, y - 1.5*mm, W, 1*mm, fill=CYAN)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 20)
    c.drawString(M, y + 9*mm, f"0{num}")
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 15)
    c.drawString(M + 22*mm, y + 10*mm, title.upper())
    if subtitle:
        c.setFillColor(MUTED); c.setFont("Helvetica", 9)
        c.drawString(M + 22*mm, y + 4*mm, subtitle)
    return y - 28*mm

def card(x, y, w, h, fill=PANEL, stroke=CYAN, r=6, alpha_stroke=1):
    rect(x, y, w, h, fill=fill, stroke=stroke, r=r)
    return y

def kpi_card(x, y, w, h, value, label, accent=CYAN, sub=None):
    rect(x, y, w, h, fill=PANEL, stroke=accent, r=8)
    rect(x, y + h - 4*mm, w, 4*mm, fill=accent, r=0)
    c.setFillColor(accent); c.setFont("Helvetica-Bold", 13)
    c.drawString(x + 6*mm, y + h - 10*mm, label.upper())
    c.setFillColor(white); c.setFont("Helvetica-Bold", 22)
    c.drawString(x + 6*mm, y + h - 22*mm, value)
    if sub:
        c.setFillColor(MUTED); c.setFont("Helvetica", 8)
        c.drawString(x + 6*mm, y + 6*mm, sub)

def page_footer(page_num):
    c.setFillColor(MUTED); c.setFont("Helvetica", 7.5)
    c.drawString(M, 12*mm, "MotoMarket Insights Cuba  ·  Plan de Campaña de Comunicación")
    c.drawRightString(W - M, 12*mm, f"{page_num}")

def cover():
    # Dark gradient background
    rect(0, 0, W, H, fill=DARK)
    # Subtle panel shapes
    rect(W - 120*mm, H - 60*mm, 100*mm, 40*mm, fill=DARK2, r=8)
    rect(20*mm, 20*mm, 80*mm, 10*mm, fill=DARK2, r=5)
    # Accent data dots and circuit lines
    c.setFillColor(CYAN)
    for i in range(12):
        cx = 40*mm + i * 35*mm
        cy = H - 30*mm - (i % 3) * 12*mm
        c.circle(cx, cy, 2.5, stroke=0, fill=1)
    c.setStrokeColor(CYAN); c.setLineWidth(0.6)
    for i in range(8):
        x1 = 30*mm; y1 = H - 50*mm - i * 30*mm
        x2 = x1 + 60*mm; y2 = y1 + (5 if i % 2 else -5)*mm
        c.line(x1, y1, x2, y2)
    # Motorcycle motif (stylized): two wheels + body
    c.setStrokeColor(CYAN); c.setLineWidth(1.2)
    c.circle(55*mm, 45*mm, 14*mm, stroke=1, fill=0)
    c.circle(105*mm, 45*mm, 14*mm, stroke=1, fill=0)
    c.rect(62*mm, 52*mm, 40*mm, 12*mm, stroke=1, fill=0)
    c.rect(62*mm, 64*mm, 20*mm, 6*mm, stroke=1, fill=0)
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(75*mm, 72*mm, "DATA")
    c.drawCentredString(75*mm, 67*mm, "VISUALS")
    # Main title block
    c.setFillColor(white); c.setFont("Helvetica-Bold", 40)
    c.drawString(M, H - 90*mm, "MotoMarket")
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 40)
    c.drawString(M, H - 110*mm, "Insights Cuba")
    c.setStrokeColor(CYAN); c.setLineWidth(2.5)
    c.line(M, H - 122*mm, M + 70*mm, H - 122*mm)
    c.setFillColor(MUTED); c.setFont("Helvetica", 13)
    c.drawString(M, H - 140*mm, "Plataforma de inteligencia de mercado para el sector de las motos en Cuba")
    c.setFillColor(white); c.setFont("Helvetica-Bold", 17)
    c.drawString(M, H - 175*mm, "Plan de Campaña de Comunicación")
    c.setFillColor(CYAN); c.setFont("Helvetica", 11.5)
    c.drawString(M, H - 195*mm, "Siete días para que la mayor cantidad de personas descubra qué revelan más de 6.100 anuncios sobre el mercado de motos en Cuba.")
    # Meta block
    yy = H - 235*mm
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, yy, "AUTOR")
    c.setFillColor(white); c.setFont("Helvetica", 10.5)
    c.drawString(M, yy - 6*mm, "Harold Ricardo Ponce")
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M + 45*mm, yy, "ASIGNATURA")
    c.setFillColor(white); c.setFont("Helvetica", 10.5)
    c.drawString(M + 45*mm, yy - 6*mm, "Introducción a la Ciencia de Datos")
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M + 100*mm, yy, "INSTITUCIÓN")
    c.setFillColor(white); c.setFont("Helvetica", 10.5)
    c.drawString(M + 100*mm, yy - 6*mm, "Universidad de La Habana")
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, yy - 20*mm, "FECHA")
    c.setFillColor(white); c.setFont("Helvetica", 10.5)
    c.drawString(M, yy - 26*mm, datetime.date.today().strftime("%d de %B de %Y"))
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M + 45*mm, yy - 20*mm, "REPOSITORIO")
    c.setFillColor(white); c.setFont("Helvetica", 8.5)
    c.drawString(M + 45*mm, yy - 26*mm, "github.com/harolric78-lab/Proyecto-Campa-a-Publicitaria-")
    c.showPage()

cover()

def section(num, title, subtitle=None, new_page=True):
    if new_page: c.showPage()
    yy = header_band(H - 30*mm, num, title, subtitle)
    return yy

# ============ PAGE 2: EL PRODUCTO ============
yy = section(1, "El producto", "Plataforma web interactiva de inteligencia de mercado")
# Description
desc = ("MotoMarket Insights Cuba convierte más de 6.100 anuncios públicos y 30 entrevistas de campo en información accionable para compradores, vendedores, talleres, mecánicos, importadoras y emprendedores. Su promesa: que ninguna persona compre, venda, repare o importe una moto a ciegas.")
yy = para(M, yy, desc, size=10.5, color=white, max_w=W-2*M, leading=16) - 8*mm
# KPI cards row
kpis = [
    ("6.101", "Anuncios analizados", CYAN),
    ("30", "Entrevistas de campo", BLUE),
    ("17", "Días de captura", PURPLE),
    ("4", "Categorías", PINK),
]
cw = (W - 2*M - 3*8*mm) / 4
for i, (v, l, ac) in enumerate(kpis):
    kpi_card(M + i*(cw + 8*mm), yy - 30*mm, cw, 22*mm, v, l, ac)
yy -= 56*mm
# Platform mockups section
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 11)
c.drawString(M, yy, "Capturas de la plataforma")
c.setStrokeColor(CYAN); c.setLineWidth(0.6); c.line(M, yy - 3*mm, M + 40*mm, yy - 3*mm)
yy -= 10*mm
mockups = [
    ("Dashboard", "Composición por categoría, precios, marcas y demanda.", CYAN),
    ("Comparador", "Indica si una oferta es excelente, buena, normal o elevada.", BLUE),
    ("Calculadora", "Precio justo por categoría, marca, estado y extras.", PURPLE),
    ("Mapa", "15 municipios de La Habana con polígonos coloreados.", PINK),
]
mw = (W - 2*M - 2*8*mm) / 2
mh = 34*mm
for i, (t, d, ac) in enumerate(mockups):
    cx = M + (i % 2) * (mw + 8*mm)
    cy = yy - (i // 2) * (mh + 8*mm)
    rect(cx, cy, mw, mh, fill=PANEL, stroke=ac, r=8)
    rect(cx, cy + mh - 3.5*mm, mw, 3.5*mm, fill=ac, r=0)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 9.5)
    c.drawString(cx + 5*mm, cy + mh - 11*mm, t.upper())
    c.setFillColor(MUTED); c.setFont("Helvetica", 8)
    c.drawString(cx + 5*mm, cy + mh - 17*mm, d)
    # mini chart bars
    bx = cx + mw - 38*mm; by = cy + 6*mm
    vals = [12, 28, 45, 33, 52]
    for v in vals:
        bh = v * 1.6*mm
        rect(bx, by, 5*mm, bh, fill=ac, r=1)
        bx += 7*mm
yy -= 2*mh + 16*mm + 10*mm
# URLs
urls = [
    ("Plataforma", "https://harolric78-lab.github.io/Proyecto-Campa-a-Publicitaria-/"),
    ("Repositorio campaña", "https://github.com/harolric78-lab/Proyecto-Campa-a-Publicitaria-"),
    ("Repositorio datos", "https://github.com/harolric78-lab/Mercado-de-Motos"),
]
for i, (lbl, url) in enumerate(urls):
    rect(M, yy - 14*mm, W - 2*M, 13*mm, fill=DARK2, stroke=CYAN, r=5)
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M + 5*mm, yy - 10.5*mm, lbl.upper())
    c.setFillColor(white); c.setFont("Helvetica", 8.5)
    c.drawString(M + 35*mm, yy - 10.5*mm, url)
    yy -= 17*mm
page_footer(2)

# ============ PAGE 3: OBJETIVOS Y METAS ============
yy = section(2, "Objetivos y metas", "Metas para los primeros siete días de campaña")
metas = [
    ("Visitantes únicos", "500", "1.000", "2.000"),
    ("Compartidos orgánicos", "10", "30", "60"),
    ("Tiempo de permanencia", "1:30 min", "2:00 min", "3:00 min"),
    ("Uso del comparador", "100", "300", "600"),
    ("Seguidores TG/WA", "50", "150", "300"),
    ("Descargas del informe", "5", "20", "50"),
    ("Menciones en grupos", "20", "60", "120"),
]
cw_full = W - 2*M
row_h = 13*mm
header_y = yy - 10*mm
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 9)
c.drawString(M, header_y, "MÉTRICA")
c.drawString(M + 90*mm, header_y, "MÍNIMA")
c.drawString(M + 160*mm, header_y, "OBJETIVO")
c.drawString(M + 235*mm, header_y, "AMBICIOSA")
line(M, header_y - 3*mm, W - M, header_y - 3*mm, CYAN, 1)
yy = header_y - 12*mm
for i, (m, mn, ob, am) in enumerate(metas):
    rect(M, yy - 2*mm, cw_full, row_h, fill=(PANEL if i % 2 == 0 else DARK2), stroke=CYAN if i % 2 == 0 else None, r=4)
    c.setFillColor(white); c.setFont("Helvetica", 9)
    c.drawString(M + 5*mm, yy + 3*mm, m)
    c.setFillColor(MUTED); c.setFont("Helvetica", 9)
    c.drawString(M + 90*mm, yy + 3*mm, mn)
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 9)
    c.drawString(M + 160*mm, yy + 3*mm, ob)
    c.setFillColor(GREEN); c.setFont("Helvetica-Bold", 9)
    c.drawString(M + 235*mm, yy + 3*mm, am)
    # progress bar visual for objetivo
    pw = 40*mm
    rect(M + 310*mm, yy + 2*mm, pw, 5*mm, fill=DARK, r=2)
    fill_w = pw * (float(ob.replace(" min","").replace(":","").replace(".","")) / 2000) if ob != "1:30 min" else pw * 0.5
    rect(M + 310*mm, yy + 2*mm, min(fill_w, pw), 5*mm, fill=CYAN, r=2)
    yy -= row_h + 2*mm
yy -= 6*mm
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 9)
c.drawString(M, yy, "Medición")
yy -= 6*mm
note = "Cada canal se etiqueta con parámetros UTM (utm_source, utm_medium, utm_campaign=lanzamiento) para atribuir visitas a Facebook, Instagram, Telegram, WhatsApp, LinkedIn y GitHub."
yy = para(M, yy, note, size=9, color=MUTED, max_w=W-2*M, leading=13)
page_footer(3)

# ============ PAGE 4: PÚBLICO OBJETIVO ============
yy = section(3, "Público objetivo", "A quién le hablamos y qué le decimos")
audiences = [
    ("Compradores", "No saben si pagan de más", "Antes de pagar, compáralo con 6.101 anuncios reales.", CYAN),
    ("Propietarios", "Dolores: batería, autonomía, apagones", "Lo que importa no aparece en el anuncio.", BLUE),
    ("Talleres", "Qué vehículos dominan el mercado", "Descubre qué servicios van a crecer.", PURPLE),
    ("Importadoras", "Qué importar, a qué precio, para quién", "Eléctrico domina la oferta, no la atención.", PINK),
    ("Emprendedores", "No encuentran nichos claros", "Las oportunidades del mercado, sobre la mesa.", AMBER),
    ("Comunidad tech", "Datos abiertos y ciencia de datos", "Observatorio digital reproducible.", GREEN),
    ("Estudiantes", "Caso real de análisis de mercado", "Metodología y datos auditables en GitHub.", RED),
]
aw = (W - 2*M - 2*8*mm) / 3
ah = 42*mm
for i, (nom, dolor, msg, ac) in enumerate(audiences):
    cx = M + (i % 3) * (aw + 8*mm)
    cy = yy - (i // 3) * (ah + 10*mm)
    rect(cx, cy, aw, ah, fill=PANEL, stroke=ac, r=8)
    rect(cx, cy + ah - 3.5*mm, aw, 3.5*mm, fill=ac, r=0)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 10)
    c.drawString(cx + 5*mm, cy + ah - 10*mm, nom.upper())
    c.setFillColor(MUTED); c.setFont("Helvetica", 7.8)
    yy2 = cy + ah - 16*mm
    yy2 = para(cx + 5*mm, yy2, "Dolor: " + dolor, size=7.8, color=MUTED, max_w=aw-10*mm, leading=10.5) - 2*mm
    para(cx + 5*mm, yy2, "Mensaje: " + msg, size=7.8, color=white, max_w=aw-10*mm, leading=10.5)
yy -= 3 * (ah + 10*mm) + 10*mm
page_footer(4)

# ============ PAGE 5: EL MENSAJE ============
yy = section(4, "El mensaje", "Mensaje principal, eslogan y tono de comunicación")
# Big slogan
rect(M, yy - 45*mm, W - 2*M, 38*mm, fill=PANEL, stroke=CYAN, r=10)
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 11)
c.drawString(M + 8*mm, yy - 14*mm, "ESLOGAN PRINCIPAL")
c.setFillColor(white); c.setFont("Helvetica-Bold", 20)
c.drawString(M + 8*mm, yy - 28*mm, '"Decisiones sobre ruedas, con datos."')
yy -= 56*mm
# Alternative slogans as chips
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 10)
c.drawString(M, yy, "Eslóganes alternativos")
yy -= 8*mm
slogans = [
    "El mercado de motos, por fin en datos.",
    "Antes de comprar, míralo en datos.",
    "Datos que valen una moto.",
    "Conduce con información, no con rumores.",
    "El observatorio de las motos en Cuba.",
    "6.101 anuncios. Una sola verdad: el mercado habla.",
]
chip_w = 44*mm; chip_h = 10*mm
for i, s in enumerate(slogans):
    cx = M + (i % 3) * (chip_w + 6*mm)
    cy = yy - (i // 3) * (chip_h + 6*mm)
    chip(cx, cy, chip_w, chip_h, s, DARK2, size=7.5)
yy -= 3 * (chip_h + 6*mm) + 12*mm
# Tono
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 10)
c.drawString(M, yy, "Tono de comunicación")
yy -= 8*mm
rect(M, yy - 22*mm, W - 2*M, 18*mm, fill=DARK2, stroke=CYAN, r=6)
tone = ("Directo, útil, con autoridad técnica y cercano al habla cubana. Nunca académico, nunca frío.")
yy = para(M + 6*mm, yy - 6*mm, tone, size=9.5, color=white, max_w=W-2*M-12*mm, leading=14)
yy -= 24*mm
# Mensaje principal
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 10)
c.drawString(M, yy, "Mensaje principal")
yy -= 8*mm
msg = ("El mercado de motos en Cuba se mueve a ciegas: no existe un observatorio público de precios, oferta y demanda. MotoMarket Insights Cuba convierte más de 6.100 anuncios y 30 entrevistas en datos claros para decidir mejor al comprar, vender, reparar o importar.")
yy = para(M, yy, msg, size=10, color=white, max_w=W-2*M, leading=15)
page_footer(5)

# ============ PAGE 6-8: HALLAZGOS ============
hallazgos = [
    (1, "El promedio mentía", "La combustión es más cara que la eléctrica.",
     "Mediana combustión: 2.250 USD · eléctrica: 2.050 USD.",
     "Alto", "Compradores, propietarios, emprendedores", CYAN),
    (2, "Menos oferta, más interés", "La combustión tiene menos oferta, pero genera más del cuádruple de interés por anuncio.",
     "60.8 vistas (combustión) vs 14.9 (eléctricas) por anuncio.",
     "Muy alto", "Compradores, vendedores, importadoras, emprendedores", BLUE),
    (3, "Casi la mitad no dice su marca", "El 47,7% de los anuncios no declara marca.",
     "Topmaq 506 · JMD 227 · Mountain 187 · Vedca 173 · Challenger 170.",
     "Medio-alto", "Importadoras, talleres, compradores, emprendedores", PURPLE),
    (4, "Lo que importa no aparece en el anuncio", "Batería, autonomía, apagones, repuestos y papeles son los verdaderos dolores.",
     "25 compradores, 4 talleres y 1 importadora entrevistados.",
     "Alto", "Propietarios, compradores, talleres, mecánicos", PINK),
    (5, "Eléctrico domina la oferta, no la atención", "El 78,3% de la oferta es eléctrica, pero la combustión genera más interés.",
     "Oferta eléctrica 78,3% · combustión 60,8 vistas vs 14,9 eléctricas.",
     "Medio", "Importadoras, talleres, emprendedores, vendedores", AMBER),
    (6, "Antes de pagar, compáralo", "El comparador indica al instante si una oferta es excelente, buena, normal o elevada.",
     "Usa percentiles 25, 50 y 75 de cada categoría (octubre 2026).",
     "Muy alto", "Compradores, vendedores, propietarios", GREEN),
]
for i in range(0, 6, 2):
    yy = section(5 if i == 0 else 6 if i == 2 else 7, "Los ganchos principales", "Hallazgos respaldados por datos · corazón de la campaña", new_page=(i == 0))
    for j in range(2):
        if i + j >= 6: break
        num, tit, subt, evidencia, viral, publico, ac = hallazgos[i + j]
        cx = M + j * ((W - 2*M - 10*mm) / 2 + 10*mm)
        cw2 = (W - 2*M - 10*mm) / 2
        cy = yy - 10*mm
        rect(cx, cy, cw2, 62*mm, fill=PANEL, stroke=ac, r=10)
        rect(cx, cy + 62*mm - 5*mm, cw2, 5*mm, fill=ac, r=0)
        c.setFillColor(ac); c.setFont("Helvetica-Bold", 9)
        c.drawString(cx + 6*mm, cy + 62*mm - 12*mm, f"GANACHO {num}")
        c.setFillColor(white); c.setFont("Helvetica-Bold", 13.5)
        c.drawString(cx + 6*mm, cy + 62*mm - 24*mm, tit)
        c.setFillColor(MUTED); c.setFont("Helvetica", 8.2)
        c.drawString(cx + 6*mm, cy + 62*mm - 33*mm, subt)
        # dato principal
        c.setFillColor(white); c.setFont("Helvetica-Bold", 10)
        c.drawString(cx + 6*mm, cy + 62*mm - 44*mm, "DATO PRINCIPAL:")
        c.setFillColor(ac); c.setFont("Helvetica-Bold", 11)
        c.drawString(cx + 42*mm, cy + 62*mm - 44*mm, evidencia.split("·")[0] if "·" in evidencia else evidencia[:25])
        # Impacto
        c.setFillColor(white); c.setFont("Helvetica-Bold", 8)
        c.drawString(cx + 6*mm, cy + 14*mm, "IMPACTO / PÚBLICO")
        c.setFillColor(white); c.setFont("Helvetica", 7.8)
        c.drawString(cx + 6*mm, cy + 6*mm, f"Viral: {viral}   ·   Público: {publico}")
    yy -= 78*mm
    page_footer(5 + i//2 + 1)

# ============ PAGE 9: CANALES ============
yy = section(8, "Canales", "Rol de cada canal en la campaña")
canales = [
    ("WhatsApp", "Difusión de utilidad inmediata en grupos de moteros y talleres.", CYAN),
    ("Facebook", "Alcance masivo y lanzamiento para público general.", BLUE),
    ("Telegram", "Comunidad técnica y observatorio de datos.", PURPLE),
    ("Instagram", "Narrativa visual y hallazgos compartibles.", PINK),
    ("LinkedIn", "Credibilidad profesional y B2B (importadoras, emprendedores).", AMBER),
    ("GitHub", "Transparencia y credibilidad académica (datos y código abiertos).", GREEN),
]
cw2 = (W - 2*M - 10*mm) / 3
ch = 30*mm
for i, (nom, rol, ac) in enumerate(canales):
    cx = M + (i % 3) * (cw2 + 10*mm)
    cy = yy - (i // 3) * (ch + 8*mm)
    rect(cx, cy, cw2, ch, fill=PANEL, stroke=ac, r=8)
    rect(cx, cy + ch - 3*mm, cw2, 3*mm, fill=ac, r=0)
    c.setFillColor(ac); c.setFont("Helvetica-Bold", 10)
    c.drawString(cx + 5*mm, cy + ch - 9*mm, nom.upper())
    c.setFillColor(white); c.setFont("Helvetica", 7.8)
    para(cx + 5*mm, cy + ch - 15*mm, rol, size=7.8, color=white, max_w=cw2-10*mm, leading=10)
yy -= 2 * (ch + 8*mm) + 12*mm
# Social mockups
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 10)
c.drawString(M, yy, "Mockups de redes sociales")
yy -= 8*mm
def phone_mock(x, y, w, h, platform, color, header_txt, msgs):
    rect(x, y, w, h, fill=DARK2, stroke=color, r=12)
    rect(x, y + h - 12*mm, w, 12*mm, fill=color, r=0)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x + 5*mm, y + h - 8*mm, platform.upper())
    c.setFillColor(white); c.setFont("Helvetica", 7)
    c.drawString(x + w - 25*mm, y + h - 8*mm, "09:42")
    yy2 = y + h - 18*mm
    for m_txt in msgs:
        lines = wrap(m_txt, "Helvetica", 7, w - 16*mm)
        bh = len(lines) * 9.5*mm + 6*mm
        rect(x + 5*mm, yy2 - bh, w - 10*mm, bh, fill=PANEL, r=6)
        c.setFillColor(white); c.setFont("Helvetica", 7)
        for k, ln in enumerate(lines):
            c.drawString(x + 8*mm, yy2 - bh + 4*mm + k*9*mm, ln)
        yy2 -= bh + 5*mm
pw_ = 52*mm; ph_ = 78*mm
mocks = [
    ("Facebook", CYAN, "Lanzamiento · 6.101 anuncios",
     ["¿Cuánto cuesta realmente una moto en La Habana? Lanzamos MotoMarket Insights Cuba, el primer observatorio digital del mercado de motos."]),
    ("Instagram", PINK, "Carrusel · 5 tarjetas",
     ["Tarjeta 1: 6.101 anuncios analizados. Tarjeta 2: 78,3% de la oferta es eléctrica. Tarjeta 3: Topmaq lidera con 506 anuncios."]),
    ("Telegram", PURPLE, "Observatorio de datos",
     ["Nuevo observatorio del mercado de motos en Cuba. 6.101 anuncios y 30 entrevistas convertidos en datos útiles."]),
]
for i, (plt, col, hd, msgs) in enumerate(mocks):
    cx = M + i * (pw_ + 8*mm)
    phone_mock(cx, yy - ph_, pw_, ph_, plt, col, hd, msgs)
yy -= ph_ + 10*mm
page_footer(9)

# ============ PAGE 10: PREPARACIÓN ============
yy = section(9, "Preparación", "Todo lo necesario antes del lanzamiento")
prep = [
    ("Piezas visuales", "Tarjetas de dato 1080×1080, capturas del dashboard, comparador, calculadora, mapa y carrusel de 5 tarjetas.", CYAN),
    ("Copies aprobados", "Textos por canal listos en campana.md, reemplazando TU-DOMINIO por la URL final de GitHub Pages.", BLUE),
    ("Hashtags", "5-10 por publicación: 2 de núcleo, 2 de sector, 1 de datos.", PURPLE),
    ("Enlaces y UTMs", "Un solo enlace por publicación con parámetros de atribución por canal.", PINK),
    ("Transparencia", "Mencionar fuente, periodo (10-26 oct 2026), limitaciones del mapa y que los datos son oferta publicada, no ventas.", AMBER),
    ("Pruebas previas", "Index.html en móvil y escritorio, enlaces, portapapeles, narración Web Speech API y despliegue en GitHub Pages.", GREEN),
]
aw2 = (W - 2*M - 10*mm) / 2
ah2 = 34*mm
for i, (nom, det, ac) in enumerate(prep):
    cx = M + (i % 2) * (aw2 + 10*mm)
    cy = yy - (i // 2) * (ah2 + 8*mm)
    rect(cx, cy, aw2, ah2, fill=PANEL, stroke=ac, r=8)
    rect(cx, cy + ah2 - 3*mm, aw2, 3*mm, fill=ac, r=0)
    c.setFillColor(ac); c.setFont("Helvetica-Bold", 9.5)
    c.drawString(cx + 5*mm, cy + ah2 - 9*mm, nom.upper())
    c.setFillColor(white); c.setFont("Helvetica", 7.8)
    para(cx + 5*mm, cy + ah2 - 15*mm, det, size=7.8, color=white, max_w=aw2-10*mm, leading=10)
yy -= 3 * (ah2 + 8*mm) + 8*mm
page_footer(10)

# ============ PAGE 11: CRONOGRAMA ============
yy = section(10, "Cronograma de 7 días", "Línea temporal visual de la campaña")
dias = [
    (1, "Lanzamiento", "El mercado habla en datos", "78,3% de la oferta es eléctrica", "Facebook + Instagram", "Reel + carrusel", "Visitar la plataforma", CYAN),
    (2, "Comparador", "¿Estás pagando de más?", "Mediana combustión 2.250 USD · eléctrica 2.050 USD", "Telegram + WhatsApp", "Mensaje + enlace", "Prueba el comparador gratuito", BLUE),
    (3, "Marcas", "Casi la mitad no dice su marca", "47,7% sin marca · Topmaq lidera con 506", "Instagram", "Carrusel Top 5", "Compartir hallazgo", PURPLE),
    (4, "Talleres", "Qué vehículos dominan y crecerán", "78,3% oferta eléctrica · servicios de batería", "Facebook", "Publicación talleres", "Probar el dashboard", PINK),
    (5, "Quiz", "¿Cuánto sabes del mercado?", "Combustión 60,8 vistas vs 14,9 eléctricas", "Instagram + X", "Quiz interactivo 6 preguntas", "Retar a un amigo", AMBER),
    (6, "Voces reales", "Lo que los números no cuentan", "Batería, autonomía, apagones, repuestos, papeles", "Telegram + Facebook", "Testimonios + dato", "Escuchar narración", RED),
    (7, "Resumen", "Guarda y comparte la semana", "Recopilación de los mejores hallazgos", "Todos los canales", "Resumen semanal", "Guardar y compartir", GREEN),
]
tl_y = yy - 12*mm
# timeline line
line(M + 15*mm, tl_y, W - M - 15*mm, tl_y, CYAN, 2.5)
for i, (d, nom, subt, hall, canal, formato, cta, ac) in enumerate(dias):
    x = M + 15*mm + i * (W - 2*M - 30*mm) / 6
    # node
    c.setFillColor(ac); c.setStrokeColor(white); c.setLineWidth(1.5)
    c.circle(x, tl_y, 5.5, stroke=1, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x, tl_y + 9*mm, f"DÍA {d}")
    c.setFillColor(ac); c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(x, tl_y + 4*mm, nom.upper())
    c.setFillColor(MUTED); c.setFont("Helvetica", 7)
    c.drawCentredString(x, tl_y - 2*mm, subt)
    c.setFillColor(white); c.setFont("Helvetica", 7)
    c.drawCentredString(x, tl_y - 8*mm, hall)
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 6.8)
    c.drawCentredString(x, tl_y - 15*mm, canal)
    c.setFillColor(MUTED); c.setFont("Helvetica", 6.8)
    c.drawCentredString(x, tl_y - 20*mm, formato)
    c.setFillColor(ac); c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(x, tl_y - 25*mm, cta.upper())
yy = tl_y - 32*mm - 8*mm
page_footer(11)

# ============ PAGE 12: MÉTRICAS Y TRANSPARENCIA ============
yy = section(11, "Métricas y transparencia", "Cómo mediremos el impacto y los límites de los datos")
# KPI visual cards
kpis2 = [
    ("1.000", "Visitas en 7 días", CYAN, 60),
    ("30%", "Interacción con comparador", BLUE, 85),
    ("10+", "Compartidos orgánicos", PURPLE, 40),
    ("2:00 min", "Tiempo de permanencia", PINK, 55),
]
cw3 = (W - 2*M - 3*8*mm) / 4
for i, (v, l, ac, pct) in enumerate(kpis2):
    cx = M + i * (cw3 + 8*mm)
    rect(cx, yy - 26*mm, cw3, 22*mm, fill=PANEL, stroke=ac, r=8)
    rect(cx, yy - 26*mm, cw3 * pct / 100, 4*mm, fill=ac, r=0)
    c.setFillColor(ac); c.setFont("Helvetica-Bold", 8)
    c.drawString(cx + 5*mm, yy - 16*mm, l.upper())
    c.setFillColor(white); c.setFont("Helvetica-Bold", 15)
    c.drawString(cx + 5*mm, yy - 30*mm, v)
    c.setFillColor(MUTED); c.setFont("Helvetica", 7)
    c.drawString(cx + 5*mm, yy - 23*mm, f"Progreso meta: {pct}%")
yy -= 40*mm
# Transparencia cards
c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 10)
c.drawString(M, yy, "Notas de transparencia")
yy -= 8*mm
transp = [
    "Los datos representan oferta publicada en Revolico, no ventas efectivas.",
    "Ventana de captura: 17 días (10 al 26 de octubre de 2026).",
    "Solo el 1,70% de los anuncios (105/6.159) tiene municipio identificable.",
    "El mapa de calor es una simulación visual.",
    "Las estimaciones de precio son orientativas, no sustituyen una inspección técnica.",
    "La muestra cualitativa es pequeña y no probabilística.",
]
tw = (W - 2*M - 10*mm) / 2
for i, t in enumerate(transp):
    cx = M + (i % 2) * (tw + 10*mm)
    cy = yy - (i // 2) * (15*mm)
    rect(cx, cy, tw, 13*mm, fill=DARK2, stroke=CYAN, r=5)
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 7)
    c.drawString(cx + 4*mm, cy + 8.5*mm, "⚠")
    c.setFillColor(white); c.setFont("Helvetica", 7.6)
    c.drawString(cx + 8*mm, cy + 8.5*mm, t)
yy -= 3 * 15*mm + 10*mm
# Cierre
rect(M, yy - 20*mm, W - 2*M, 16*mm, fill=CYAN, r=8)
c.setFillColor(white); c.setFont("Helvetica-Bold", 11)
c.drawCentredString(W/2, yy - 10*mm, "MotoMarket Insights Cuba · Decisiones sobre ruedas, con datos.")
page_footer(12)

c.save()
print("PDF generado con diseño de pitch deck.")
