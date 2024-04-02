# SELECIONAR TAGS PARA QUIZ
Esta epic é responsável por colocar uma tag no ato de criação de um quiz.

`User Story #12` - Como criador de quizzes quero poder selecionar pelo menos uma tag aquando da criação do quiz para que os testes possam ser criados com base nessas tags

### Testes:
    * O utilizador não seleciona nenhuma tag
    * O utilizador seleciona uma única tag
    * O utilizador seleciona múltiplas tags
    * O utilizador seleciona múltiplas tags e, de seguida, dessseleciona essas tags e tenta submeter o quiz
    * O utilizador seleciona múltiplas tags e, de seguida, desseleciona essas tags, seleciona apenas uma e submete o quiz
    * O utilizador cria um quizz com uma tag e, em seguida, cancela e cria outro quiz sem selecionar nenhuma tag
    * O utilizador cria um quiz com uma tag e, em seguida, cancela e cria outro quiz selecionando uma tag diferente
<br/>

`Caso de Uso #1-` Selecionar uma tag no ato de criação de um quizz

__Ator Primário:__ Criador

__Nível:__ Objetivo do criador

__Stakeholders e Interesses:__ Criadores, resolvedores, site

__Pré-condição:__ 
* Estar logado
* Estar na página de criação de quizz's aberta

__Garantia Mínima:__ Nenhuma

__Garantia de Sucesso:__ Conseguir selecionar uma tag no ato de criação de um quizz

__Cenário de Sucesso Principal:__

1. O utilizador está com a página de criação de quizz aberta
2. O utilizador seleciona uma tag 
   
__Extensões:__

2.a. O utilizador não seleciona nenhuma tag <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.a.1 A plataforma avisa que não foi selecionada nenhuma tag até ser selecionada pelo menos uma. <br/>
2.b. O utilizador seleciona múltiplas tags <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.b.1 A plataforma avisa que foram selecionadas múltiplas tags até ser selecionada apenas uma.