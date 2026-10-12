<div align="center">

# 🌲 Nusantara Wildfire Early Warning
### Predictive Early Warning & Susceptibility Mapping for Tropical Peatland Wildfires (*Karhutla*) in Indonesia
**Remote Sensing & Machine Learning · Environmental Data Science · Master's Thesis Track**

[![Python CI](https://github.com/KevinNaserwan/nusantara-wildfire-earlywarning/actions/workflows/ci.yml/badge.svg)](https://github.com/KevinNaserwan/nusantara-wildfire-earlywarning/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![LightGBM](https://img.shields.io/badge/Model-LightGBM%20%2F%20XGBoost-blue.svg)](https://lightgbm.readthedocs.io/)
[![GeoPandas](https://img.shields.io/badge/GIS-GeoPandas-green.svg)](https://geopandas.org/)

</div>

---

## 📌 Problem Statement & Environmental Urgency

Indonesia contains over **13.4 million hectares of tropical peatland ecosystems**, primarily across Sumatra (Riau, South Sumatra) and Kalimantan. Drained and degraded peat layers are highly susceptible to subterranean smoldering combustion during dry seasons (aggravated by positive IOD and El Niño anomalies), generating severe transboundary toxic haze and monumental greenhouse gas emissions.

### Paradigm Shift: Reactive $\longrightarrow$ Proactive
- **Traditional Approach (Reactive)**: Relies on thermal anomalies (MODIS/VIIRS thermal hotspots) detected *after* ignition has already occurred and underground fires have spread.
- **This Framework (Proactive)**: Delivers a **3-to-7 day pre-ignition susceptibility forecast** by correlating satellite canopy moisture indices, meteorological drought persistence, and proximity to artificial drainage canal networks.

---

## 🏛️ Pipeline Architecture

```
+-------------------------------------------------------------------------+
|                PEATLAND WILDFIRE EARLY WARNING PIPELINE                 |
+-------------------------------------------------------------------------+

 [ Multi-Source Satellite & Telemetry Streams (NASA FIRMS / Sentinel / ERA5) ]
                                    |
                                    v
 +---------------------------------------------------------------------+
 |                     DATA INGESTION & PROCESSING                     |
 +----------------------------------+----------------------------------+
                                    |
      +--------------------+--------+--------+--------------------+
      |                    |                 |                    |
      v (Sentinel-2)       v (ERA5 / BMKG)   v (Spatial BRGM)     v (Hydrology)
 +-----------------+ +-----------------+ +-----------------+ +-----------------+
 | Moisture & Fuel | | Meteorology:    | | Peat Hydro Unit | | Canal Proximity |
 | NDMI, NBR, SWIR | | CDD, Temp, Wind | | KHG Typology    | | Drainage Index  |
 +--------+--------+ +--------+--------+ +--------+--------+ +--------+--------+
          |                   |                   |                   |
          +-------------------+---------+---------+-------------------+
                                        |
                                        v
 +---------------------------------------------------------------------+
 |                  SPATIAL FEATURE AGGREGATOR ENGINE                  |
 +--------------------------------------+------------------------------+
                                        |
                                        v
 +---------------------------------------------------------------------+
 |         Spatial Cross-Validation LightGBM Risk Classifier           |
 +--------------------------------------+------------------------------+
                                        |
                                        v
 +---------------------------------------------------------------------+
 |                 MULTI-CRITERIA EARLY WARNING ENGINE                 |
 +--------------------------------------+------------------------------+
                                        |
                     +------------------+------------------+
                     |                                     |
                     v                                     v
 [ Alert Levels: LOW / MODERATE / HIGH / EXTREME ]   [ Risk GeoTIFF & Map ]
```

---

## 📐 Mathematical Formulations

### 1. Fuel Moisture & Peatland Spectral Indices
$$\text{NDMI} = \frac{\text{NIR} - \text{SWIR1}}{\text{NIR} + \text{SWIR1}} = \frac{B8 - B11}{B8 + B11} \quad \text{(Direct proxy for canopy and peat surface moisture)}$$

$$\text{NBR} = \frac{\text{NIR} - \text{SWIR2}}{\text{NIR} + \text{SWIR2}} = \frac{B8 - B12}{B8 + B12} \quad \text{(Normalized Burn Ratio)}$$

$$\Delta\text{NBR} = \text{NBR}_{\text{pre-fire}} - \text{NBR}_{\text{post-fire}} \quad \text{(Post-fire burn severity)}$$

### 2. Peat Drainage Canal Vulnerability Decay
Artificial drainage canals artificially drop the groundwater table (*Tinggi Muka Air Tanah - TMAT*). Vulnerability weight $w_{\text{canal}}$ decays exponentially with Euclidean distance $d$ (meters) to the nearest canal:

$$w_{\text{canal}}(d) = \exp\left(-\frac{d}{\sigma_{\text{canal}}}\right), \quad \sigma_{\text{canal}} \approx 250\text{ m}$$

---

## 📂 Project Structure

```
nusantara-wildfire-earlywarning/
├── data/
│   ├── raw/                 # MODIS/VIIRS hotspot catalogs & KHG boundary polygons
│   └── processed/           # Feature matrices with spatial environmental joins
├── docs/                    # KHG classification documentation & thesis drafts
├── notebooks/               # Case studies on Riau & Pulang Pisau (Central Kalimantan)
│   └── 01_hotspot_spatial_analysis.ipynb
├── src/
│   ├── fire_indices.py      # NBR, NDMI, dNBR spectral calculation routines
│   ├── early_warning.py     # Multi-criteria susceptibility scoring & alert engine
│   ├── canal_risk.py        # Drainage canal proximity spatial decay model
│   └── spatial_matcher.py   # Ray-casting point-in-polygon spatial matcher
├── tests/                   # Automated pytest suites
└── requirements.txt         # Dependencies
```

---

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone git@github.com:KevinNaserwan/nusantara-wildfire-earlywarning.git
cd nusantara-wildfire-earlywarning

# Install dependencies
pip install -r requirements.txt
```

### Run Risk Classification Demo
```bash
python -c "from src.early_warning import PeatlandFireRiskClassifier; res = PeatlandFireRiskClassifier.classify_risk(ndmi=0.07, consecutive_dry_days=14, distance_to_canal_meters=120.0, temperature_celsius=36.5); print('Risk Result:', res)"
```

---

## 🔬 Scientific Roadmap & Publication Targets
- [x] Peatland-specific spectral indices (NDMI, NBR, dNBR)
- [x] Multi-criteria early warning risk grading engine
- [ ] Integration with ground-truth BRGM PRIMS telemetry (TMAT sensor logs)
- [ ] Spatial Cross-Validation training on 2019-2023 historical wildfire occurrences
- [ ] Target Publication: *Environmental Data Science (Cambridge)* or *International Journal of Wildland Fire*.

---

## 👤 Author & Research Citation
- **Principal Investigator**: Kevin Putrayudha Naserwan ([@KevinNaserwan](https://github.com/KevinNaserwan))
- **Affiliation**: Universitas Sriwijaya (Alumnus) · Master's Thesis Research Track
