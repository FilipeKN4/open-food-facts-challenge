# Python Challenge (Open Food Facts)

## Sobre o Projeto

O projeto se chama __open_food_facts__ e para a construção foram criados dois apps, que são:
* __account:__ utilizado para a criação de usuários e grupos
* __products:__ utilizado para a criação dos modelos de produtos e histórico de atualizações dos produtos

Além dos dois apps criados existe, por padrão, o app __open_food_facts__, criado ao iniciar o projeto.

## Instalação e Execução

Para utilizar o projeto, primeiramente é necessário definir as informações de conexão com o banco de dados que será utilizado, visto que foi utilizado o Mongo DB por meio da plataforma de cloud Atlas (https://www.mongodb.com/cloud/atlas). Essas definições devem ser feitas no arquivos __settings.py__ do app padrão __open_food_facts__.

Com o banco de dados devidamente configurado deve ser rodar o comando:

`docker-compose build`

Este comando irá gerar a imagem do projeto e instalar as dependências necessárias para a sua execução sendo necessário ser utilizado apenas uma vez. Em seguida, para executar o projeto, deve-se rodar o comando:

`docker-compose up`

Ou, para executar em segundo plano:

`docker-compose up -d`

Com esses comandos executados, o projeto estará rodando no endereço http://localhost:8000/.

## Testes

Para a execução dos testes deve-se utilizar o comando:

`docker-compose run django-rest ./manage.py test`

Ou, para executar os testes e gerar um relatório de cobertura:

`docker-compose run django-rest coverage run ./manage.py test`

E, para visualizar o relatório de cobertura:

`docker-compose run django-rest coverage report`

## Bibliotecas Utilizadas

Para a realização desse projeto foram utilizadas as seguintes bibliotecas:

* Django: https://www.djangoproject.com/
* DJango REST framework: https://www.django-rest-framework.org/
* Djongo: https://pypi.org/project/djongo/
* Psutil: https://pypi.org/project/psutil/
* Coverage: https://coverage.readthedocs.io/en/coverage-5.5/