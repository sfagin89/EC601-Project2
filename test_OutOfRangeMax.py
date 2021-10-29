import tweetitude as tt
import pytest

def test_gtMax(capfd):
    input_values = ["asmongold", "105"]
    output = []

    def simulated_input(s):
        output.append(s)
        return input_values.pop(0)
    tt.input = simulated_input
    tt.print = lambda s: output.append(s)

    out, err = capfd.readouterr()
    assert out == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n"

def test_ltMin(capfd):
    input_values = ["asmongold", "5"]
    output = []

    def simulated_input(s):
        output.append(s)
        return input_values.pop(0)
    tt.input = simulated_input
    tt.print = lambda s: output.append(s)

    out, err = capfd.readouterr()
    assert out == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n"

def test_crct(capfd):
    input_values = ["asmongold", "50"]
    output = []

    def simulated_input(s):
        output.append(s)
        return input_values.pop(0)
    tt.input = simulated_input
    tt.print = lambda s: output.append(s)

    out, err = capfd.readouterr()
    assert out != "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n"
