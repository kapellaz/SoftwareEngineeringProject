# CRIAR QUIZ
Epic responsável por criar quizz's de forma que o utilizador possa ter o máximo de qualidade nas perguntas que lhe são atribuidas.
<br/>

`User Story #5` - Como criador quero adicionar perguntas para criar um quizz.
### Testes:
  * Texto muito extenso (ultrapassa 512 caracteres);
  * Texto com caracteres inválidos;
  * Número de respostas inseridas diferente de 6;
  * Não insere a justificação da resposta;
  * Não insere a opção correta (verdadeira/falsa).
<br/>

`Caso de Uso #1-` Adicionar perguntas/respostas de um quizz


__Ator Primário:__ Criador

__Nível:__ Objetivo do criador

__Stakeholders e Interesses:__ Criadores, resolvedores, site

__Pré-condição:__ Estar logado e na página de criação de quizz aberta

__Garantia Mínima:__ Nenhuma

__Garantia de sucesso:__ Conseguir escrever uma pergunta, incluindo, se desejar, uma descrição, opção de submeter um quizz e opção de cancelamento de um quizz

__Cenário de Sucesso Principal:__
1. O utilizador está com a página de criação de quizz aberta
2. O utilizador insere uma pergunta na respetiva caixa
3. O utilizador insere uma descrição na respetiva caixa (opcional)
4. O utilizador insere as respostas correspondentes da pergunta
5. O utilizador indica se as respostas são verdadeiras ou falsas
6. O utilizador justifica o valor lógico das respostas
7. O utilizador pressiona o botão de cancelar (se desejar cancelar o quizz)
8. O utilizador pressiona o botão de submeter (se desejar submeter o quizz)

__Extensões:__ 

2.a. O utilizador não insere texto na caixa da pergunta <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.a.1. A plataforma avisa que não foi inserido texto até o utilizador inserir algo <br/>
2.b. O utilizador insere texto muito extenso (+ 512 caracteres), seja na caixa da pergunta, da descrição ou da resposta <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.b.1. A plataforma avisa que o texto inserido ultrapassa 512 caracteres <br/>
2.c. O utilizador insere caracter/es inválido/s, seja na caixa da pergunta, da descrição ou da resposta <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.c.1. A plataforma avisa que o/s caracter/es inserido/s foi/foram inválido/s <br/>
4.a. O utilizador insere um número de respostas diferente de 6 <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.a.1. A plataforma avisa que tem de inserir um número correto de respostas  <br/>
5.a. O utilizador não indica se a resposta é verdadeira ou falsa <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5.a.1. A plataforma avisa que tem de inserir o valor lógico das respostas  <br/>
5.b. O utilizador indica mais do que uma opção verdadeira <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5.b.1. A plataforma avisa que só é possível haver uma opção correta <br/>
6.a. O utilizador não insere texto na caixa da justificação <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6.a.1. A plataforma avisa que não foi inserido texto até o utilizador inserir algo <br/>