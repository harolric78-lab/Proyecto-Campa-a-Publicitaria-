# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import os

OUT = "C:\\Users\\LA RUEDA\\Desktop\\Poyectos Matcom\\Proyecto de campana publicitaria\\assets"
os.makedirs(OUT, exist_ok=True)

DARK   = "#081120"
BLUE   = "#00a3d6"
CYAN   = "#00e5ff"
GRAY   = "#6b7280"
LIGHT  = "#f4f6f8"
ACCENT = "#7c3aed"
INK    = "#0f172a"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.edgecolor": "#cbd5e1",
    "axes.linewidth": 0.8,
    "axes.titlesize": 10,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.dpi": 200,
})

# 1. Composición por categoría (oferta)
fig, ax = plt.subplots(figsize=(6.2, 2.9))
cats = ["Motos de combustión", "Motos eléctricas", "Bicicletas eléctricas", "Patinetes eléctricos"]
vals = [1099, 2201, 2576, 225]
colors = [BLUE, ACCENT, "#10b981", GRAY]
bars = ax.bar(cats, vals, color=colors, width=0.62)
ax.set_title("Composición del mercado por categoría (anuncios)", pad=10)
ax.set_ylabel("Anuncios")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 40, f"{v:,}", ha="center", va="bottom", fontsize=8.5, color=INK)
ax.tick_params(axis="x", rotation=12, labelsize=8)
ax.tick_params(axis="y", labelsize=8)
plt.tight_layout()
plt.savefig(f"{OUT}/categoria.png", bbox_inches="tight")
plt.close(fig)

# 2. Precio mediano por categoría
fig, ax = plt.subplots(figsize=(6.2, 2.9))
cats2 = ["Combustión", "Eléctrica", "Bicicleta eléctrica", "Patinete"]
vals2 = [2250, 2050, 1150, 750]
colors2 = [BLUE, ACCENT, "#10b981", GRAY]
bars = ax.bar(cats2, vals2, color=colors2, width=0.62)
ax.set_title("Precio mediano por categoría (USD)", pad=10)
ax.set_ylabel("USD")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, vals2):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 45, f"{v:,}", ha="center", va="bottom", fontsize=8.5, color=INK)
ax.tick_params(axis="x", rotation=0, labelsize=8)
ax.tick_params(axis="y", labelsize=8)
plt.tight_layout()
plt.savefig(f"{OUT}/precios.png", bbox_inches="tight")
plt.close(fig)

# 3. Marcas con más presencia
fig, ax = plt.subplots(figsize=(6.2, 2.9))
marcas = ["Topmaq", "JMD", "Mountain", "Vedca", "Challenger"]
mv = [506, 227, 187, 173, 170]
bars = ax.barh(marcas, mv, color=[ACCENT, BLUE, "#10b981", GRAY, CYAN], height=0.6)
ax.set_title("Marcas con más presencia (anuncios publicados)", pad=10)
ax.set_xlabel("Anuncios")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, mv):
    ax.text(b.get_width() + 8, b.get_y() + b.get_height()/2, f"{v}", va="center", fontsize=8.5, color=INK)
ax.tick_params(axis="y", labelsize=8)
ax.tick_params(axis="x", labelsize=8)
plt.tight_layout()
plt.savefig(f"{OUT}/marcas.png", bbox_inches="tight")
plt.close(fig)

# 4. Demanda: vistas promedio por anuncio
fig, ax = plt.subplots(figsize=(6.2, 2.9))
dem_cats = ["Combustión", "Bicicletas eléctricas", "Motos eléctricas", "Patinetes"]
dem_vals = [60.8, 27.4, 14.9, 9.2]
colors3 = [BLUE, "#10b981", ACCENT, GRAY]
bars = ax.bar(dem_cats, dem_vals, color=colors3, width=0.62)
ax.set_title("Demanda: vistas promedio por anuncio", pad=10)
ax.set_ylabel("Vistas promedio")
ax.spines[["top", "right"]].set_visible(False)
for b, v in zip(bars, dem_vals):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 1.5, f"{v}", ha="center", va="bottom", fontsize=8.5, color=INK)
ax.tick_params(axis="x", rotation=10, labelsize=8)
ax.tick_params(axis="y", labelsize=8)
plt.tight_layout()
plt.savefig(f"{OUT}/demanda.png", bbox_inches="tight")
plt.close(fig)

# 5. Oferta eléctrica vs resto
fig, ax = plt.subplots(figsize=(3.4, 2.6))
sizes = [78.3, 21.7]
labels = ["Eléctrica (78,3 %)", "Resto (21,7 %)"]
cols = [ACCENT, "#e2e8f0"]
wedges, _ = ax.pie(sizes, colors=cols, startangle=90, counterclock=False,
                   wedgeprops=dict(width=0.42, edgecolor="white", linewidth=1.5))
ax.text(0, 0.06, "78,3 %", ha="center", va="center", fontsize=13, fontweight="bold", color=ACCENT)
ax.text(0, -0.14, "oferta eléctrica", ha="center", va="center", fontsize=7.5, color=GRAY)
ax.set_title("Participación de la oferta eléctrica", pad=8)
ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(0.98, 0.5), fontsize=7.5, frameon=False)
plt.tight_layout()
plt.savefig(f"{OUT}/electrica.png", bbox_inches="tight")
plt.close(fig)

print("Gráficos generados en", OUT)
