import tweetitude as tt
from collections import deque
import pytest

# Creating Multiple Inputs to simulate user input for connect_to_endpoint
def gen_inputs(inputs):
    def next_input(_):
        return inputs.popleft()
    return next_input

# Testing API call, comparing result message of successful call
def test_gtMax(capfd, monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', gen_inputs(deque(["asmongold", "105"])))
    tt.connect_to_endpoint()
    _, err = capfd.readouterr()
    assert err == "Tweets retrieved\n"
