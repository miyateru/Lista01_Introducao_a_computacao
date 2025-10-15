# Lista01_Introducao_a_computacao

**Alunos:**
    > Arthur Fazzio Mendes
    > Lívia Rezende Masson

**Professor**
    > Rafael Serapilha Durelli.

**Semestre:** 2025/2

**Turma e Disciplina:** Turma 10A, de Bacharelado em Ciência da Computação 2025/02, pela UFLA.

**Versão utilizada do Python:** 3.13.7

****

# TODO

- [ ] Adicionar todos os testes
- [ ] Completar o README
    - [ ] Adicionar como executar os arquivos
- [ ] Atualizar interface
    - [ ] Tratar entradas invalidas
- [ ] Gravar vídeo funcionalidade
- [ ] Adicionar como executar exercicios indidualemente
- [ ] Adicionar como executar exercicios pela interface
- [ ] Terminar exercicio 10 + tratar entradas invalidas exercicio 10

## Uso

Testado para funcionar em Windows 11 e Linux (Ubuntu e Linux Mint). 
Necessita de python 3.13.7 instalado no sistema, e so utiliza as bibliotecas padrão de python. 
Caso python nessa versão não esteja instalado no seu sistema verifique como fazer a instalação na [pagina de download do python.org](https://www.python.org/downloads/).

## Especificações dos arquivos:

- Cada exercício proposto na Lista 01 está em seu respectivo arquivo *.py*, designado com a seguinte nomenclatura: "exercicio[número do exercício].py".

- O arquivo *"automated_tests.py"* designa os testes automatizados para cada exercício. Pode ser tanto visto pela interface ou pelo próprio arquivo, usando main_test().

- O arquivo *"errors_check.py"* engloba as funções de checagem de caracteres válidos para cada base numérica, e o posicionamento adequado do sinal negativo (-).
    Cada exercício importa essas funções de validação, para facilitação do entendimento do código e não precisar reutilizar as mesmas funções em diversos arquivos.

- O arquivo *"interface.py"* serve como uma interface de usuário geral para os exercícios e os testes automatizados. Basta executar o código com a versão mais recente de Python, e escolher as opções no terminal.
    - Todo arquivo de exercício também possui uma main() própria para testes individuais da atividade proposta.
