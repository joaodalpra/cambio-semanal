# Cambio Semanal

Projeto de estudo (Python + DevOps) que acompanha a cotacao diaria do dolar (USD/BRL) e de uma pequena lista de acoes da B3, e gera um resumo no fim de cada semana.

> **Aviso:** este projeto tem fins **educacionais** (praticar Python, consumo de APIs e CI/CD). A "pontuacao de compra" e uma heuristica simples baseada na distancia ate a maxima da semana -- **nao e recomendacao de investimento**.

## Como funciona

- `python main.py fetch` -- busca a cotacao de hoje do dolar e das acoes acompanhadas e salva em `data/history.json`. Se hoje for sexta-feira, ja imprime o resumo semanal.
- `python main.py report` -- gera o resumo semanal a partir do historico salvo, a qualquer momento.

## Acoes acompanhadas

PETR4, VALE3, ITUB4, BBDC4, ABEV3 (editavel em `main.py`, variavel `WATCHLIST`).

## Instalacao

```bash
pip install -r requirements.txt
```

## Rodando os testes

```bash
pytest -v
```

## Estrutura

```
main.py                   # CLI (fetch / report)
src/
  fetcher.py               # busca cotacoes via yfinance
  storage.py                # persistencia local em JSON
  analysis.py                # calculos puros (variacao, pontuacao de compra)
  report.py                   # geracao do texto do resumo semanal
tests/
  test_analysis.py             # testes unitarios
.github/workflows/ci.yml    # roda os testes a cada push/PR
```
