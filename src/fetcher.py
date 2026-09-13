"""Busca cotacoes diarias via yfinance (dolar e acoes da B3)."""

from __future__ import annotations

from datetime import date

import yfinance as yf

DOLAR_TICKER = "BRL=X"  # cotacao USD/BRL


def buscar_fechamento_atual(ticker: str) -> float | None:
    """Retorna o ultimo fechamento disponivel para o ticker informado."""
    dados = yf.Ticker(ticker).history(period="1d")
    if dados.empty:
        return None
    return round(float(dados["Close"].iloc[-1]), 4)


def buscar_dolar_hoje() -> float | None:
    return buscar_fechamento_atual(DOLAR_TICKER)


def buscar_acoes_hoje(watchlist: list[str]) -> dict[str, float]:
    resultado = {}
    for ticker in watchlist:
        preco = buscar_fechamento_atual(ticker)
        if preco is not None:
            resultado[ticker] = preco
    return resultado


def data_hoje() -> str:
    return date.today().isoformat()
