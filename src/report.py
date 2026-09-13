"""Geracao do relatorio semanal em texto."""

from __future__ import annotations

from src.analysis import melhor_oportunidade, resumo_semanal

AVISO = (
    "Este relatorio e gerado por um script educacional para praticar Python, "
    "APIs e DevOps. NAO e recomendacao de investimento."
)


def gerar_relatorio_semanal(
    precos_dolar_semana: list[float],
    precos_acoes_semana: dict[str, list[float]],
) -> str:
    resumo_dolar = resumo_semanal(precos_dolar_semana)
    ticker_melhor, pontuacao = melhor_oportunidade(precos_acoes_semana)

    linhas = [
        "===== Resumo semanal - Cambio Semanal =====",
        "",
        "Dolar (USD/BRL):",
        f"  Abertura da semana: R$ {resumo_dolar['abertura']:.4f}",
        f"  Fechamento da semana: R$ {resumo_dolar['fechamento']:.4f}",
        f"  Maxima: R$ {resumo_dolar['maxima']:.4f} | Minima: R$ {resumo_dolar['minima']:.4f}",
        f"  Variacao na semana: {resumo_dolar['variacao_pct']:.2f}%",
        "",
        "Acoes acompanhadas:",
    ]
    for ticker, precos in precos_acoes_semana.items():
        resumo_acao = resumo_semanal(precos)
        linhas.append(
            f"  {ticker}: variacao {resumo_acao['variacao_pct']:.2f}% "
            f"(fechamento R$ {resumo_acao['fechamento']:.2f})"
        )

    linhas += [
        "",
        f"Maior 'desconto' da semana (heuristica): {ticker_melhor} "
        f"({pontuacao:.2f}% abaixo da maxima semanal)",
        "",
        AVISO,
    ]
    return "\n".join(linhas)
