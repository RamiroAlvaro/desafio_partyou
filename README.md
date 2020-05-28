# desafio_partyou
[![Build Status](https://travis-ci.org/RamiroAlvaro/desafio_partyou.svg?branch=master)](https://travis-ci.org/RamiroAlvaro/desafio_partyou)
[![codecov](https://codecov.io/gh/RamiroAlvaro/desafio_partyou/branch/master/graph/badge.svg)](https://codecov.io/gh/RamiroAlvaro/desafio_partyou)

https://desafiopartyou.herokuapp.com

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/RamiroAlvaro/desafio_partyou.git desafio_partyou
cd desafio_partyou
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-partyou .env
pytest partyou --cov=partyou
```

1. Faça as migrações
2. Crie um usuário
3. Rode o servidor local
```
python manage.py migrate
python manage.py createsuperuser
python manager.py runserver
```