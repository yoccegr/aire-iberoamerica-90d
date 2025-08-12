\
"""
Descarga datos de PM2.5 de OpenAQ para los últimos 90 días
para 5 capitales iberoamericanas y los agrega a promedio diario por ciudad.

Uso:
    python src/fetch_openaq_pm25.py

Salida:
    data/pm25_raw_90d.csv  (registros crudos)
    data/pm25_90d.csv      (promedio diario por ciudad)
"""
import os
import time
import math
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# --- Config ---
PARAM = "pm25"
DAYS = 90
# Capitales objetivo
TARGETS = [
    ("Santiago","CL"),
    ("Mexico City","MX"),
    ("Bogotá","CO"),
    ("Madrid","ES"),
    ("Brasília","BR"),
]

# Variantes de nombre por ciudad en OpenAQ
CITY_VARIANTS = {
    ("Santiago","CL"): ["Santiago"],
    ("Mexico City","MX"): ["Mexico City","Ciudad de México","Ciudad de Mexico","CDMX"],
    ("Bogotá","CO"): ["Bogotá","Bogota"],
    ("Madrid","ES"): ["Madrid"],
    ("Brasília","BR"): ["Brasília","Brasilia"],
}

OUT_RAW = "data/pm25_raw_90d.csv"
OUT_CLEAN = "data/pm25_90d.csv"

# Rango de fechas (UTC)
date_to = datetime.now(timezone.utc)
date_from = date_to - timedelta(days=DAYS)

def fetch_city(city, country):
    """
    Descarga measurements de OpenAQ v2 para una ciudad/país en el rango de 90 días.
    Pagina automáticamente hasta traer todo.
    Retorna DataFrame con columnas: datetime_utc, value, unit, city, country, location, latitude, longitude
    """
    base = "https://api.openaq.org/v2/measurements"
    params = {
        "parameter": PARAM,
        "country": country,
        "city": city,
        "date_from": date_from.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "date_to": date_to.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "limit": 10000,          # máximo por página
        "page": 1,
        "sort": "desc",
        "order_by": "date"
    }
    rows = []
    while True:
        r = requests.get(base, params=params, timeout=60)
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        if not results:
            break
        for it in results:
            dt = it.get("date", {}).get("utc")
            val = it.get("value")
            unit = it.get("unit")
            loc = it.get("location")
            coords = it.get("coordinates", {}) or {}
            lat, lon = coords.get("latitude"), coords.get("longitude")
            rows.append({
                "datetime_utc": dt,
                "value": val,
                "unit": unit,
                "city": city,
                "country": country,
                "location": loc,
                "latitude": lat,
                "longitude": lon
            })
        # Paginación
        meta = data.get("meta", {})
        found = meta.get("found", 0)
        limit = meta.get("limit", 10000)
        page = meta.get("page", params["page"])
        total_pages = math.ceil(found / limit) if limit else 1
        if page >= total_pages:
            break
        params["page"] = page + 1
        time.sleep(0.4)  # gentil con la API
    return pd.DataFrame(rows)

def try_fetch_with_variants(city_key):
    """
    Intenta descargar datos probando variantes de nombre de ciudad.
    Devuelve (df, variant_usada) o (df_vacio, None) si no hubo éxito.
    """
    variants = CITY_VARIANTS.get(city_key, [city_key[0]])
    country = city_key[1]
    for variant in variants:
        print(f"  - Intentando '{variant}' ...")
        df = fetch_city(variant, country)
        if not df.empty:
            df["city"] = city_key[0]  # normaliza al nombre 'canónico'
            df["country"] = country
            return df, variant
    return pd.DataFrame(), None

def main():
    os.makedirs("data", exist_ok=True)
    frames = []
    for (city, country) in TARGETS:
        print(f"Descargando {city} ({country}) en últimos {DAYS} días...")
        dfc, used = try_fetch_with_variants((city, country))
        if dfc.empty:
            print(f"⚠️  Sin datos para {city} ({country}). Revisa nombre o parámetro.")
            continue
        if used and used != city:
            print(f"   ✔ Usando variante encontrada: '{used}'")
        frames.append(dfc)

    if not frames:
        print("❌ No se descargaron datos para ninguna ciudad. Aborta.")
        return

    df = pd.concat(frames, ignore_index=True).dropna(subset=["datetime_utc","value"])
    df.to_csv(OUT_RAW, index=False)
    print(f"✔ Guardado crudo: {OUT_RAW} ({len(df):,} filas)")

    # Limpieza y agregación diaria por ciudad
    df["datetime_utc"] = pd.to_datetime(df["datetime_utc"], utc=True)
    df["date"] = df["datetime_utc"].dt.date
    daily = (
        df.groupby(["country","city","date"], as_index=False)
          .agg(pm25=("value","mean"),
               n_obs=("value","size"),
               lat=("latitude","median"),
               lon=("longitude","median"))
    )

    daily.to_csv(OUT_CLEAN, index=False)
    print(f"✔ Guardado limpio: {OUT_CLEAN} ({len(daily):,} filas)")
    print(daily.head())

if __name__ == "__main__":
    main()
