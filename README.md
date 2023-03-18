# Sistema Distribuído

A proposta do projeto é de simular um sistema distribuído onde o projeto seja executado em três terminais com diferentes portas e todos tenham acesso aos mesmos dados inseridos, realizando as requisições a partir de uma rota de inserção de filme e uma para acessar os filmes cadastrados, que serão salvos em memória pelo redis.


## Configuração rápida

1. Este projeto utiliza o [Poetry](https://python-poetry.org/) para gerenciar suas dependências.
    Consulte a [documentação oficial](https://python-poetry.org/docs/#installation) para instalá-lo se ainda não o fez.
    **Este passo só precisa ser executado uma vez.**

1. **A versão utilizada do Python é a 3.10**.

  - Utilizando o [conda](https://docs.conda.io/en/latest/miniconda.html):
  - Crie um novo ambiente virtual:
    ```sh
    conda env create -f environment.yml
    ```
  - Ative o ambiente virtual:
    ```sh
    conda activate projeto-teste
    ```


1. Instale as dependências do backend:

    ```sh
    pip install "fastapi[all]"
    pip install sqlalchemy
    pip install sqlalchemy_utc
    pip install pymysql
    pip install pytest
    pip install factory-boy
    pip install requests
    pip install redis
    pip install pymongo
    ```

    python -m uvicorn backend.main:app --reload --port=8000

    Url swagger: http://localhost:8000/api/docs/

1. Para executar o arquivo redis.yml (necessária instalação do docker):
    ```
    docker-compose -f redis.yml up -d
    ```

