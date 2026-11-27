from xapp.kpi import KPI
from xapp.metrics_analyzer import MetricsAnalyzer


def test_congested_cell():
    analyzer = MetricsAnalyzer()
    kpi = KPI("cell-1", 45, 50)

    assert analyzer.is_congested(kpi) is True


def test_normal_cell():
    analyzer = MetricsAnalyzer()
    kpi = KPI("cell-2", 20, 50)

    assert analyzer.is_congested(kpi) is False


def test_threshold():
    analyzer = MetricsAnalyzer()
    kpi = KPI("cell-3", 40, 50)

    assert analyzer.is_congested(kpi) is True