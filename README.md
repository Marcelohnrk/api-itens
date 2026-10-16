# API de Itens

API REST feita com Python e FastAPI para gerenciar uma lista de itens
(lista de compras), com operações de criar, listar, atualizar e apagar.

> Projeto em desenvolvimento.

## Ferramentas

- Python
- FastAPI
- Uvicorn
- Pydantic

## Como rodar

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative o ambiente virtual:

   python -m venv venv
   venv\Scripts\activate

3. Instale as dependências:

   pip install -r requirements.txt

4. Inicie o servidor:

   uvicorn app.main:app --reload

5. Acesse a documentação interativa em http://127.0.0.1:8000/docs

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /itens | Lista todos os itens |
| GET | /itens/{id} | Busca um item pelo id |
| POST | /itens | Cria um item |
| PUT | /itens/{id} | Atualiza um item |
| DELETE | /itens/{id} | Apaga um item |

## Próximos passos

- [ ] Validação de dados em schemas
- [ ] Banco de dados SQLite
- [ ] Testes automatizados