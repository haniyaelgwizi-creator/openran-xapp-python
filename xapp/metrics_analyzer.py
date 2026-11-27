from xapp.kpi import KPI

class MetricsAnalyzer:

    def __init__(self):
        self.threshold = 80

    def is_congested(self, kpi: KPI):
        load = kpi.get_load()

        if load >= self.threshold:
            return True
        else:
            return False