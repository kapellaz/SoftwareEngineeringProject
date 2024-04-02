# IMPORTAR E EXPORTAR QUIZZES EM XML
Epic responsável por partilhar quizzes entre aplicações.
<br/>

`User Story #15` - Como utilizador quero poder importar quizzes em XML para ser possivel importar quizzes criados noutra PL para a minha aplicação

* **Testes**: 
  * Ficheiro para importação sem questões
  * Ficheiro para importação não contem tags
  * Ficheiro para importação com quizzes em duplicado
  * Ficheiro com mais de mil quizzes
  * Não utilização do CRLF-Carriage Return Line Feed
  * Incompatibilidade do formato com a aplicação de destino
<br/>

`Caso de Uso #1-` 

__Ator Primário:__ Utilizador

__Nível:__ Objetivo do Utilizador

__Stakeholders e Interesses:__ Utilizador - consegue importar quizzes para a aplicação

__Pré-condição:__ Estar registado no sistema

__Garantia Mínima:__ Ter um quiz para importar em formato XML, estar registado no sistema

__Garantia de sucesso:__ O utilizador consegue importar o(s) quiz(es) desejados para a aplicação

__Cenário de Sucesso Principal:__
1. O utilizador acede ao seu perfil pessoal
2. O utilizador clica no botão de importação
3. O utilizador é redirecionado para uma página onde faz upload de um ficheiro XML
4. O utilizador seleciona que ficheiro importar 
5. O quiz é importado em estado por verificar

__Extensões:__ 
4a. O utilizador seleciona um ficheiro sem ser em formato XML
  4a1. O sistema informa o utilizador que os ficheiros selecionados têm de ser, obrigatoriamente, em formato XML
  4a2. O utilizador pode voltar a selecionar outros ficheiros
5a. Erro ao importar o ficheiro XML
  5a1. O sistema apresenta uma mensagem informativa onde pede ao utilizador para tentar mais tarde.
  5a2. O utilizador é redirecionado para a página do ser perfil pessoal
