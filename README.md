# Projeto Teste

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
    ```

    Se precisar do valor de alguma credencial, peça a algum colega.

    python -m uvicorn backend.main:app --reload
