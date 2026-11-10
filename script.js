const $ = (selector, scope = document) => scope.querySelector(selector);
const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));

const fmt = (value, decimals = 0) =>
  new Intl.NumberFormat("es-ES", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
    useGrouping: true,
  }).format(value);

const sharePct = (value, total, decimals = 1) =>
  total ? ((value / total) * 100).toFixed(decimals).replace(".", ",") : "0";

const MEDIANS = {
  combustion: { label: "Moto de combustión", median: 2300, p25: 1900, p75: 2600, min: 50, max: 26000 },
  electrica: { label: "Moto eléctrica", median: 2170, p25: 1400, p75: 2650, min: 50, max: 45000 },
  bicicleta: { label: "Bicicleta eléctrica", median: 1150, p25: 655, p75: 1650, min: 50, max: 111111 },
  patinete: { label: "Patinete eléctrico", median: 750, p25: 700, p75: 800, min: 50, max: 1250 },
};

const MARKET = {
  total: 6159,
  categories: [
    { key: "bicicleta", label: "Bicicletas eléctricas", count: 2653, price: 1150, views: 27.4, color: "#00e5ff" },
    { key: "electrica", label: "Motos eléctricas", count: 2125, price: 2170, views: 14.9, color: "#7c5cff" },
    { key: "combustion", label: "Motos de combustión", count: 1137, price: 2300, views: 60.8, color: "#ff8a3d" },
    { key: "patinete", label: "Patinetes", count: 244, price: 750, views: 9.2, color: "#f472b6" },
  ],
  brands: [
    { name: "Topmaq", count: 506, color: "#00e5ff" },
    { name: "JMD", count: 235, color: "#38bdf8" },
    { name: "Mountain", count: 187, color: "#818cf8" },
    { name: "Vedca", count: 174, color: "#a78bfa" },
    { name: "Yoazaky", count: 171, color: "#c084fc" },
    { name: "Challenger", count: 170, color: "#f472b6" },
  ],
};

const initNav = () => {
  const toggle = $("#navToggle");
  const nav = $("#nav");
  if (!toggle || !nav) return;
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
  });
  $$("a", nav).forEach((link) =>
    link.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Abrir menú");
    })
  );
};

const initScroll = () => {
  const header = $(".site-header");
  const bar = $("#scrollBar");
  const onScroll = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - window.innerHeight;
    if (bar) bar.style.width = `${height > 0 ? (scrollTop / height) * 100 : 0}%`;
    if (header) header.classList.toggle("is-scrolled", scrollTop > 12);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
};

const initReveal = () => {
  const items = $$(".reveal");
  if (!("IntersectionObserver" in window)) {
    items.forEach((item) => item.classList.add("is-visible"));
    return;
  }
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );
  items.forEach((item) => observer.observe(item));
};

const animateCounters = () => {
  const counters = $$("[data-count]");
  if (!counters.length) return;
  const run = (el) => {
    const target = parseFloat(el.dataset.count);
    const decimals = parseInt(el.dataset.decimals || "0", 10);
    const duration = 1400;
    const start = performance.now();
    const update = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = fmt(target * eased, decimals);
      if (progress < 1) requestAnimationFrame(update);
      else el.textContent = fmt(target, decimals);
    };
    requestAnimationFrame(update);
  };
  if (!("IntersectionObserver" in window)) {
    counters.forEach(run);
    return;
  }
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          run(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );
  counters.forEach((el) => observer.observe(el));
};

let charts = {};

const chartFont = () => (window.Chart ? Chart.defaults.font.family : "Inter, sans-serif");

const initCharts = () => {
  if (typeof Chart === "undefined") return;

  Chart.defaults.color = "#8fa3bd";
  Chart.defaults.font.family = "Inter, 'Segoe UI', sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.borderColor = "rgba(255,255,255,0.06)";

  const tooltipStyle = {
    backgroundColor: "rgba(8,17,32,0.95)",
    borderColor: "rgba(255,255,255,0.12)",
    borderWidth: 1,
    titleColor: "#eaf2fb",
    bodyColor: "#a9c4dd",
    padding: 12,
    cornerRadius: 10,
    displayColors: true,
  };

  const cats = MARKET.categories;
  const catEl = $("#chartCategories");
  if (catEl) {
    charts.categories = new Chart(catEl, {
      type: "doughnut",
      data: {
        labels: cats.map((c) => c.label),
        datasets: [
          {
            data: cats.map((c) => c.count),
            backgroundColor: cats.map((c) => c.color),
            borderColor: "#111c2d",
            borderWidth: 3,
            hoverOffset: 10,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: "62%",
        plugins: {
          legend: { position: "bottom", labels: { boxWidth: 10, boxHeight: 10, padding: 14, usePointStyle: true, pointStyle: "circle" } },
          tooltip: {
            ...tooltipStyle,
            callbacks: {
              label: (ctx) => {
                const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                const value = ctx.parsed;
                return ` ${ctx.label}: ${fmt(value)} (${((value / total) * 100).toFixed(1)}%)`;
              },
            },
          },
        },
      },
    });
  }

  const priceEl = $("#chartPrices");
  if (priceEl) {
    charts.prices = new Chart(priceEl, {
      type: "bar",
      data: {
        labels: cats.map((c) => c.label.replace("Motos de ", "").replace("Bicicletas ", "Bici ")),
        datasets: [
          {
            label: "Precio mediano",
            data: cats.map((c) => c.price),
            backgroundColor: cats.map((c) => c.color),
            borderRadius: 8,
            maxBarThickness: 54,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false }, tooltip: { ...tooltipStyle, callbacks: { label: (ctx) => ` ${fmt(ctx.parsed.y)} USD` } } },
        scales: {
          x: { grid: { display: false }, ticks: { maxRotation: 0, autoSkip: false, font: { size: 10 } } },
          y: { beginAtZero: true, grid: { color: "rgba(255,255,255,0.05)" }, ticks: { callback: (v) => `${fmt(v)}` } },
        },
      },
    });
  }

  const brandEl = $("#chartBrands");
  if (brandEl) {
    charts.brands = new Chart(brandEl, {
      type: "bar",
      data: {
        labels: MARKET.brands.map((b) => b.name),
        datasets: [
          {
            label: "Anuncios",
            data: MARKET.brands.map((b) => b.count),
            backgroundColor: MARKET.brands.map((b) => b.color),
            borderRadius: 8,
            maxBarThickness: 26,
          },
        ],
      },
      options: {
        indexAxis: "y",
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false }, tooltip: { ...tooltipStyle, callbacks: { label: (ctx) => ` ${fmt(ctx.parsed.x)} anuncios` } } },
        scales: {
          x: { beginAtZero: true, grid: { color: "rgba(255,255,255,0.05)" }, ticks: { callback: (v) => fmt(v) } },
          y: { grid: { display: false } },
        },
      },
    });
  }

  const demandEl = $("#chartDemand");
  if (demandEl) {
    charts.demand = new Chart(demandEl, {
      type: "bar",
      data: {
        labels: cats.map((c) => c.label.replace("Motos de ", "").replace("Bicicletas ", "Bici ")),
        datasets: [
          {
            label: "Vistas promedio",
            data: cats.map((c) => c.views),
            backgroundColor: ["rgba(0,229,255,0.85)", "rgba(124,92,255,0.85)", "rgba(255,138,61,0.9)", "rgba(244,114,182,0.85)"],
            borderRadius: 8,
            maxBarThickness: 54,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false }, tooltip: { ...tooltipStyle, callbacks: { label: (ctx) => ` ${fmt(ctx.parsed.y, 1)} vistas por anuncio` } } },
        scales: {
          x: { grid: { display: false }, ticks: { maxRotation: 0, autoSkip: false, font: { size: 10 } } },
          y: { beginAtZero: true, grid: { color: "rgba(255,255,255,0.05)" } },
        },
      },
    });
  }

  window.addEventListener("resize", () => {
    Object.values(charts).forEach((chart) => {
      if (chart && typeof chart.resize === "function") chart.resize();
    });
  });

  $$("[data-dash]").forEach((btn) =>
    btn.addEventListener("click", () => {
      $$("[data-dash]").forEach((b) => b.classList.remove("is-active"));
      btn.classList.add("is-active");
      const mode = btn.dataset.dash;
      const selected = mode === "comb" ? cats.filter((c) => c.key === "combustion") : mode === "elec" ? cats.filter((c) => c.key !== "combustion") : cats;
      if (charts.categories) {
        charts.categories.data.labels = selected.map((c) => c.label);
        charts.categories.data.datasets[0].data = selected.map((c) => c.count);
        charts.categories.data.datasets[0].backgroundColor = selected.map((c) => c.color);
        charts.categories.update();
      }
      if (charts.prices) {
        charts.prices.data.labels = selected.map((c) => c.label.replace("Motos de ", "").replace("Bicicletas ", "Bici "));
        charts.prices.data.datasets[0].data = selected.map((c) => c.price);
        charts.prices.data.datasets[0].backgroundColor = selected.map((c) => c.color);
        charts.prices.update();
      }
    })
  );
};

const initComparator = () => {
  const form = $("#priceForm");
  if (!form) return;
  const empty = $("#cmpEmpty");
  const content = $("#cmpContent");
  const tag = $("#cmpTag");
  const title = $("#cmpTitleResult");
  const text = $("#cmpText");
  const fill = $("#cmpFill");
  const marker = $("#cmpMarker");
  const stats = $("#cmpStats");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const key = $("#cmpCategory").value;
    const price = parseFloat($("#cmpPrice").value);
    if (!Number.isFinite(price) || price <= 0) {
      $("#cmpPrice").focus();
      return;
    }
    const data = MEDIANS[key];
    const diff = ((price - data.median) / data.median) * 100;
    let verdict;
    let className;
    if (price <= data.p25) {
      verdict = "Oferta excelente";
      className = "deal";
    } else if (price <= data.median) {
      verdict = "Buena oferta";
      className = "good";
    } else if (price <= data.p75) {
      verdict = "Precio normal";
      className = "normal";
    } else {
      verdict = "Precio elevado";
      className = "high";
    }

    const diffText = diff < 0 ? `${Math.abs(diff).toFixed(1)}% por debajo de la mediana` : `${diff.toFixed(1)}% por encima de la mediana`;

    tag.textContent = verdict;
    tag.className = `verdict-tag ${className}`;
    title.textContent = `${data.label}: ${fmt(price)} USD`;
    text.textContent = `${price <= data.p75 ? "Está dentro del rango habitual del mercado." : "Supera el rango habitual: hay margen para negociar o buscar alternativas."} El precio está ${diffText}.`;

    const scaleMax = data.p75 * 1.35;
    const pos = Math.min(Math.max((price / scaleMax) * 100, 2), 98);
    if (marker) marker.style.left = `${pos}%`;
    if (fill) fill.style.transform = `scaleX(${Math.max(1 - pos / 100, 0)})`;

    $("#cmpP25").textContent = `P25 ${fmt(data.p25)}`;
    $("#cmpMed").textContent = `Mediana ${fmt(data.median)}`;
    $("#cmpP75").textContent = `P75 ${fmt(data.p75)}`;

    const savings = Math.max(data.median - price, 0);
    stats.innerHTML = `
      <div><dt>Diferencia</dt><dd>${diff >= 0 ? "+" : ""}${diff.toFixed(1)}%</dd></div>
      <div><dt>Rango típico</dt><dd>${fmt(data.p25)} – ${fmt(data.p75)}</dd></div>
      <div><dt>${savings > 0 ? "Ahorro vs mediana" : "Sobreprecio"}</dt><dd>${fmt(Math.abs(data.median - price))} USD</dd></div>
    `;

    empty.style.display = "none";
    content.hidden = false;
  });
};

const initCalculator = () => {
  const form = $("#calcForm");
  if (!form) return;
  const brandFactor = { topmaq: 1.05, jmd: 0.95, mountain: 1.0, vedca: 0.9, challenger: 0.85, otra: 0.9 };
  const conditionFactor = { nueva: 1.15, "como-nueva": 1.0, usada: 0.85, reparar: 0.6 };

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const key = $("#calcCategory").value;
    const brand = $("#calcBrand").value;
    const condition = $("#calcCondition").value;
    const hasBattery = $("#calcBattery").checked;
    const hasPapers = $("#calcPapers").checked;
    const hasSecond = $("#calcSecond").checked;
    const base = MEDIANS[key].median;
    const electric = key !== "combustion";

    let factor = brandFactor[brand] * conditionFactor[condition];
    if (electric && hasBattery) factor += 0.22;
    if (electric && hasSecond) factor += 0.3;
    if (hasPapers) factor += 0.08;

    const mid = Math.round((base * factor) / 10) * 10;
    const low = Math.round((mid * 0.88) / 10) * 10;
    const high = Math.round((mid * 1.12) / 10) * 10;

    $("#calcLow").textContent = fmt(low);
    $("#calcHigh").textContent = fmt(high);
    const extras = [
      electric && hasBattery ? "batería nueva" : "",
      electric && hasSecond ? "segunda batería" : "",
      hasPapers ? "papeles en regla" : "",
    ].filter(Boolean);
    const article = key === "patinete" ? "Un" : "Una";
    $("#calcText").textContent = `${article} ${MEDIANS[key].label.toLowerCase()} ${condition === "nueva" ? "nueva" : condition === "reparar" ? "para reparar" : "en ese estado"}${extras.length ? `, con ${extras.join(" y ")}` : ""}, se movería en ese rango. Publica cerca del valor medio y negocia desde ahí.`;

    const bars = $("#calcBars");
    bars.hidden = false;
    const scale = high * 1.15;
    $("#calcBarLow").style.width = `${(low / scale) * 100}%`;
    $("#calcBarMid").style.width = `${(mid / scale) * 100}%`;
    $("#calcBarHigh").style.width = `${(high / scale) * 100}%`;
    $("#calcTagLow").textContent = `${fmt(low)} USD`;
    $("#calcTagMid").textContent = `${fmt(mid)} USD`;
    $("#calcTagHigh").textContent = `${fmt(high)} USD`;
  });
};

const NARRATION = [
  "Bienvenido a MotoMarket Insights Cuba, la plataforma de inteligencia de mercado para el sector de las motos en Cuba.",
  "Analizamos seis mil ciento cincuenta y nueve anuncios publicados en La Habana durante diecisiete días, y treinta entrevistas de campo a compradores, talleres e importadoras.",
  "El hallazgo principal: el setenta y siete punto seis por ciento de las motos y bicicletas publicadas es eléctrico. Las bicicletas eléctricas lideran con dos mil seiscientos cincuenta y tres anuncios, seguidas por las motos eléctricas con dos mil ciento veinticinco.",
  "En precios, la mediana de una moto de combustión es de dos mil trescientos dólares. Una moto eléctrica ronda los dos mil ciento setenta, una bicicleta eléctrica los mil ciento cincuenta, y un patinete los setecientos cincuenta.",
  "En marcas, Topmaq lidera la presencia del mercado con quinientos seis anuncios, seguida por J M D, Mountain, Vedca y Yoazaky.",
  "La combustión tiene menos oferta, pero genera más interés por anuncio: sesenta punto ocho vistas promedio, frente a catorce punto nueve en las motos eléctricas.",
  "Las entrevistas revelan que la batería, la autonomía, los apagones y la disponibilidad de repuestos son los principales dolores del mercado. También aparecen los papeles y la chapa como factores de riesgo.",
  "Las oportunidades están claras: servicios especializados de batería y carga, mantenimiento de motores eléctricos, importación de bicicletas y patinetes, y negocios de alquiler y mensajería.",
  "Explora el dashboard, compara precios y descubre si estás pagando de más. MotoMarket Insights Cuba convierte datos dispersos en decisiones inteligentes.",
];

const initNarrator = () => {
  const synth = window.speechSynthesis;
  const btn = $("#narrateBtn");
  const stop = $("#stopNarrate");
  const label = $("#narrateLabel");
  const status = $("#narrateStatus");
  const wave = $(".wave");
  if (!btn || !synth) {
    if (status) status.textContent = "La narración no está disponible en este navegador.";
    if (btn) btn.disabled = true;
    return;
  }

  let speaking = false;

  const reset = (message) => {
    speaking = false;
    label.textContent = "Escuchar resumen";
    status.textContent = message || "Listo para narrar los hallazgos principales.";
    stop.disabled = true;
    if (wave) wave.classList.remove("is-speaking");
  };

  const speak = () => {
    if (!("SpeechSynthesisUtterance" in window)) {
      status.textContent = "La narración no está disponible en este navegador.";
      return;
    }
    synth.cancel();
    const utterance = new SpeechSynthesisUtterance(NARRATION.join(" "));
    utterance.lang = "es-ES";
    utterance.rate = 0.98;
    utterance.pitch = 1;
    const voices = synth.getVoices();
    const spanish = voices.find((v) => /^es/i.test(v.lang));
    if (spanish) utterance.voice = spanish;
    utterance.onstart = () => {
      speaking = true;
      label.textContent = "Narrando…";
      status.textContent = "Reproduciendo el resumen del mercado.";
      stop.disabled = false;
      if (wave) wave.classList.add("is-speaking");
    };
    utterance.onend = () => reset();
    utterance.onerror = () => reset("No se pudo completar la narración.");
    label.textContent = "Preparando…";
    status.textContent = "Preparando la narración…";
    stop.disabled = false;
    window.setTimeout(() => {
      if (!speaking && !synth.speaking) {
        reset("La narración no está disponible en este dispositivo.");
      }
    }, 3500);
    synth.speak(utterance);
  };

  btn.addEventListener("click", () => {
    if (speaking) {
      synth.cancel();
      reset();
      return;
    }
    speak();
  });
  if (stop) {
    stop.addEventListener("click", () => {
      synth.cancel();
      reset();
    });
  }
  window.addEventListener("beforeunload", () => synth.cancel());

  const hero = $("#heroNarrate");
  if (hero) {
    hero.addEventListener("click", () => {
      document.getElementById("narrador").scrollIntoView({ behavior: "smooth", block: "center" });
      setTimeout(speak, 500);
    });
  }
};

const initGeoStats = () => {
  const data = window.MAPA_DATA;
  if (!data) return;
  const withData = data.municipios
    .filter((m) => m.anuncios > 0)
    .sort((a, b) => b.anuncios - a.anuncios);
  if (!withData.length) return;

  const top = withData[0];
  const min = Math.min(...withData.map((m) => m.anuncios));
  const bottoms = withData.filter((m) => m.anuncios === min);
  const set = (selector, text) => {
    const el = $(selector);
    if (el) el.textContent = text;
  };

  set("#geoTotal", fmt(data.georreferenciados));
  set("#geoTotalNote", `de ${fmt(data.dataset_total)} registros`);
  set("#geoCoverage", `${sharePct(data.georreferenciados, data.dataset_total, 2)}%`);
  set("#geoDiscardedNote", `${fmt(data.descartados)} sin municipio`);
  set("#geoTop", top.municipio);
  set("#geoTopCount", `${fmt(top.anuncios)} anuncios · ${sharePct(top.anuncios, data.georreferenciados)}% del total georreferenciado`);
  if (bottoms.length > 1) {
    set("#geoBottom", `${bottoms.length} municipios`);
    set("#geoBottomCount", `${bottoms.map((m) => m.municipio).join(", ")} · ${min} anuncio c/u`);
  } else {
    set("#geoBottom", bottoms[0].municipio);
    set("#geoBottomCount", `${min} anuncio · ${sharePct(min, data.georreferenciados)}%`);
  }

  const list = $("#mapRanking");
  if (list) {
    const max = top.anuncios;
    list.innerHTML = withData
      .map((m, index) => {
        const width = Math.max((m.anuncios / max) * 100, 3);
        const label = `${m.municipio}: ${m.anuncios} anuncios, ${sharePct(m.anuncios, data.georreferenciados)}% del total georreferenciado`;
        return `<li class="map-rank-row" aria-label="${label}">
          <span class="map-rank-pos">${String(index + 1).padStart(2, "0")}</span>
          <span class="map-rank-name">${m.municipio}</span>
          <div class="map-rank-bar"><span style="--w:${width}%"></span></div>
          <span class="map-rank-value">${fmt(m.anuncios)}</span>
          <span class="map-rank-share">${sharePct(m.anuncios, data.georreferenciados)}%</span>
        </li>`;
      })
      .join("");
  }

  const legendMin = $("#legendMin");
  const legendMid = $("#legendMid");
  const legendMax = $("#legendMax");
  if (legendMin && legendMid && legendMax) {
    legendMin.textContent = "0";
    legendMid.textContent = "10";
    legendMax.textContent = fmt(top.anuncios);
  }
};

const mapPopup = (m, data) => {
  const categories = [
    ["Bicicletas eléctricas", m.bicicletas_electricas],
    ["Motos eléctricas", m.motos_electricas],
    ["Motos de combustión", m.motos_combustion],
    ["Patinetes", m.patinetes],
  ]
    .filter(([, value]) => value > 0)
    .map(([label, value]) => `<span>${label}: <strong>${fmt(value)}</strong></span>`)
    .join("");
  const median = m.precio_mediano_usd
    ? `${fmt(m.precio_mediano_usd)} USD <small>(n=${fmt(m.n_precio_valido)})</small>`
    : "sin precio válido";
  return `<div class="map-popup">
    <strong>${m.municipio}</strong>
    <span class="map-popup-kicker">${fmt(m.anuncios)} anuncios · ${sharePct(m.anuncios, data.georreferenciados)}% del total georreferenciado</span>
    <div class="map-popup-cats">${categories}</div>
    <div class="map-popup-price">Precio mediano: <strong>${median}</strong></div>
    <div class="map-popup-source">Fuente: ${fmt(m.fuente_apollo)} Apollo + ${fmt(m.fuente_texto)} texto</div>
    <div class="map-popup-note">Asignación por municipio declarado; no es una dirección exacta.</div>
  </div>`;
};

const mapColor = (count) => {
  if (count >= 20) return "#ff4d5e";
  if (count >= 10) return "#ff8a3d";
  if (count >= 5) return "#f5c542";
  if (count > 0) return "#22c55e";
  return "#334155";
};

const initMap = () => {
  const el = $("#map");
  if (!el) return;
  const data = window.MAPA_DATA;
  if (typeof L === "undefined") {
    el.innerHTML = '<div class="map-error">No se pudo cargar Leaflet. Revisa la conexión e inténtalo de nuevo.</div>';
    return;
  }
  if (!data) {
    el.innerHTML = '<div class="map-error">No se encontró la capa geográfica real. Falta cargar mapa_datos.js.</div>';
    return;
  }
  const withData = data.municipios
    .filter((m) => m.anuncios > 0)
    .sort((a, b) => b.anuncios - a.anuncios);
  if (!withData.length) {
    el.innerHTML = '<div class="map-error">No hay anuncios con municipio identificable en el dataset.</div>';
    return;
  }
  const geoData = window.MAPA_GEO;
  if (!geoData || !Array.isArray(geoData.features) || !geoData.features.length) {
    el.innerHTML = '<div class="map-error">No se encontraron los límites municipales. Falta cargar mapa_municipios.js.</div>';
    return;
  }

  const map = L.map(el, {
    center: [23.08, -82.38],
    zoom: 11,
    zoomControl: true,
    scrollWheelZoom: false,
    attributionControl: true,
  });

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors | Límites: OSM Overpass',
    maxZoom: 19,
  }).addTo(map);

  const byName = new Map(data.municipios.map((m) => [m.municipio, m]));
  const top3 = new Set(withData.slice(0, 3).map((m) => m.municipio));

  const municipiosLayer = L.geoJSON(geoData, {
    style: (feature) => {
      const name = feature.properties.municipio;
      const record = byName.get(name);
      const count = record ? record.anuncios : 0;
      const isTop = top3.has(name);
      return {
        color: isTop ? "#fbbf24" : "#334155",
        weight: isTop ? 3 : 1.3,
        opacity: 1,
        fillColor: mapColor(count),
        fillOpacity: count > 0 ? 0.72 : 0.3,
        dashArray: count > 0 ? null : "4 4",
      };
    },
    onEachFeature: (feature, layer) => {
      const name = feature.properties.municipio;
      const record = byName.get(name);
      if (!record || record.anuncios === 0) {
        layer.bindTooltip(`${name} · sin anuncios`, { direction: "top", className: "map-tooltip" });
        layer.bindPopup(`<div class="map-popup">
          <strong>${name}</strong>
          <span class="map-popup-kicker">Sin anuncios con municipio identificable.</span>
          <div class="map-popup-note">No se imputaron datos ni coordenadas.</div>
        </div>`);
      } else {
        layer.bindPopup(mapPopup(record, data));
        const isTop = top3.has(name);
        const position = withData.findIndex((m) => m.municipio === name) + 1;
        layer.bindTooltip(
          isTop ? `#${position} · ${name} — ${fmt(record.anuncios)} anuncios` : `${name} · ${fmt(record.anuncios)} anuncios`,
          {
            direction: "top",
            offset: [0, -6],
            className: isTop ? "map-tooltip map-tooltip-top" : "map-tooltip",
          }
        );
      }
      layer.on({
        mouseover: (event) => {
          event.target.setStyle({ weight: top3.has(name) ? 4 : 3, color: "#ffffff" });
          event.target.bringToFront();
        },
        mouseout: () => municipiosLayer.resetStyle(layer),
      });
    },
  }).addTo(map);

  const topBadges = L.layerGroup();
  withData.slice(0, 3).forEach((m, index) => {
    L.marker([m.lat, m.lon], {
      icon: L.divIcon({
        className: "map-top-badge-wrap",
        html: `<span class="map-top-badge">#${index + 1}</span>`,
        iconSize: [30, 30],
        iconAnchor: [[30, 30], [0, 0], [15, 30]][index] || [15, 15],
      }),
      interactive: true,
      keyboard: false,
      zIndexOffset: 1000,
    })
      .bindTooltip(`#${index + 1} · ${m.municipio} — ${fmt(m.anuncios)} anuncios`, {
        direction: "top",
        className: "map-tooltip map-tooltip-top",
      })
      .bindPopup(mapPopup(m, data))
      .addTo(topBadges);
  });

  const pins = L.layerGroup();
  withData.forEach((m) => {
    const color = mapColor(m.anuncios);
    const radius = 7 + Math.sqrt(m.anuncios) * 4.4;
    L.circleMarker([m.lat, m.lon], {
      radius,
      color,
      weight: 2,
      fillColor: color,
      fillOpacity: 0.55,
    })
      .bindPopup(mapPopup(m, data))
      .bindTooltip(`${m.municipio} · ${fmt(m.anuncios)} anuncios`, { direction: "top", className: "map-tooltip" })
      .addTo(pins);
  });

  map.fitBounds(municipiosLayer.getBounds().pad(0.04));

  const municipiosBtn = $("#mapHeatBtn");
  const pinsBtn = $("#mapPinsBtn");

  const setMode = (mode) => {
    if (mode === "municipios") {
      if (!map.hasLayer(municipiosLayer)) municipiosLayer.addTo(map);
      if (!map.hasLayer(topBadges)) topBadges.addTo(map);
      if (map.hasLayer(pins)) map.removeLayer(pins);
    } else {
      if (map.hasLayer(municipiosLayer)) map.removeLayer(municipiosLayer);
      if (map.hasLayer(topBadges)) map.removeLayer(topBadges);
      if (!map.hasLayer(pins)) pins.addTo(map);
    }
  };

  setMode("municipios");

  if (municipiosBtn && pinsBtn) {
    municipiosBtn.addEventListener("click", () => {
      municipiosBtn.classList.add("is-active");
      pinsBtn.classList.remove("is-active");
      setMode("municipios");
    });
    pinsBtn.addEventListener("click", () => {
      pinsBtn.classList.add("is-active");
      municipiosBtn.classList.remove("is-active");
      setMode("pins");
    });
  }

  setTimeout(() => map.invalidateSize(), 300);
  window.addEventListener("resize", () => map.invalidateSize());
  const section = $("#mapa");
  if (section && "IntersectionObserver" in window) {
    const obs = new IntersectionObserver(
      (entries) => entries.forEach((entry) => entry.isIntersecting && map.invalidateSize()),
      { threshold: 0.2 }
    );
    obs.observe(section);
  }
};

const copyText = async (text) => {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text);
    return true;
  }
  const area = document.createElement("textarea");
  area.value = text;
  area.style.position = "fixed";
  area.style.opacity = "0";
  document.body.appendChild(area);
  area.focus();
  area.select();
  let ok = false;
  try {
    ok = document.execCommand("copy");
  } catch (error) {
    ok = false;
  }
  document.body.removeChild(area);
  return ok;
};

const initShare = () => {
  $$(".btn-share").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const text = btn.dataset.share || "Descubre el mercado de motos en Cuba con MotoMarket Insights.";
      if (navigator.share) {
        try {
          await navigator.share({ title: "MotoMarket Insights Cuba", text, url: window.location.href });
          return;
        } catch (error) {
          if (error && error.name === "AbortError") return;
        }
      }
      const ok = await copyText(`${text} ${window.location.href}`);
      btn.classList.add("is-copied");
      btn.textContent = ok ? "¡Copiado!" : "No se pudo copiar";
      setTimeout(() => {
        btn.classList.remove("is-copied");
        btn.textContent = "Compartir";
      }, 2000);
    });
  });
};

const QUIZ = [
  {
    question: "¿Qué porcentaje de la oferta observada es eléctrica?",
    options: ["62,0%", "77,6%", "45,0%", "90,0%"],
    correct: 1,
    explanation: "El 77,6% de los anuncios son motos y bicicletas eléctricas.",
  },
  {
    question: "¿Qué categoría concentra más anuncios?",
    options: ["Motos eléctricas", "Bicicletas eléctricas", "Motos de combustión", "Patinetes"],
    correct: 1,
    explanation: "Las bicicletas eléctricas lideran con 2.653 anuncios.",
  },
  {
    question: "¿Qué marca tiene mayor presencia en el mercado?",
    options: ["JMD", "Mountain", "Topmaq", "Vedca"],
    correct: 2,
    explanation: "Topmaq lidera con 506 anuncios publicados.",
  },
  {
    question: "¿Cuál es el precio mediano de una moto de combustión?",
    options: ["1.150 USD", "2.300 USD", "3.100 USD", "750 USD"],
    correct: 1,
    explanation: "La mediana de combustión es 2.300 USD.",
  },
  {
    question: "¿Qué categoría genera más vistas promedio por anuncio?",
    options: ["Bicicletas eléctricas", "Motos eléctricas", "Motos de combustión", "Patinetes"],
    correct: 2,
    explanation: "Combustión promedia 60,8 vistas por anuncio, muy por encima del resto.",
  },
  {
    question: "¿Qué problemas aparecen con más fuerza en las entrevistas?",
    options: ["Diseño y color", "Apagones y batería", "Velocidad máxima", "Tamaño del motor"],
    correct: 1,
    explanation: "Los apagones, la autonomía y la batería son los dolores más mencionados.",
  },
];

const initQuiz = () => {
  const card = $("#quizCard");
  if (!card) return;
  const stepEl = $("#quizStep");
  const scoreEl = $("#quizScore");
  const progressEl = $("#quizProgress");
  const questionEl = $("#quizQuestion");
  const optionsEl = $("#quizOptions");
  const feedbackEl = $("#quizFeedback");
  const restart = $("#quizRestart");

  let index = 0;
  let score = 0;
  let answered = false;

  const render = () => {
    if (index >= QUIZ.length) {
      stepEl.textContent = "Quiz completado";
      scoreEl.textContent = `${score} / ${QUIZ.length} pts`;
      progressEl.style.width = "100%";
      questionEl.textContent = score === QUIZ.length ? "¡Perfecto! Dominas el mercado." : score >= 4 ? "Buen ojo para el mercado." : "Hay margen para seguir explorando.";
      optionsEl.innerHTML = "";
      feedbackEl.className = "quiz-feedback";
      feedbackEl.textContent = `Has acertado ${score} de ${QUIZ.length} preguntas. ${score >= 4 ? "Comparte tu resultado y reta a alguien." : "Vuelve al dashboard y prueba de nuevo."}`;
      restart.hidden = false;
      return;
    }

    answered = false;
    restart.hidden = true;
    const item = QUIZ[index];
    stepEl.textContent = `Pregunta ${index + 1} de ${QUIZ.length}`;
    scoreEl.textContent = `${score} pts`;
    progressEl.style.width = `${(index / QUIZ.length) * 100}%`;
    questionEl.textContent = item.question;
    feedbackEl.className = "quiz-feedback";
    feedbackEl.textContent = "";
    optionsEl.innerHTML = "";

    item.options.forEach((option, i) => {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = option;
      button.addEventListener("click", () => {
        if (answered) return;
        answered = true;
        const correct = i === item.correct;
        if (correct) {
          score += 1;
          button.classList.add("correct");
          feedbackEl.className = "quiz-feedback good";
        } else {
          button.classList.add("wrong");
          optionsEl.children[item.correct].classList.add("correct");
          feedbackEl.className = "quiz-feedback bad";
        }
        feedbackEl.textContent = item.explanation;
        scoreEl.textContent = `${score} pts`;
        Array.from(optionsEl.children).forEach((child) => (child.disabled = true));
        setTimeout(() => {
          index += 1;
          render();
        }, 1800);
      });
      optionsEl.appendChild(button);
    });
  };

  restart.addEventListener("click", () => {
    index = 0;
    score = 0;
    render();
  });

  render();
};

const initGuess = () => {
  const grid = $("#guessGrid");
  if (!grid) return;
  const feedback = $("#guessFeedback");
  grid.addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button || button.disabled) return;
    const correct = button.dataset.guess === "topmaq";
    Array.from(grid.children).forEach((child) => {
      child.disabled = true;
      if (child.dataset.guess === "topmaq") child.classList.add("correct");
    });
    if (!correct) button.classList.add("wrong");
    feedback.className = `guess-feedback ${correct ? "good" : "bad"}`;
    feedback.textContent = correct ? "Exacto: Topmaq lidera con 506 anuncios." : "Casi. La líder es Topmaq, con 506 anuncios.";
  });
};

const BUYER_QUESTIONS = [
  {
    question: "¿Qué pesa más cuando eliges una moto?",
    options: [
      { label: "El precio", type: "cazador" },
      { label: "La tecnología y el ahorro", type: "explorador" },
      { label: "La fiabilidad", type: "pragmatico" },
      { label: "El uso para negocio", type: "emprendedor" },
    ],
  },
  {
    question: "¿Qué harías con la moto?",
    options: [
      { label: "Buscar la mejor oferta", type: "cazador" },
      { label: "Moverme por la ciudad", type: "explorador" },
      { label: "Viajar y trabajar sin fallos", type: "pragmatico" },
      { label: "Mensajería, alquiler o reparto", type: "emprendedor" },
    ],
  },
  {
    question: "¿Qué te frena al comprar?",
    options: [
      { label: "Pagar de más", type: "cazador" },
      { label: "La batería y los apagones", type: "explorador" },
      { label: "Los repuestos y la mecánica", type: "pragmatico" },
      { label: "Que no genere ingresos", type: "emprendedor" },
    ],
  },
];

const BUYER_RESULTS = {
  cazador: "Cazador de ofertas: tu ventaja está en comparar precios y negociar con datos.",
  explorador: "Explorador eléctrico: te atrae la movilidad eléctrica, pero vigila batería y carga.",
  pragmatico: "Pragmático de combustión: priorizas fiabilidad, repuestos y rendimiento.",
  emprendedor: "Emprendedor de movilidad: ves la moto como herramienta de negocio.",
};

const initBuyerGame = () => {
  const container = $("#buyerQuestions");
  const result = $("#buyerResult");
  if (!container || !result) return;

  const answers = new Array(BUYER_QUESTIONS.length).fill(null);

  BUYER_QUESTIONS.forEach((item, qi) => {
    const wrapper = document.createElement("div");
    wrapper.className = "buyer-q";
    const title = document.createElement("span");
    title.textContent = item.question;
    const opts = document.createElement("div");
    opts.className = "opts";
    item.options.forEach((option) => {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = option.label;
      button.addEventListener("click", () => {
        Array.from(opts.children).forEach((child) => child.classList.remove("is-active"));
        button.classList.add("is-active");
        answers[qi] = option.type;
        if (answers.every(Boolean)) {
          const tally = {};
          answers.forEach((type) => (tally[type] = (tally[type] || 0) + 1));
          const winner = Object.keys(tally).sort((a, b) => tally[b] - tally[a])[0];
          result.textContent = BUYER_RESULTS[winner];
        }
      });
      opts.appendChild(button);
    });
    wrapper.appendChild(title);
    wrapper.appendChild(opts);
    container.appendChild(wrapper);
  });
};

const COMPARE_MODES = {
  price: { comb: 2300, elec: 2170, unit: "USD", note: "La combustión cuesta un 6,0% más y tiene menos oferta, pero genera más interés por anuncio." },
  views: { comb: 60.8, elec: 14.9, unit: "vistas/anuncio", note: "La combustión genera más de 4 veces el interés por anuncio de una moto eléctrica." },
  offer: { comb: 1137, elec: 2125, unit: "anuncios", note: "Hay casi el doble de motos eléctricas publicadas que de motos de combustión." },
};

const initCompare = () => {
  const buttons = $$("[data-compare]");
  if (!buttons.length) return;
  const combValue = $("#compareCombValue");
  const elecValue = $("#compareElecValue");
  const unit = $("#compareUnit");
  const unit2 = $("#compareUnit2");
  const combBar = $("#compareCombBar");
  const elecBar = $("#compareElecBar");
  const note = $("#compareNote");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      buttons.forEach((b) => b.classList.remove("is-active"));
      button.classList.add("is-active");
      const mode = COMPARE_MODES[button.dataset.compare];
      const max = Math.max(mode.comb, mode.elec);
      combValue.textContent = fmt(mode.comb, mode.unit === "vistas/anuncio" ? 1 : 0);
      elecValue.textContent = fmt(mode.elec, mode.unit === "vistas/anuncio" ? 1 : 0);
      unit.textContent = mode.unit;
      unit2.textContent = mode.unit;
      combBar.style.width = `${(mode.comb / max) * 100}%`;
      elecBar.style.width = `${(mode.elec / max) * 100}%`;
      note.textContent = mode.note;
    });
  });
};

const boot = () => {
  initNav();
  initScroll();
  initReveal();
  animateCounters();
  initCharts();
  initComparator();
  initCalculator();
  initNarrator();
  initGeoStats();
  initMap();
  initShare();
  initQuiz();
  initGuess();
  initBuyerGame();
  initCompare();
};

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", boot);
} else {
  boot();
}

if (window.speechSynthesis) {
  window.speechSynthesis.onvoiceschanged = () => {};
}
