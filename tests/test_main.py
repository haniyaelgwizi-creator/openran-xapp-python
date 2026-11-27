from xapp.main import main


def test_main_execution(capsys):
    main()

    captured = capsys.readouterr()

    assert "HANDOVER" in captured.out
    assert "Handover réussi" in captured.out
    assert "cell-1 : 70.0 %" in captured.out
    assert "cell-2 : 60.0 %" in captured.out
    assert "cell-3 : 20.0 %" in captured.out