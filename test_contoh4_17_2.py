# Import the necessary modules
import pytest
import unittest
from unittest.mock import patch
from contoh4_17 import *

# Test cases for the kira_purata function
def test_kira_purata_with_positive_values():
    assert kira_purata(10, 5) == 2.0

def test_kira_purata_with_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        kira_purata(10, 0)

@pytest.fixture
def mock_print(capsys):
    with patch('builtins.input', side_effect=['10', '20', 'X']), patch('sys.exit') as mock_exit:
        main()
    captured = capsys.readouterr()
    return captured.out

def test_main_with_valid_inputs(mock_print):
    expected_output = "Purata = 15.0\nTamat\n"
    assert mock_print == expected_output

@pytest.fixture
def mock_print2(capsys):
    with patch('builtins.input', side_effect=['X']), patch('sys.exit') as mock_exit:
        main()
    captured = capsys.readouterr()
    return captured.out

def test_main_with_no_inputs(mock_print2):
    expected_output = "Tamat\n"
    assert mock_print2 == expected_output
