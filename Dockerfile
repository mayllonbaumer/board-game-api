# Dockerfile
FROM python:3.9-slim

# Instala dependências
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o código da API
COPY . .

# Expõe a porta e define o comando de execução
EXPOSE 8080
CMD ["python", "app.py"]