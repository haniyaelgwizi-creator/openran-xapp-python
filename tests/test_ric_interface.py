from xapp.ric_interface import RICInterface


def test_receive_kpis():
    ric = RICInterface()

    cells = ric.receive_kpis()

    assert len(cells) == 3


def test_send_decision_success():
    ric = RICInterface()
    cells = ric.receive_kpis()

    result = ric.send_decision(cells[0], cells[1], 10)

    assert result is True
    assert cells[0].users == 35
    assert cells[1].users == 30


def test_send_decision_failure():
    ric = RICInterface()
    cells = ric.receive_kpis()

    result = ric.send_decision(cells[0], cells[1], 40)

    assert result is False
    assert cells[0].users == 45
    assert cells[1].users == 20