"""
Early Warning System & Peatland Wildfire Risk Scoring Engine.
"""
from typing import Dict, Any, List
import numpy as np

class PeatlandFireRiskClassifier:
    """
    Evaluates multi-factor susceptibility indicators:
    - Canopy & Peat moisture (NDMI)
    - Consecutive Dry Days (CDD)
    - Distance to canal drainage network (Canal drainage lowers groundwater table)
    - Surface Temperature anomaly
    """

    @staticmethod
    def classify_risk(
        ndmi: float,
        consecutive_dry_days: int,
        distance_to_canal_meters: float,
        temperature_celsius: float
    ) -> Dict[str, Any]:
        """
        Returns risk score [0.0 - 1.0] and alert level: LOW, MODERATE, HIGH, EXTREME.
        """
        score = 0.0

        # Dryness penalty (Lower NDMI = drier vegetation and peat surface)
        if ndmi < 0.1:
            score += 0.35
        elif ndmi < 0.25:
            score += 0.20
        else:
            score += 0.05

        # Drought duration penalty
        if consecutive_dry_days >= 14:
            score += 0.35
        elif consecutive_dry_days >= 7:
            score += 0.20
        elif consecutive_dry_days >= 3:
            score += 0.10

        # Proximity to drained peat canals (drained peat is highly flammable)
        if distance_to_canal_meters <= 200:
            score += 0.20
        elif distance_to_canal_meters <= 500:
            score += 0.10

        # Thermal anomaly
        if temperature_celsius >= 35.0:
            score += 0.10

        score = float(np.clip(score, 0.0, 1.0))

        if score >= 0.75:
            level = "EXTREME"
        elif score >= 0.50:
            level = "HIGH"
        elif score >= 0.30:
            level = "MODERATE"
        else:
            level = "LOW"

        return {
            "risk_score": score,
            "alert_level": level,
            "intervention_recommended": score >= 0.50
        }
