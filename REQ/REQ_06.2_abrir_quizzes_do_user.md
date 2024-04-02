# VER HISTORICO DE QUIZZES CRIADOS
Esta epic é responsavel por mostrar o historico de todos os quizz's criados pelo utilizador.

`User Story #6` - Como criador quero ser capaz de ver os Quizz's que criei, bem como as suas opções e o seu status

### Testes:
    * Tentar aceder a quizz's de outros utilizadores
    * Tentar aceder a quizz's que não existem
    * Testar com quizz de estado reprovado
    * Testar com quizz de estado diferente de reprovado
<br/>

`Caso de Uso #2-` Aceder aos detalhes de um Quizz criado pelo Utilizador

__Ator Primário:__ Criador

__Nível:__ Objetivo do criador

__Stakeholders e Interesses:__ Criadores, resolvedores, site

__Pré-condição:__ 
* Estar logado
* ter feito Quizz's
* ter selecionado um quizz

__Garantia Mínima:__ Nenhuma

__Garantia de sucesso:__ Conseguir visualizar os detalhes do quizz selecionado

__Cenário de Sucesso Principal:__
1. Estar na página de detalhes de um quizz criado <br/>
2. A página apresenta toda a informação do quizz selecionado
3. O utilizador clica no botão de editar (se pretender editar um quizz que foi reprovado) <br/>

__Extensões:__ 

1.a O utilizador tenta aceder a um quizz não criado por si<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.a.1 A plataforma avisa que o quizz correspondente não foi criado por si<br/>
1.b O utilizador tenta aceder a um quizz que não existe <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.b.1 A plataforma avisa que o quizz correspondente não existe<br/>
3.a. O utilizador criou quizz's que foram reprovados <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3.a.1. A plataforma disponibiliza a opção de editar estes quizz's <br/>