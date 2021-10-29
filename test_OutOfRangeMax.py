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

    tt.connect_to_endpoint()

    output, err = capfd.readouterr()
    assert output == [
        "Enter the twitter username you want to search for recent tweets about: ",
        "What's the maximum number of tweets you want to include in the calculation? (10-100): ",
        "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n"]

def test_ltMin(capfd):
    input_values = ["asmongold", "5"]
    output = []

    def simulated_input(s):
        output.append(s)
        return input_values.pop(0)
    tt.input = simulated_input
    tt.print = lambda s: output.append(s)

    tt.connect_to_endpoint()

    output, err = capfd.readouterr()
    assert output == [
        "Enter the twitter username you want to search for recent tweets about: ",
        "What's the maximum number of tweets you want to include in the calculation? (10-100): ",
        "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n"]

def test_crct(capfd):
    input_values = ["asmongold", "50"]
    output = []

    def simulated_input(s):
        output.append(s)
        return input_values.pop(0)
    tt.input = simulated_input
    tt.print = lambda s: output.append(s)

    tt.connect_to_endpoint()

    output, err = capfd.readouterr()
    assert output != [
        "Enter the twitter username you want to search for recent tweets about: ",
        "What's the maximum number of tweets you want to include in the calculation? (10-100): ",
        "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n"]
