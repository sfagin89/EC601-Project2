import tweetitude as tt
import pytest

#def test_gtMax(monkeypatch):
#    monkeypatch.setattr('builtins.input', lambda _: "105")
#    tt.connect_to_endpoint()

#    i = input("What's the maximum number of tweets you want to include in the calculation? (10-100): ")

#    assert i == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n"

def test_gtMax(capfd):
    tt.input = lambda _: "105"
    tt.connect_to_endpoint()
    out, err = capfd.readouterr()

    assert out == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n\n"

def test_ltMin(capfd):
    tt.input = lambda _: "5"
    tt.connect_to_endpoint()
    out, err = capfd.readouterr()

    assert out == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n\n"

def test_crct(capfd):
    tt.input = lambda _: "50"
    tt.connect_to_endpoint()
    out, err = capfd.readouterr()

    assert out != "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n\n"
