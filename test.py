
import pytest
from sample.py import *

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
