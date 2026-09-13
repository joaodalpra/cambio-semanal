"""CLI: busca cotacoes diarias e, as sextas-feiras, gera o resumo semanal."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from src.fetcher import DOLAR_TICKER, buscar_acoes_hoje, buscar_dolar_hoje, data_hoje
from src.report import gerar_relatorio_semanal
from src.storage import adicionar_registro, carregar_historico, salvar_historico

HISTORICO_PATH = Path("data/history.json")

WATCHLIST = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA", "ABEV3.SA"]


def cmd_fetch() -> None:
    historico = carregar_historico(HISTORICO_PATH)
    hoje = data_hoje()

    dolar = buscar_dolar_hoje()
    if dolar is not None:
        adicionar_registro(historico, DOLAR_TICKER, hoje, dolar)
        print(f"Dolar hoje: R$ {dolar:.4f}")

    for ticker, preco in buscar_acoes_hoje(WATCHLIST).items():
        adicionar_registro(historico, ticker, hoje, preco)
        print(f"{ticker}: R$ {preco:.2f}")

    salvar_historico(HISTORICO_PATH, historico)

    if date.today().weekday() == 4:  # sexta-feira
        cmd_report()


def _precos_da_semana(historico: dict, ticker: str) -> list[float]:
    registros = historico.get(ticker, [])
    return [r["fechamento"] for r in registros[-5:]]


def cmd_report() -> None:
    historico = carregar_historico(HISTORICO_PATH)
    precos_dolar = _precos_da_semana(historico, DOLAR_TICKER)
    precos_acoes = {
        ticker: _precos_da_semana(historico, ticker)
        for ticker in WATCHLIST
        if _precos_da_semana(historico, ticker)
    }

    if not precos_dolar or not precos_acoes:
        print("Ainda nao ha dados suficientes no historico para gerar o resumo semanal.")
        return

    print(gerar_relatorio_semanal(precos_dolar, precos_acoes))


def main() -> None:
    parser = argparse.ArgumentParser(description="Cambio Semanal")
    parser.add_argument(
        "comando",
        choices=["fetch", "report"],
        help="fetch: busca cotacoes de hoje | report: gera o resumo semanal",
    )
    args = parser.parse_args()

    if args.comando == "fetch":
        cmd_fetch()
    else:
        cmd_report()


if __name__ == "__main__":
    main()
