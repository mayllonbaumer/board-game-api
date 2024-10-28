# Dockerfile
FROM python:3.9-slim

# Instala dependências
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o código da API
COPY . .

# Definir a variável de ambiente para o banco de dados MySQL
ENV DATABASE_URL=mysql://${DB_USER}:${DB_PASSWORD}@${DB_URL}:${DB_PORT}/${DB_NAME}

# Expõe a porta e define o comando de execução
EXPOSE 8080
CMD ["python", "app.py"]