
# 🪙 Meme Crypto Time Series Analysis

Este proyecto construye un pipeline completo para la recolección, limpieza y análisis de criptomonedas categorizadas como *memecoins*.  
Utiliza las APIs de **CoinMarketCap** y **TwelveData** para extraer información de mercado y crear datasets procesables para análisis de series temporales.

---

## 📁 Estructura del repositorio

```

eda.ipynb                # Análisis exploratorio de datos (EDA)
script.py                # Obtiene memecoins desde CoinMarketCap
time_series.py           # Descarga datos históricos desde TwelveData
to_csv.py                # Convierte JSON limpios a CSV
clean_data.json / .csv   # Datos finales procesados
memecoins.csv            # Dataset inicial

````

---

## ⚙️ Requisitos

- **Python 3.10+**
- Dependencias principales:
  ```bash
  pip install requests flatten_json pandas matplotlib
  ````

* APIs necesarias:

  * [CoinMarketCap API](https://coinmarketcap.com/api/)
  * [TwelveData API](https://twelvedata.com/docs)

Configura tus API keys directamente en los scripts o mediante variables de entorno.

---

## 🚀 Ejecución paso a paso

### 1. Obtener lista de memecoins

```bash
python script.py
```

Genera el archivo `memecoins.csv` con metadatos de las principales memecoins.

### 2. Descargar series temporales

```bash
python time_series.py
```

Obtiene datos históricos (3 años por símbolo) y los guarda en `time_series_data.json` y `clean_data.json`.

### 3. Convertir a CSV

```bash
python to_csv.py
```

Crea `clean_data.csv` para facilitar el análisis en notebooks o Power BI.

### 4. Ejecutar análisis exploratorio

Abre y corre `eda.ipynb` para visualizar patrones, tendencias y estadísticas descriptivas de las memecoins.

---

## 📊 Resultados esperados

* Dataset limpio con valores de apertura, cierre, máximo, mínimo y volumen.
* Comparativa de precios históricos entre diferentes memecoins.
* Visualizaciones temporales y métricas básicas de correlación.

---

## 🧩 Aplicaciones posibles

* Modelado predictivo de precios con ML.
* Análisis de volatilidad en el mercado *meme*.
* Dashboard financiero con Power BI o Streamlit.

---



```



