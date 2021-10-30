import tweetitude as tt
from collections import deque
import pytest

# Creating Multiple Inputs to simulate user input for connect_to_endpoint
def gen_inputs(inputs):
    def next_input(_):
        return inputs.popleft()
    return next_input

#For testing single input with the twitter user hardcoded
#def test_gtMax(capfd):
#    tt.input = lambda _: "105"
#    tt.connect_to_endpoint()
#    out, err = capfd.readouterr()
#    assert out == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n\n"

# Testing MaxTweet Input above the max range
def test_gtMax(capfd, monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', gen_inputs(deque(["asmongold", "105"])))
    tt.connect_to_endpoint()
    out, _ = capfd.readouterr()
    assert out == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n\n"

# Testing MaxTweet Input below the min range
def test_ltMinx(capfd, monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', gen_inputs(deque(["asmongold", "5"])))
    tt.connect_to_endpoint()
    out, _ = capfd.readouterr()
    assert out == "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n\n"

# Testing MaxTweet Input within the correct range
def test_crct(capfd, monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', gen_inputs(deque(["asmongold", "50"])))
    tt.connect_to_endpoint()
    out, _ = capfd.readouterr()
    assert out != "Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n\n"
