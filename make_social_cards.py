# -*- coding: utf-8 -*-
"""Genera tarjetas de dato 1080x1080 (Instagram/Facebook) para la campaña."""
import os
import matplotlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "promocion", "tarjetas")
os.makedirs(OUT, exist_ok=True)

W = H = 1080
BG_TOP = (8, 17, 32)
BG_BOTTOM = (12, 27, 48)
CYAN = (0, 229, 255)
PURPLE = (124, 92, 255)
ORANGE = (255, 138, 61)
PINK = (244, 114, 182)
GREEN = (34, 197, 94)
TEXT = (234, 242, 251)
MUTED = (143, 163, 189)
BORDER = (32, 47, 72)

FONT_DIR = os.path.join(matplotlib.get_data_path(), "fonts", "ttf")


def load_font(bold, size):
    if bold:
        candidates = [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf"]
    else:
        candidates = [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def fit_font(draw, text, bold, max_w, start, min_size=48):
    size = start
    while size > min_size:
        fnt = load_font(bold, size)
        if text_size(draw, text, fnt)[0] <= max_w:
            return fnt
        size -= 6
    return load_font(bold, min_size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if text_size(draw, test, fnt)[0] <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def center(draw, y, text, fnt, fill):
    w, _ = text_size(draw, text, fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


def background(accent):
    img = Image.new("RGB", (W, H), BG_TOP)
    top = Image.new("RGB", (1, H))
    for y in range(H):
        t = y / (H - 1)
        top.putpixel((0, y), tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3)))
    img = top.resize((W, H))

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([W * 0.55, -320, W * 1.45, H * 0.48], fill=(accent[0], accent[1], accent[2], 70))
    od.ellipse([-260, H * 0.6, W * 0.45, H * 1.35], fill=(accent[0], accent[1], accent[2], 30))
    overlay = overlay.filter(ImageFilter.GaussianBlur(170))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def footer(draw, accent):
    draw.line([(120, 800), (W - 120, 800)], fill=BORDER, width=2)
    brand_f = load_font(True, 36)
    url_f = fit_font(draw, "harolric78-lab.github.io/Proyecto-Campa-a-Publicitaria-", True, W - 200, 30, 18)
    note_f = load_font(False, 25)
    center(draw, 830, "MotoMarket Insights Cuba", brand_f, TEXT)
    center(draw, 888, "harolric78-lab.github.io/Proyecto-Campa-a-Publicitaria-", url_f, accent)
    center(draw, 943, "Datos: 6.159 anuncios de Revolico · La Habana, oct 2026", note_f, MUTED)


def stat_card(kicker, stat, body, accent, filename):
    img = background(accent)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([48, 48, W - 48, H - 48], radius=36, outline=BORDER, width=2)

    center(draw, 112, kicker.upper(), load_font(True, 40), accent)

    stat_f = fit_font(draw, stat, True, W - 200, 210, 90)
    _, sh = text_size(draw, stat, stat_f)
    center(draw, 300, stat, stat_f, TEXT)

    body_f = load_font(False, 46)
    lines = wrap(draw, body, body_f, W - 260)
    y = 300 + sh + 70
    for line in lines:
        center(draw, y, line, body_f, MUTED)
        y += int(body_f.size * 1.32)

    footer(draw, accent)
    img.save(os.path.join(OUT, filename), "PNG")
    print("OK", filename)


def title_card(kicker, title, body, accent, filename):
    img = background(accent)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([48, 48, W - 48, H - 48], radius=36, outline=BORDER, width=2)

    center(draw, 120, kicker.upper(), load_font(True, 40), accent)

    title_f = load_font(True, 92)
    lines = wrap(draw, title, title_f, W - 220)
    y = 300 - (len(lines) - 1) * (int(title_f.size * 1.15)) // 2
    for line in lines:
        center(draw, y, line, title_f, TEXT)
        y += int(title_f.size * 1.15)

    body_f = load_font(False, 46)
    blines = wrap(draw, body, body_f, W - 260)
    y += 40
    for line in blines:
        center(draw, y, line, body_f, MUTED)
        y += int(body_f.size * 1.32)

    footer(draw, accent)
    img.save(os.path.join(OUT, filename), "PNG")
    print("OK", filename)


stat_card(
    "Composición del mercado",
    "77,6%",
    "de la oferta de motos y bicicletas en La Habana es eléctrica.",
    CYAN,
    "01_oferta_electrica.png",
)

stat_card(
    "Marcas",
    "Topmaq",
    "lidera el mercado con 506 anuncios publicados.",
    PURPLE,
    "02_marca_lider.png",
)

stat_card(
    "Precios",
    "2.300 USD",
    "es la mediana de una moto de combustión. Una eléctrica: 2.170 USD.",
    ORANGE,
    "03_precios.png",
)

stat_card(
    "Demanda",
    "60,8 vs 14,9",
    "vistas promedio por anuncio: la combustión genera más interés que la eléctrica.",
    PINK,
    "04_demanda.png",
)

stat_card(
    "El dato incómodo",
    "47,7%",
    "de los anuncios no declara su marca. Casi la mitad del mercado es anónimo.",
    GREEN,
    "05_sin_marca.png",
)

stat_card(
    "El observatorio",
    "6.159",
    "anuncios y 30 entrevistas convertidos en datos para decidir mejor.",
    CYAN,
    "06_volumen.png",
)

title_card(
    "Herramienta gratis",
    "¿Estás pagando de más por tu moto?",
    "Elige la categoría, pon el precio y descúbrelo en 5 segundos. Comparador gratis con precios reales.",
    ORANGE,
    "07_comparador_cta.png",
)

print("Listo. Tarjetas en:", OUT)
