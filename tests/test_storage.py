from src.storage import adicionar_registro, carregar_historico, salvar_historico


def test_adicionar_registro_novo():
    historico = {}
    historico = adicionar_registro(historico, "BRL=X", "2026-09-21", 5.10)
    assert historico == {"BRL=X": [{"data": "2026-09-21", "fechamento": 5.10}]}


def test_adicionar_registro_nao_duplica_mesma_data():
    historico = {"BRL=X": [{"data": "2026-09-21", "fechamento": 5.10}]}
    historico = adicionar_registro(historico, "BRL=X", "2026-09-21", 5.50)
    assert len(historico["BRL=X"]) == 1
    assert historico["BRL=X"][0]["fechamento"] == 5.10


def test_adicionar_registro_ordena_por_data():
    historico = {}
    historico = adicionar_registro(historico, "BRL=X", "2026-09-22", 5.20)
    historico = adicionar_registro(historico, "BRL=X", "2026-09-21", 5.10)
    datas = [r["data"] for r in historico["BRL=X"]]
    assert datas == ["2026-09-21", "2026-09-22"]


def test_salvar_e_carregar_historico(tmp_path):
    caminho = tmp_path / "sub" / "history.json"
    historico = {"BRL=X": [{"data": "2026-09-21", "fechamento": 5.10}]}

    salvar_historico(caminho, historico)

    assert caminho.exists()
    assert carregar_historico(caminho) == historico


def test_carregar_historico_inexistente(tmp_path):
    caminho = tmp_path / "nao-existe.json"
    assert carregar_historico(caminho) == {}
