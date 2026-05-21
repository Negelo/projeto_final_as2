# projeto_final_as2

Aplicação Django simples para a disciplina AS2, com foco em práticas de administração de sistemas: Git/GitHub, variáveis de ambiente, Docker, Docker Compose e MySQL.

## Funcionalidades

- Página inicial com lista de publicações
- Página de detalhe da publicação (likes e comentários)
- Página com publicações por utilizador
- Dados persistidos na base de dados

## Requisitos

- Python 3.12+ (desenvolvimento local)
- Docker e Docker Compose (execução containerizada)

## Desenvolvimento Local

1. Criar ambiente virtual:
   - `python -m venv .venv`
2. Ativar ambiente virtual (PowerShell):
   - `.\.venv\Scripts\Activate.ps1`
3. Instalar dependências:
   - `pip install -r requirements.txt`
4. Criar `.env` com base no exemplo:
   - `Copy-Item .env.example .env`
5. Para local sem MySQL, usar no `.env`:
   - `DB_ENGINE=sqlite`
6. Aplicar migrações:
   - `python manage.py migrate`
7. Iniciar servidor:
   - `python manage.py runserver`

## Produção/Container (MySQL)

1. Criar `.env` a partir de `.env.example` e ajustar passwords.
2. Garantir no `.env`:
   - `DB_ENGINE=mysql`
   - `DB_HOST=db`
3. Subir serviços:
   - `docker compose up --build`
4. Aceder:
   - `http://localhost:8000`

## Estrutura de Serviços (Docker Compose)

- `web`: aplicação Django
- `db`: MySQL 8 com volume persistente `mysql_data`

## Variáveis de Ambiente

Ver `.env.example` para todas as variáveis necessárias.

## Repositório

- GitHub: https://github.com/Negelo/projeto_final_as2
