from xapp.kpi import KPI


class NetworkSimulator:

    def __init__(self):

        self.cells = [
            KPI("cell-1", 45, 50),
            KPI("cell-2", 20, 50),
            KPI("cell-3", 10, 50)
        ]

    def get_kpis(self):

        return self.cells

    def handover(self, source, target, users):

        if (users > 0
                and source != target
                and source.users >= users
                and target.users + users <= target.capacity):

            source.users -= users
            target.users += users

            return True

        return False