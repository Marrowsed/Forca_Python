# ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
[![CodeQL](https://github.com/Marrowsed/forca_python/actions/workflows/codeql.yml/badge.svg)](https://github.com/Marrowsed/controle_financeiro/actions/workflows/codeql.yml)

# Jogo da Forca em Python ! (Hangman Game)

## ✔️ Tecnologias utilizadas

![Django-Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/2560px-Django_logo.svg.png)

- ``Python``
- ``PostgreSQL``
- ``PyCharm``

## Instalação
É necessária a Instalação mais recente do <a href="https://www.python.org/downloads/" target="_blank">Python</a>

## Dependências</h2>

````sh
pip install -r requirements.txt
````

## Configuração
<ol>
  <li> Crie um arquivo `.env` na mesma pasta onde está o arquivo `migrate.py`.</li>
  <li>No seu terminal com o ambiente virtual ativado, execute o comando `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` para gerar uma chave secreta.</li>
  <li>Substitua a chave secreta no arquivo `.env` com a chave gerada na variável `SECRET_KEY`.</li>
  <li>Substitua o endereço do banco de dados no arquivo `.env` com o endereço do banco de dados que você deseja utilizar na variável `DATABASE_URL`.</li>
  <li>Execute o comando `python manage.py migrate` para criar as tabelas do banco de dados.</li>
</ol>

#TO DO
- Boneco da Forca aparecer automaticamente

## Rodando o projeto

```sh
python manage.py runserver
```

O servidor está rodando, visite http://127.0.0.1:8000/ no seu navegador de internet
