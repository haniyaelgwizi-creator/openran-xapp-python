from xapp.network_simulator import NetworkSimulator


class RICInterface:

    def __init__(self):

        self.simulator = NetworkSimulator()

    def receive_kpis(self):

        return self.simulator.get_kpis()

    def send_decision(self, source, target, users):

        print("Demande de HANDOVER")

        result = self.simulator.handover(
            source, target, users
        )

        if result:
            print("Handover réussi")
        else:
            print("Handover refusé")

        return result