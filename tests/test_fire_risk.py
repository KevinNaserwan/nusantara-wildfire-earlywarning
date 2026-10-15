
# Auto-generated incremental update
from src.early_warning import PeatlandFireRiskClassifier

def test_extreme_risk():
    r = PeatlandFireRiskClassifier.classify_risk(0.01, 20, 50, 38.0)
    assert r['alert_level'] == 'EXTREME'

