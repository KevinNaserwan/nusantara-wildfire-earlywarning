# Nusantara Wildfire Early Warning

[![Python CI](https://github.com/KevinNaserwan/nusantara-wildfire-earlywarning/actions/workflows/ci.yml/badge.svg)](https://github.com/KevinNaserwan/nusantara-wildfire-earlywarning/actions)

Predictive early warning system and susceptibility mapping for **tropical peatland wildfires (*Kebakaran Hutan dan Lahan / Karhutla*) in Indonesia** using multi-sensor satellite remote sensing (Sentinel-1/2, MODIS/VIIRS) and machine learning.

## National Urgency & Research Background
Indonesia houses over 13 million hectares of tropical peatlands (notably in Riau, South Sumatra, West and Central Kalimantan). During dry seasons, drained and degraded peat layers become fuel for smoldering, subterranean fires that produce toxic transboundary haze and massive CO2 emissions.

Traditional monitoring is reactive (detecting active hotspots after ignition). This project provides a **proactive 3-to-7 day pre-ignition risk forecast** by fusing:
- **Peat Moisture Proxies**: NDMI & Sentinel-1 SAR moisture variation.
- **Canal Drainage Drainage Network**: Proximity to artificial canals lowering the groundwater table (*Tinggi Muka Air Tanah - TMAT*).
- **Meteorological Drivers**: Consecutive dry days (CDD) and surface temperature anomalies.

## Project Structure
```
├── data/
│   ├── raw/             # Historical MODIS/VIIRS hotspots & KHG polygon boundaries
│   └── processed/       # Spatially-joined environmental susceptibility features
├── src/
│   ├── fire_indices.py  # NBR, NDMI, dNBR burn severity calculations
│   └── early_warning.py # Multi-factor risk rating & alert classifier
├── notebooks/           # Case studies on Riau & Pulang Pisau (Central Kalimantan)
└── requirements.txt
```

## Quick Start
```bash
pip install -r requirements.txt
python -c "from src.early_warning import PeatlandFireRiskClassifier; print(PeatlandFireRiskClassifier.classify_risk(0.08, 15, 150, 36.0))"
```

## Research Roadmap
- [x] Specialized peatland spectral indices (NDMI, NBR, dNBR)
- [x] Multi-criteria early warning risk grading engine
- [ ] Integration with BRGM (Badan Restorasi Gambut dan Mangrove) sensor network telemetry
- [ ] Spatial cross-validation with LightGBM/XGBoost on 2019-2023 historical fire seasons
- [ ] Publication manuscript target: Environmental Data Science / IEEE JSTARS

## License
MIT
