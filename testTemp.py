import pytest
from initSettings import cleanTempScale

def test_blank():
    assert cleanTempScale('') == 'C'

def test_none():
    assert cleanTempScale(None) == 'C'

def test_number():
    assert cleanTempScale(500) == 'C'

def test_properUseCase01():
    assert cleanTempScale("F") == 'F'

def test_properUseCase02():
    assert cleanTempScale("C") == 'C'    

def test_properUseCase03():
    assert cleanTempScale("Fahrenheit") == 'F'

def test_properUseCase04():
    assert cleanTempScale("Celsisus") == 'C'        