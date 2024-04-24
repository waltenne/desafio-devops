# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie todo o projeto para o diretório de trabalho e instale as dependencias
COPY . /app
RUN pip install -r requirements.txt

# Comando para iniciar a aplicação usando Gunicorn
CMD ["gunicorn", "--log-level", "debug", "-b", "0.0.0.0:8000", "api:app"]
