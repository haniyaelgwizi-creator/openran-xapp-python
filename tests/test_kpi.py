from xapp.kpi import KPI


def test_get_load():
    kpi = KPI("cell-1", 45, 50)
    assert kpi.get_load() == 90.0


def test_empty_cell():
    kpi = KPI("cell-2", 0, 50)
    assert kpi.get_load() == 0.0


def test_full_cell():
    kpi = KPI("cell-3", 50, 50)
    assert kpi.get_load() == 100.0