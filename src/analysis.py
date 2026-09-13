"""Funcoes puras de analise de precos (sem I/O), faceis de testar."""

from __future__ import annotations


def variacao_percentual(preco_inicial: float, preco_final: float) -> float:
    """Retorna a variacao percentual entre dois precos."""
    if preco_inicial == 0:
        raise ValueError("preco_inicial nao pode ser zero")
    return ((preco_final - preco_inicial) / preco_inicial) * 100


def resumo_semanal(precos: list[float]) -> dict:
    """Recebe os fechamentos diarios da semana (ordem cronologica) e devolve um resumo."""
    if not precos:
        raise ValueError("lista de precos vazia")
    return {
        "abertura": precos[0],
        "fechamento": precos[-1],
        "maxima": max(precos),
        "minima": min(precos),
        "variacao_pct": round(variacao_percentual(precos[0], precos[-1]), 2),
    }


def pontuacao_compra(precos: list[float]) -> float:
    """
    Heuristica simples e educacional: quanto mais o fechamento atual estiver
    abaixo da maxima da semana, maior a pontuacao (maior "desconto" aparente).
    Nao e recomendacao de investimento.
    """
    if not precos:
        raise ValueError("lista de precos vazia")
    maxima = max(precos)
    fechamento = precos[-1]
    if maxima == 0:
        return 0.0
    return round(((maxima - fechamento) / maxima) * 100, 2)


def melhor_oportunidade(precos_por_acao: dict[str, list[float]]) -> tuple[str, float]:
    """Retorna o ticker com a maior pontuacao de compra dentre as opcoes avaliadas."""
    if not precos_por_acao:
        raise ValueError("nenhuma acao informada")
    pontuacoes = {
        ticker: pontuacao_compra(precos) for ticker, precos in precos_por_acao.items()
    }
    melhor_ticker = max(pontuacoes, key=pontuacoes.get)
    return melhor_ticker, pontuacoes[melhor_ticker]
