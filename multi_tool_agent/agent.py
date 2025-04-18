import requests
from google.adk.agents import Agent

def get_address_by_cep(cep: str) -> dict:
    """Consulta o endereço completo a partir de um CEP usando a API ViaCEP.

    Args:
        cep (str): CEP no formato '01001-000' ou apenas números '01001000'.

    Returns:
        dict: status e endereço completo ou mensagem de erro.
    """
    cep = cep.replace("-", "").strip()

    if not cep.isdigit() or len(cep) != 8:
        return {
            "status": "error",
            "error_message": "Formato de CEP inválido. Use 8 dígitos, com ou sem hífen.",
        }

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if "erro" in data:
            return {
                "status": "error",
                "error_message": f"CEP '{cep}' não encontrado.",
            }

        address = (
            f"{data['logradouro']}, {data['bairro']}, "
            f"{data['localidade']} - {data['uf']}, CEP: {data['cep']}"
        )

        return {
            "status": "success",
            "report": address,
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Erro ao consultar o CEP: {str(e)}",
        }

