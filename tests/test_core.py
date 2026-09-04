import pytest
from versionkit import bump, compare, is_valid, parse


def test_parse():
    assert parse("1.2.3") == (1, 2, 3)


def test_compare():
    assert compare("1.2.0", "1.1.9") == 1
    assert compare("1.0.0", "1.0.0") == 0


def test_bump():
    assert bump("1.2.3", "major") == "2.0.0"
    assert bump("1.2.3", "minor") == "1.3.0"
    assert bump("1.2.3", "patch") == "1.2.4"


def test_validation():
    assert is_valid("0.0.1")
    assert not is_valid("v1.2.3")
    with pytest.raises(ValueError):
        parse("1.2")
