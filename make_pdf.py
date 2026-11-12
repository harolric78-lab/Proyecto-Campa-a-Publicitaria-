# -*- coding: utf-8 -*-
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
    Table, TableStyle, HRFlowable, KeepTogether, PageBreak
)
from reportlab.platypus.flowables import Flowable

SRC = r"C:\Users\LA RUEDA\Desktop\Poyectos Matcom\Proyecto de campana publicitaria\Plan_de_Campana_Comunicacion_MotoMarket.md"
DST = r"C:\Users\LA RUEDA\Desktop\Poyectos Matcom\Proyecto de campana publicitaria\Plan_de_Campana_Comunicacion_MotoMarket.pdf"

PAGE_W, PAGE_H = A4
MARGIN = 18 * mm

ACCENT = colors.HexColor("#081120")
ACCENT2 = colors.HexColor("#00e5ff")
ACCENT3 = colors.HexColor("#00a3d6")
LIGHT = colors.HexColor("#f4f6f8")
LIGHT2 = colors.HexColor("#e8edf2")
GRAY = colors.HexColor("#4b5563")
RULE = colors.HexColor("#d1d5db")
WHITE = colors.white

class ColoredRule(Flowable):
    def __init__(self, width, height=2, color=ACCENT, space_before=0, space_after=0):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.space_before = space_before
        self.space_after = space_after
    def wrap(self, aw, ah):
        return (self.width, self.height + self.space_before + self.space_after)
    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, self.space_after, self.width, self.height, stroke=0, fill=1)

class SectionHeader(Flowable):
    def __init__(self, text, width, number=None):
        super().__init__()
        self.text = text
        self.width = width
        self.number = number
    def wrap(self, aw, ah):
        return (self.width, 22 * mm)
    def draw(self):
        c = self.canv
        c.setFillColor(ACCENT)
        c.rect(0, 0, self.width, 10 * mm, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 12.5)
        x = 6
        if self.number:
            c.setFillColor(ACCENT2)
            c.circle(8, 5 * mm, 3.2, stroke=0, fill=1)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(8, 5 * mm - 1.1, self.number)
            x = 16
        c.drawString(x, 3.6 * mm, self.text.upper())
        c.setFillColor(ACCENT2)
        c.rect(0, 9.5 * mm, self.width, 0.6 * mm, stroke=0, fill=1)

class MetricCard(Flowable):
    def __init__(self, value, label, width):
        super().__init__()
        self.value = value
        self.label = label
        self.width = width
    def wrap(self, aw, ah):
        return (self.width, 20 * mm)
    def draw(self):
        c = self.canv
        c.setFillColor(LIGHT)
        c.roundRect(0, 0, self.width, 16 * mm, 3, stroke=0, fill=1)
        c.setStrokeColor(ACCENT2)
        c.setLineWidth(0.8)
        c.roundRect(0, 0, self.width, 16 * mm, 3, stroke=1, fill=0)
        c.setFillColor(ACCENT)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(self.width / 2, 10.5 * mm, self.value)
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(self.width / 2, 4 * mm, self.label.upper())

def md_to_inline(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<font name='Courier'><b>\1</b></font>", text)
    return text

styles = {}
styles["cover_title"] = ParagraphStyle("cover_title", fontName="Helvetica-Bold", fontSize=30, leading=38, textColor=WHITE, alignment=TA_LEFT)
styles["cover_sub"] = ParagraphStyle("cover_sub", fontName="Helvetica", fontSize=14.5, leading=21, textColor=colors.HexColor("#cfd8e0"), alignment=TA_LEFT)
styles["cover_meta"] = ParagraphStyle("cover_meta", fontName="Helvetica", fontSize=10.5, leading=15, textColor=colors.HexColor("#9fb0c4"), alignment=TA_LEFT, spaceAfter=1)
styles["cover_label"] = ParagraphStyle("cover_label", fontName="Helvetica-Bold", fontSize=8.5, leading=12, textColor=ACCENT2, alignment=TA_LEFT, spaceBefore=4, spaceAfter=1)
styles["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13.5, leading=17, textColor=ACCENT, spaceBefore=2, spaceAfter=2, alignment=TA_LEFT)
styles["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.8, leading=14.2, textColor=colors.black, alignment=TA_JUSTIFY, spaceAfter=4.5)
styles["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.8, leading=13.8, textColor=colors.black, alignment=TA_LEFT, leftIndent=13, bulletIndent=3, spaceAfter=2.5)
styles["num"] = ParagraphStyle("num", fontName="Helvetica", fontSize=9.8, leading=13.8, textColor=colors.black, alignment=TA_LEFT, leftIndent=15, bulletIndent=3, spaceAfter=2.5)
styles["small"] = ParagraphStyle("small", fontName="Helvetica-Oblique", fontSize=8.2, leading=11, textColor=GRAY, alignment=TA_LEFT, spaceAfter=3)
styles["table_th"] = ParagraphStyle("table_th", fontName="Helvetica-Bold", fontSize=8.4, leading=10.5, textColor=WHITE, alignment=TA_LEFT)
styles["table_td"] = ParagraphStyle("table_td", fontName="Helvetica", fontSize=8.6, leading=11.5, textColor=colors.black, alignment=TA_LEFT)

def parse_blocks(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    lines = raw.split("\n")
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if re.match(r"^[-*_]{3,}\s*$", stripped):
            blocks.append(("hr", None)); i += 1; continue
        if stripped.startswith("# "):
            blocks.append(("cover_title", stripped[2:].strip())); i += 1; continue
        if stripped.startswith("## "):
            blocks.append(("cover_sub", stripped[3:].strip())); i += 1; continue
        if stripped.startswith("### "):
            blocks.append(("cover_meta", stripped[4:].strip())); i += 1; continue
        if stripped.startswith("### ") and not stripped.startswith("## "):
            blocks.append(("h3", stripped[4:].strip())); i += 1; continue
        if stripped.startswith("# ") and not stripped.startswith("## "):
            blocks.append(("h1", stripped[2:].strip())); i += 1; continue
        if stripped.startswith("## ") and not stripped.startswith("### "):
            blocks.append(("h2", stripped[3:].strip())); i += 1; continue
        if stripped.startswith("|") and "|" in stripped[1:]:
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append([md_to_inline(c) for c in cells])
                i += 1
            blocks.append(("table", rows)); continue
        m = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if m:
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(md_to_inline(re.sub(r"^\d+\.\s+", "", lines[i].strip())))
                i += 1
            blocks.append(("numlist", items)); continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            items = []
            while i < n and (lines[i].strip().startswith("- ") or lines[i].strip().startswith("* ")):
                items.append(md_to_inline(re.sub(r"^[-*]\s+", "", lines[i].strip())))
                i += 1
            blocks.append(("bulletlist", items)); continue
        paras = []
        while i < n and lines[i].strip() and not lines[i].strip().startswith("#") and not lines[i].strip().startswith("|") and not re.match(r"^\d+\.\s+", lines[i].strip()) and not (lines[i].strip().startswith("- ") or lines[i].strip().startswith("* ")) and not re.match(r"^[-*_]{3,}\s*$", lines[i].strip()):
            paras.append(lines[i].strip()); i += 1
        if paras:
            blocks.append(("para", " ".join(paras)))
    return blocks

def build_table(rows, available_w):
    col_count = len(rows[0])
    col_w = available_w / col_count
    data = []
    for r, row in enumerate(rows):
        line_items = []
        for c in row:
            if r == 0:
                line_items.append(Paragraph(c, styles["table_th"]))
            else:
                line_items.append(Paragraph(c, styles["table_td"]))
        data.append(line_items)
    t = Table(data, colWidths=[col_w]*col_count, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), ACCENT),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT]),
        ("GRID", (0,0), (-1,-1), 0.4, RULE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.6)
    canvas.line(MARGIN, PAGE_H - 13 * mm, PAGE_W - MARGIN, PAGE_H - 13 * mm)
    canvas.setFont("Helvetica", 7.6); canvas.setFillColor(GRAY)
    canvas.drawString(MARGIN, PAGE_H - 11 * mm, "PLAN DE CAMPAÑA DE COMUNICACIÓN  ·  MOTOMARKET INSIGHTS CUBA")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 11 * mm, "UNIVERSIDAD DE LA HABANA")
    canvas.line(MARGIN, 13 * mm, PAGE_W - MARGIN, 13 * mm)
    canvas.drawString(MARGIN, 9.5 * mm, "Harold Ricardo Ponce · Introducción a la Ciencia de Datos")
    canvas.drawRightString(PAGE_W - MARGIN, 9.5 * mm, f"Página {doc.page}")
    canvas.restoreState()

doc = BaseDocTemplate(DST, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=18 * mm, bottomMargin=16 * mm,
                      title="Plan de Campaña de Comunicación - MotoMarket Insights Cuba", author="Harold Ricardo Ponce")
frame = Frame(MARGIN, 16 * mm, PAGE_W - 2*MARGIN, PAGE_H - 18*mm - 16*mm, id="main")
doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=header_footer)])

story = []
blocks = parse_blocks(SRC)
available_w = PAGE_W - 2 * MARGIN

for kind, val in blocks:
    if kind == "cover_title":
        story.append(Spacer(1, 14 * mm))
        cover_bg = Table([[Paragraph("PLAN DE CAMPAÑA DE COMUNICACIÓN", ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=24, leading=32, textColor=WHITE))]],
                         colWidths=[available_w], rowHeights=[30 * mm])
        cover_bg.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), ACCENT), ("LEFTPADDING", (0,0), (-1,-1), MARGIN), ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6)]))
        story.append(cover_bg)
        story.append(Spacer(1, 10 * mm))
        story.append(Paragraph("Siete días para que la mayor cantidad de personas descubra qué revelan más de 6.100 anuncios sobre el mercado de motos en Cuba.", ParagraphStyle("cs", fontName="Helvetica", fontSize=13, leading=20, textColor=colors.HexColor("#cfd8e0"), alignment=TA_LEFT)))
        story.append(Spacer(1, 16 * mm))
        story.append(Paragraph("Autor: Harold Ricardo Ponce", styles["cover_label"]))
        story.append(Paragraph("Asignatura: Introducción a la Ciencia de Datos", styles["cover_label"]))
        story.append(Paragraph("Universidad de La Habana", styles["cover_label"]))
        story.append(Paragraph("Repositorio: github.com/harolric78-lab/Proyecto-Campa-a-Publicitaria-", styles["cover_label"]))
        story.append(PageBreak())
        continue
    if kind == "cover_sub":
        story.append(Paragraph(val, styles["subtitle"] if "subtitle" in styles else ParagraphStyle("sub", fontName="Helvetica", fontSize=13, leading=20, textColor=GRAY, alignment=TA_LEFT)))
        continue
    if kind == "cover_meta":
        story.append(Paragraph(val, styles["cover_meta"]))
        continue
    if kind == "h1":
        story.append(SectionHeader(val, available_w))
        continue
    if kind == "h2":
        story.append(Paragraph(val, styles["h1"]))
        continue
    if kind == "h3":
        story.append(Paragraph(val, ParagraphStyle("h3", parent=styles["body"], fontName="Helvetica-Bold", fontSize=10.6, textColor=ACCENT3, spaceBefore=7, spaceAfter=3, alignment=TA_LEFT)))
        continue
    if kind == "para":
        story.append(Paragraph(md_to_inline(val), styles["body"]))
        continue
    if kind == "bulletlist":
        for item in val:
            story.append(Paragraph("&bull;  " + item, styles["bullet"]))
        continue
    if kind == "numlist":
        for idx, item in enumerate(val, 1):
            story.append(Paragraph(f"<b>{idx}.</b>&nbsp;&nbsp;{item}", styles["num"]))
        continue
    if kind == "table":
        story.append(build_table(val, available_w))
        story.append(Spacer(1, 7))
        continue
    if kind == "hr":
        story.append(ColoredRule(available_w, height=1.2, color=ACCENT2, space_before=4, space_after=8))
        continue

doc.build(story)
print("PDF generado:", DST)
