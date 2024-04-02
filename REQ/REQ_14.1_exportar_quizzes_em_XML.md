# IMPORTAR E EXPORTAR QUIZZES EM XML
Epic responsável por partilhar quizzes entre aplicações.
<br/>

`User Story #14` - Como utilizador quero poder exportar quizzes em XML para ser possivel exportar quizzes feitos na minha PL para a aplicação de outras turmas

* **Testes**: 
  * Testar exportar sem selecionar nenhum quiz
  * Testar exportar 100 quizzes
  * Testar exportar 1 quiz
  * Testar exportar sem login
  * Testar fazer refresh à página a meio da exportação
<br/>

`Caso de Uso #1-` 

__Ator Primário:__ Utilizador

__Nível:__ Objetivo do Utilizador

__Stakeholders e Interesses:__ Utilizador - consegue partilhar quizzes para outras aplicações

__Pré-condição:__ Estar registado no sistema

__Garantia Mínima:__ O sistema ter quizzes aprovados, ter acesso há pagina de perfil pessoal e há lista de quizzes aprovados

__Garantia de sucesso:__ O utilizador consegue partilhar os quizzes desejados com outra aplicação

__Cenário de Sucesso Principal:__
1. O utilizador acede ao seu perfil pessoal
2. O utilizador clica no botão de exportação
3. O utilizador é redirecionado para uma página com todos os quizzes validados.
4. O utilizador seleciona que quiz(es) quer exportar
5. Os quizzes são associados ao autor que os criou
6. Os quizzes são gerados em formato XML


__Extensões:__ 

3a. Não existem quizzes válidos disponiveis.
  3a1. O sistema informa o utilizador que não existem de momento quizzes verificados para exportar.
  3a2. O utilizador é redirecionado para a página do seu perfil pessoal.
4a. O utilizador não seleciona qualquer quiz
  4a1. O sistema informa o utilizador que não pode prosseguir sem antes selecionar qualquer quiz.
  4a2. O utilizador é redirecionado de novo para a página de seleção de quizzes.
6a. Erro ao gerar o ficheiro 
  6a1. O sistema apresenta uma mensagem informativa onde pede ao utilizador para tentar mais tarde.
  6a2. O utilizador é redirecionado para a página do ser perfil pessoal
