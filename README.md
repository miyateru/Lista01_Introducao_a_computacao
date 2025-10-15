# Lista01_Introducao_a_computacao

**Alunos:**

- Arthur Fazzio Mendes
- Lívia Rezende Masson

**Professor**

- Rafael Serapilha Durelli.

**Semestre:** 2025/2

**Turma e Disciplina:** Turma 10A, de Bacharelado em Ciência da Computação, pela UFLA.

**Versão utilizada do Python:** 3.13.7

****

# TODO

- [x] Adicionar todos os testes
- [ ] Completar o README
    - [ ] Adicionar como executar os arquivos
- [x] Atualizar interface
    - [x] Tratar entradas inválidas
- [ ] Gravar vídeo funcionalidade
- [x] Adicionar como executar exercicios indidualemente
- [x] Adicionar como executar exercicios pela interface
- [x] Terminar exercicio 10 + tratar entradas invalidas exercicio 10

## Uso

    Testado para funcionar em Windows 11 e Linux (Ubuntu e Linux Mint). 
Necessita de Python 3.13.7 instalado no sistema, e são utilizadas apenas as bibliotecas padrão de Python.

    Caso Python nessa versão não esteja instalado no sistema, verifique como fazer a instalação na [página de download do Python](https://www.python.org/downloads/).

## Especificações dos arquivos:

- Cada exercício proposto na Lista 01 está em seu respectivo arquivo *.py*, designado com a seguinte nomenclatura: "exercicio[número do exercício].py".

- O arquivo *"automated_tests.py"* designa os testes automatizados para cada exercício. Pode ser tanto visto pela interface quanto pelo próprio arquivo, utilizando main_test().

- O arquivo *"errors.py"* engloba as funções de checagem de caracteres válidos para cada base numérica, e o posicionamento adequado do sinal negativo (-).

    Cada exercício importa essas funções de validação, para facilitação do entendimento do código e não precisar reutilizar as mesmas funções em diversos arquivos.

- O arquivo *"interface.py"* serve como uma interface de usuário geral para os exercícios e os testes automatizados. Basta executar o código com a versão mais recente de Python (demonstrada no tópico abaixo), e escolher as opções descritas no terminal.
    - Todo arquivo de exercício também possui uma main() própria para testes individuais da atividade proposta.

## Execução de exercícios:

- Caso queira executar os exercícios individuais (sem a ajuda da interface), ou a interface, ou ainda os testes automatizados pelo terminal, basta seguir esses passos:
    * Entre na pasta do projeto e copie o seu endereço;
    * Em uma aba de terminal, digite o comando "cd \endereço\da\lista\01", e aperte Enter;
    * Agora, digite *"py"*/*"python"*/*"python3"* na linha de comando (dependendo do sistema operacional utilizado), e o nome do exercício, junto com a terminação ".py".

- Exemplo: 'py exercicio01.py'
