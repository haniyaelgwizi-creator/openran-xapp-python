from xapp.network_simulator import NetworkSimulator


def test_get_kpis():
    simulator = NetworkSimulator()

    cells = simulator.get_kpis()

    assert len(cells) == 3


def test_successful_handover():
    simulator = NetworkSimulator()
    cells = simulator.get_kpis()

    source = cells[0]
    target = cells[1]

    result = simulator.handover(source, target, 10)

    assert result is True
    assert source.users == 35
    assert target.users == 30


def test_failed_handover():
    simulator = NetworkSimulator()
    cells = simulator.get_kpis()

    source = cells[0]
    target = cells[1]

    result = simulator.handover(source, target, 40)

    assert result is False
    assert source.users == 45
    assert target.users == 20