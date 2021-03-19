# buscar container pronto com versão alpine do node
FROM python:3.9

# Definir diretório principal da aplicação no container
WORKDIR /usr/app

# Copiar todos os arquivos gerados para dentro do container
COPY . .

# Rodar dependências do projeto
RUN pip install -r requirements.txt