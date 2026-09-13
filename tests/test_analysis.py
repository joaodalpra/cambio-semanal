import pytest

from src.analysis import (
    melhor_oportunidade,
    pontuacao_compra,
    resumo_semanal,
    variacao_percentual,
)


def test_variacao_percentual_alta():
    assert variacao_percentual(5.0, 5.5) == 10.0


def test_variacao_percentual_queda():
    assert round(variacao_percentual(5.5, 5.0), 2) == -9.09


def test_variacao_percentual_preco_inicial_zero():
    with pytest.raises(ValueError):
        variacao_percentual(0, 5.0)


def test_resumo_semanal():
    precos = [5.00, 5.10, 4.95, 5.20, 5.05]
    resumo = resumo_semanal(precos)
    assert resumo == {
        "abertura": 5.00,
        "fechamento": 5.05,
        "maxima": 5.20,
        "minima": 4.95,
        "variacao_pct": 1.0,
    }


def test_resumo_semanal_lista_vazia():
    with pytest.raises(ValueError):
        resumo_semanal([])


def test_pontuacao_compra():
    precos = [10.0, 10.5, 11.0, 9.0]
    assert pontuacao_compra(precos) == 18.18


def test_melhor_oportunidade():
    precos_por_acao = {
        "PETR4.SA": [30.0, 31.0, 29.0],
        "VALE4.SA": [60.0, 60.0, 59.5],
    }
    ticker, pontuacao = melhor_oportunidade(precos_por_acao)
    assert ticker == "PETR4.SA"
    assert pontuacao == 6.45


def test_melhor_oportunidade_sem_dados():
    with pytest.raises(ValueError):
        melhor_oportunidade({})
