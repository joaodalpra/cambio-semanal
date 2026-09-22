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

## Rodando com Docker

```bash
docker build -t cambio-semanal .
docker run --rm cambio-semanal report
docker run --rm cambio-semanal fetch
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
.github/workflows/ci.yml    # CI: roda os testes a cada push/PR
.github/workflows/cd.yml     # CD: builda o pacote e publica como artefato do workflow
.github/workflows/notify.yml  # Alerta: envia notificacao no Discord a cada push no main
pyproject.toml                # metadados de build do pacote (usado pelo workflow de CD)
Dockerfile                    # imagem Docker para rodar a aplicacao em container
```

## CI/CD

- **CI** (`.github/workflows/ci.yml`): instala as dependencias e roda `pytest` a cada push e a cada pull request para `main`.
- **CD** (`.github/workflows/cd.yml`): builda um pacote distribuivel do projeto (`python -m build`) e publica o resultado como artefato do workflow a cada push/PR para `main`. Como este e um script CLI (sem servidor para implantar), o "deployment" aqui e a entrega continua de um pacote pronto para uso, em vez de um deploy para producao.
- **Alertas** (`.github/workflows/notify.yml`): envia uma mensagem para um canal do Discord a cada push no `main` (o que inclui todo merge de Pull Request), via um webhook guardado no secret `DISCORD_WEBHOOK`. Tambem pode ser disparado manualmente pela aba Actions (`workflow_dispatch`).
