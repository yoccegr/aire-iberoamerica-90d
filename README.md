# Calidad del aire en Iberoamérica (últimos 90 días)

Comparación de **PM2.5** en cinco capitales iberoamericanas: **Santiago (CL), Ciudad de México (MX), Bogotá (CO), Madrid (ES) y Brasília (BR)**.
Período: últimos 90 días desde la fecha de descarga.

**Fuente:** [OpenAQ](https://openaq.org) — datos abiertos.  
**Fecha de creación del proyecto:** 2025-08-12

## Estructura
```
aire-iberoamerica-90d/
├─ data/
│  ├─ pm25_raw_90d.csv    # crudo desde API OpenAQ
│  └─ pm25_90d.csv        # limpio y agregado diario por ciudad
├─ notebooks/
│  └─ 01_visualizacion_pm25.ipynb
├─ src/
│  └─ fetch_openaq_pm25.py
├─ .gitignore
├─ requirements.txt
└─ README.md
```

## Reproducir
1. Crear entorno e instalar dependencias:
   - Windows (PowerShell)
     ```powershell
     cd aire-iberoamerica-90d
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     pip install -r requirements.txt
     ```
   - macOS/Linux
     ```bash
     cd aire-iberoamerica-90d
     python3 -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     ```

2. Descargar y preparar datos (API OpenAQ v2 — últimos 90 días):
   ```bash
   python src/fetch_openaq_pm25.py
   ```

3. Abrir el notebook y generar visualizaciones:
   - En VS Code: abre la carpeta y ejecuta `notebooks/01_visualizacion_pm25.ipynb`.
   - O con Jupyter:
     ```bash
     pip install jupyter
     jupyter notebook notebooks/01_visualizacion_pm25.ipynb
     ```

## Visualizaciones
- **Mapa interactivo** (`scatter_geo`): tamaño y color = promedio PM2.5 por ciudad (últimos 90 días).
- **Serie temporal** (`line`): evolución diaria, con línea guía **OMS 24h ≈ 15 µg/m³**.

## Notas y buenas prácticas
- Si alguna ciudad viene sin datos, el script prueba variantes de nombre (p. ej., *Mexico City / Ciudad de México*).
- Los promedios diarios se calculan en **UTC** (consistencia temporal).
- Recomendado: describir **2–3 hallazgos** en el README (picos estacionales, ciudad con menor promedio, variación semanal).

## Licencia
Uso libre citando la fuente (OpenAQ).
