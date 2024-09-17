# CRUD---POO-em-Python
Projeto de CRUD para manipulação de dicionarios

# Projeto Final de Programação Orientada a Objetos (POO)

Este repositório contém o código do projeto final da disciplina de Programação Orientada a Objetos (POO) do curso de Engenharia de Dados da ADA Tech.

## Descrição

O projeto consiste em um sistema de gerenciamento de dicionários, onde é possível criar, visualizar, inserir, atualizar e deletar dicionários e suas respectivas chaves e valores. O sistema armazena os dados em um arquivo JSON para persistência.

## Estrutura do Código

O código está organizado em duas classes principais:

### Classe `Sistema`

A classe `Sistema` é responsável por gerenciar os dicionários. Ela possui os seguintes métodos:

- `__init__`: Inicializa a classe e carrega os dados do arquivo JSON.
- `criar(nome)`: Cria um novo dicionário com o nome fornecido.
- `ler(nome)`: Retorna o dicionário correspondente ao nome fornecido.
- `inserir(nome, chave, valor)`: Insere uma nova chave e valor no dicionário especificado.
- `atualizar(nome, chave_antiga, chave_nova, valor_novo)`: Atualiza uma chave e valor no dicionário especificado.
- `deletar(nome)`: Deleta o dicionário especificado.
- `deletar_chave(nome, chave)`: Deleta uma chave do dicionário especificado.
- `listar_dicionarios()`: Retorna uma lista com os nomes de todos os dicionários.
- `listar_chaves(nome)`: Retorna uma lista com as chaves do dicionário especificado.
- `salvar_dados()`: Salva os dicionários no arquivo JSON.
- `carregar_dados()`: Carrega os dicionários do arquivo JSON.

### Classe `Interface`

A classe `Interface` é responsável por interagir com o usuário. Ela possui o método `menu`, que exibe um menu de opções para o usuário escolher as operações a serem realizadas no sistema.

## Como Executar

Para executar o sistema, basta rodar o arquivo principal:
