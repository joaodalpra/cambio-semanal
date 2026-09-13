"""Persistencia simples do historico de precos em um arquivo JSON local."""

from __future__ import annotations

import json
from pathlib import Path


def carregar_historico(caminho: Path) -> dict:
    if not caminho.exists():
        return {}
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def salvar_historico(caminho: Path, historico: dict) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def adicionar_registro(historico: dict, ticker: str, data: str, fechamento: float) -> dict:
    """Adiciona um registro diario ao historico, evitando duplicar a mesma data."""
    registros = historico.setdefault(ticker, [])
    if any(r["data"] == data for r in registros):
        return historico
    registros.append({"data": data, "fechamento": fechamento})
    registros.sort(key=lambda r: r["data"])
    return historico
