**1)** Definição inicial da estrutura do projeto

```
├── app                      -- Diretorio Principal do Projeto
│   ├── api.py
│   ├── config.py
│   ├── log                  -- Diretorio onde conterão os Logs 
│   ├── requirements.txt     -- Arquivo de Requisitos
│   ├── settings.toml        -- Arquivo de Configuração do Dynaconf
│   └── src                  -- Diretorio de Código do Projeto
│       ├── db.py            -- Classe / Metodo de Conexão com o Banco de Dados
│       ├── __init__.py      -- Arquivo de Inicialização dos modulos
│       └── routes.py        -- Classe / Metodo de Rotas do Flask
├── COMMENTS.md
├── docker                   -- Diretorio para os arquivos Docker
│   ├── compose-db.yml       
│   ├── Dockerfile
│   ├── nginx
│   │   └── default.conf
│   └── table.sql
├── Makefile
└── README.md
```

**2)** Organização do codigo deixando mais modularizado, utilizando as bibilotecas
- **dynaconf** -- biblioteca de configuração de variáveis 
- **pyscopg2** -- biblioteca de conexão com o banco de dados

**3)** Preparando a api para salvar e consultar os comentários em um banco de dados **POSTGRESL**
**4)** Definindo o projeto para uso em container
**5)** Criando do compose para o banco de dados e o script inicial para criar a tabela
**6)** Definição inicial do Makefile
