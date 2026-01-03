import pytest 

def test_main():
    names = ["Bob", "Jim", "Becky", "Jim"]

    assert "Bob" in names, "Where's Bob?"
    assert "Jim" in names, "Where's Jim"

