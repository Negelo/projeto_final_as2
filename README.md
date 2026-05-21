# projeto_final_as2

Projeto da disciplina AS2: aplicação Django com boas práticas de administração de sistemas.

## Estado

- Repositório inicializado
- Estrutura base criada
- Dependências definidas
- Páginas principais implementadas

## Configuração local (ambiente virtual)

1. Criar venv:
   - Windows PowerShell: `python -m venv .venv`
2. Ativar venv:
   - Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
3. Instalar dependências:
   - `pip install -r requirements.txt`

## Variáveis de ambiente

1. Criar `.env` com base no exemplo:
   - `Copy-Item .env.example .env`
2. Ajustar os valores no `.env` para o teu ambiente.

## Base de dados

- Para MySQL (Docker/produção): `DB_ENGINE=mysql`
- Para SQLite (desenvolvimento local sem MySQL): `DB_ENGINE=sqlite`

## Docker

1. Build da imagem:
   - `docker build -t projeto-final-as2 .`
2. Correr container:
   - `docker run --rm -p 8000:8000 --env-file .env projeto-final-as2`

## Repositório

- GitHub: https://github.com/Negelo/projeto_final_as2
