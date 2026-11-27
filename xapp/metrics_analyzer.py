from xapp.kpi import KPI


class MetricsAnalyzer:
    def __init__(self):
        self.threshold = 80

    def is_congested(self, kpi: KPI):
        load = kpi.get_load()

        return load >= self.threshold