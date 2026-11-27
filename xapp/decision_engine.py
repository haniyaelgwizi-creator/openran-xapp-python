from xapp.kpi import KPI
from xapp.metrics_analyzer import MetricsAnalyzer


class DecisionEngine:

    def __init__(self):
        self.analyzer = MetricsAnalyzer()

    def decide(self, kpi: KPI):

        if self.analyzer.is_congested(kpi):
            return "HANDOVER"
        else:
            return "NO_ACTION"