"""
Fire & Moisture Spectral Indices Calculator for Tropical Peatlands.
"""
import numpy as np

class PeatlandFireIndices:
    """
    Computes spectral indices specialized for tropical peatland fire monitoring:
    - NBR: Normalized Burn Ratio (Burnt area discrimination & fire severity)
    - NDMI: Normalized Difference Moisture Index (Fuel moisture & drought proxy)
    - dNBR: Delta NBR for burn damage assessment
    """

    @staticmethod
    def calculate_nbr(nir: np.ndarray, swir2: np.ndarray) -> np.ndarray:
        """
        NBR = (NIR - SWIR2) / (NIR + SWIR2)
        For Sentinel-2: NIR is Band 8, SWIR2 is Band 12.
        """
        denom = nir + swir2
        return np.where(denom != 0, (nir - swir2) / denom, 0.0)

    @staticmethod
    def calculate_ndmi(nir: np.ndarray, swir1: np.ndarray) -> np.ndarray:
        """
        NDMI = (NIR - SWIR1) / (NIR + SWIR1)
        High correlation with peat ground water table and canopy dryness.
        """
        denom = nir + swir1
        return np.where(denom != 0, (nir - swir1) / denom, 0.0)

    @staticmethod
    def calculate_dnbr(pre_fire_nbr: np.ndarray, post_fire_nbr: np.ndarray) -> np.ndarray:
        """
        Delta NBR: assesses fire severity.
        > 0.66: High Severity
        0.44 - 0.66: Moderate-high
        0.27 - 0.44: Moderate-low
        0.10 - 0.27: Low Severity
        """
        return pre_fire_nbr - post_fire_nbr
