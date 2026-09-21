from src.report import gerar_relatorio_semanal


def test_gerar_relatorio_semanal_contem_dados_principais():
    precos_dolar = [5.00, 5.05, 5.10, 5.08, 5.12]
    precos_acoes = {
        "PETR4.SA": [30.0, 31.0, 29.0, 29.5, 29.0],
        "VALE3.SA": [60.0, 60.5, 59.5, 59.0, 59.5],
    }

    relatorio = gerar_relatorio_semanal(precos_dolar, precos_acoes)

    assert "PETR4.SA" in relatorio
    assert "VALE3.SA" in relatorio
    assert "Variacao na semana" in relatorio
    assert "NAO e recomendacao de investimento" in relatorio


def test_gerar_relatorio_semanal_aponta_maior_desconto():
    precos_dolar = [5.00, 5.10]
    precos_acoes = {
        "AAA": [10.0, 10.0],  # 0% de desconto em relacao a maxima
        "BBB": [10.0, 8.0],  # 20% de desconto -> maior oportunidade
    }

    relatorio = gerar_relatorio_semanal(precos_dolar, precos_acoes)

    trecho_final = relatorio.split("heuristica):")[1]
    assert "BBB" in trecho_final
