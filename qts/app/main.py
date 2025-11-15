from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Sistema de Biblioteca - Validação de Cartão de Usuário", version="1.0.0"
)

CODIGO_CARTAO_VALIDADO = "BIBLIOTECA-ALUNO-001"


def cartao_e_valido(codigo: str) -> bool:
    """Retorna True se o código do cartão for exatamente o esperado"""
    return codigo == CODIGO_CARTAO_VALIDADO


@app.get("/cartao/{codigo}")
def verificar_cartao(codigo: str):
    """Endpoint de validação de cartão de biblioteca"""
    if cartao_e_valido(codigo):
        return {"card": codigo, "valid": True}
    raise HTTPException(status_code=400, detail="Cartão inválido")
