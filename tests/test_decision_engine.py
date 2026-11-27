from xapp.decision_engine import DecisionEngine
from xapp.kpi import KPI


def test_handover_decision():
    engine = DecisionEngine()
    kpi = KPI("cell-1", 45, 50)

    assert engine.decide(kpi) == "HANDOVER"


def test_no_action_decision():
    engine = DecisionEngine()
    kpi = KPI("cell-2", 20, 50)

    assert engine.decide(kpi) == "NO_ACTION"