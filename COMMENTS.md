**1)** Definição inicial da estrutura do projeto

```
.
├── app
│   ├── api.py
│   ├── compose                -- Diretorio de arquitetura em docker
│   │   ├── compose-db.yml
│   │   ├── compose-dev.yml
│   │   └── table.sql
│   ├── config.py
│   ├── Dockerfile             
│   ├── log                    -- Diretorio de logs
│   ├── requirements.txt
│   ├── settings.toml          -- Arquivo de configuração
│   └── src                    -- Diretorio dos modulos
│       ├── db.py
│       ├── __init__.py
│       └── routes.py
├── COMMENTS.md
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
