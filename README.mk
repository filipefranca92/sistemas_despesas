# Sistema de Controle de Despesas

Sistema web desenvolvido em **Python/Django** para gerenciamento e controle de despesas pessoais. A aplicação permite cadastrar, editar, excluir e consultar despesas, além de disponibilizar filtros por mês e ano, cálculo automático dos gastos mensais e paginação dos registros.

---

## Visão Geral

O Sistema de Controle de Despesas foi criado para auxiliar usuários no acompanhamento de seus gastos, proporcionando uma interface simples e objetiva para registro e consulta de despesas.

A aplicação foi desenvolvida utilizando o framework **Django**, seguindo o padrão **MVC (Model-View-Template)**, com persistência de dados em banco **MySQL**.

---

## Funcionalidades

### Cadastro de Despesas

* Registro de novas despesas.
* Informações armazenadas:

  * Valor
  * Descrição
  * Categoria
  * Data de cadastro

### Edição de Despesas

* Atualização de registros existentes.
* Alteração de valor, descrição e categoria.

### Exclusão de Despesas

* Remoção segura de registros cadastrados.

### Histórico de Despesas

* Visualização de todas as despesas cadastradas.
* Ordenação por data.

### Filtros

* Consulta por:

  * Mês
  * Ano

### Resumo Financeiro

* Cálculo automático do total gasto no período selecionado.

### Paginação

* Exibição de 5 registros por página para melhor desempenho e usabilidade.

---

## Categorias Disponíveis

O sistema possui categorias pré-definidas:

* Aluguel
* Luz
* Água
* Internet/TV
* Mercado
* Petshop
* Lazer
* Transporte
* Outros

---

## Tecnologias Utilizadas

### Backend

* Python 3.x
* Django 6.x

### Banco de Dados

* MySQL

### Frontend

* HTML5
* CSS3
* Django Templates

### Bibliotecas Utilizadas

* Django ORM
* Django Paginator
* Django Transactions

---

## Arquitetura do Projeto

```text
sistemas_despesas/
│
├── manage.py
│
├── projeto_despesas/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── despesas/
│   ├── migrations/
│   ├── templates/
│   │   └── despesas/
│   │       ├── home.html
│   │       ├── listar.html
│   │       ├── adicionar.html
│   │       ├── editar.html
│   │       └── excluir.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── db.sqlite3
```

---

## Modelo de Dados

### Entidade: Despesa

| Campo     | Tipo             |
| --------- | ---------------- |
| id        | Auto Increment   |
| valor     | Float            |
| descricao | Text             |
| data      | Date             |
| categoria | CharField        |
| usuario   | ForeignKey(User) |

---

## Regras de Negócio

### Cadastro

* Toda despesa deve possuir valor, descrição e categoria.

### Data

* A data é gerada automaticamente no momento do cadastro.

### Categoria

* Deve pertencer à lista de categorias previamente definida.

### Exclusão

* A remoção é permanente.

### Histórico

* As consultas podem ser filtradas por mês e ano.

---

## Segurança e Integridade

O projeto utiliza recursos nativos do Django para garantir integridade dos dados:

### Transações Atômicas

Operações críticas utilizam:

```python
@transaction.atomic
```

Garantindo que alterações sejam concluídas integralmente ou revertidas em caso de falha.

### Bloqueio de Registro

Utilização de:

```python
select_for_update()
```

para evitar conflitos de edição simultânea.

---

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/sistema-despesas.git
```

### 2. Acessar o Diretório

```bash
cd sistema-despesas
```

### 3. Criar Ambiente Virtual

```bash
python -m venv venv
```

### 4. Ativar Ambiente Virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5. Instalar Dependências

```bash
pip install django
pip install mysqlclient
```

---

## Configuração do Banco de Dados

No arquivo:

```python
projeto_despesas/settings.py
```

Configure as credenciais do MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'despesas_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

---

## Executando as Migrações

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## Criando Usuário Administrador

```bash
python manage.py createsuperuser
```

---

## Executando o Projeto

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000
```

---

## Rotas da Aplicação

| URL              | Descrição             |
| ---------------- | --------------------- |
| `/`              | Página inicial        |
| `/historico/`    | Histórico de despesas |
| `/adicionar/`    | Cadastro de despesa   |
| `/editar/<id>/`  | Edição de despesa     |
| `/excluir/<id>/` | Exclusão de despesa   |

---

## Melhorias Futuras

* Sistema completo de autenticação.
* Controle de despesas por usuário.
* Dashboard com gráficos.
* Exportação para Excel e PDF.
* Relatórios financeiros.
* Categorias personalizadas.
* API REST com Django REST Framework.
* Responsividade para dispositivos móveis.

---

## Licença

Este projeto é distribuído para fins acadêmicos e de aprendizado. A utilização em ambiente produtivo deve incluir adequações de segurança, autenticação, gerenciamento de credenciais e configurações de produção.

---

## Autor

**Sistema de Controle de Despesas**

Desenvolvido utilizando Python, Django e MySQL para gerenciamento eficiente de despesas pessoais e acompanhamento financeiro.
