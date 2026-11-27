from xapp.decision_engine import DecisionEngine
from xapp.ric_interface import RICInterface

def main():

    ric = RICInterface()

    engine = DecisionEngine()

    cells = ric.receive_kpis()

    for cell in cells:

        print("----------------------")

        print("Cellule :", cell.cell_id)

        print("Utilisateurs :", cell.users)

        print("Charge :", cell.get_load(), "%")

        decision = engine.decide(cell)

        print("Decision :", decision)

        if decision == "HANDOVER":

            for target in cells:

                if target != cell and target.get_load() < 80:

                    if ric.send_decision(cell, target, 10):
                        break

    print("\nEtat final des cellules :")

    for cell in cells:

        print(cell.cell_id, ":", cell.get_load(), "%")


if __name__ == "__main__":

    main()