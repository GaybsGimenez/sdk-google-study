# Multi Tool Agent com Google ADK

Projeto simples para testar o uso do **Google Agent Developer Kit (ADK)** com uma função personalizada que busca endereço pelo CEP usando a API ViaCEP.

🧠 Sobre o Google ADK
O Google ADK (Agent Developer Kit) é uma ferramenta recente da Google que permite criar agentes com:

Suporte nativo a chamadas de função

Interface web embutida para testes

Integração com modelos da API GenAI do Google

Mais detalhes: [Google ADK Docs](https://google.github.io/adk-docs/)

## Estrutura

```
multi_tool_agent/
├── agent.py      # Função get_address_by_cep
├── __init__.py
├── .env          # Contém GOOGLE_API_KEY
```

## Como usar

1. Crie e ative o ambiente virtual
2. Instale as dependências
3. Adicione sua chave no `.env`
4. Rode com:
```bash
adk web
```

Acesse [http://localhost:8000](http://localhost:8000) para testar.

