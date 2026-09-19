from app import soma, subtracao, multiplicacao, divisao, eh_par
import pytest

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_subtracao():
    assert subtracao(10, 5) == 5
    assert subtracao(0, 5) == -5

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12
    assert multiplicacao(0, 10) == 0

def test_divisao():
    assert divisao(10, 2) == 5
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_eh_par():
    assert eh_par(2) == True
    assert eh_par(3) == False
    assert eh_par(0) == True
